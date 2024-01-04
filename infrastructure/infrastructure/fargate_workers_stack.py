from typing import Mapping

from aws_cdk import Stack
from aws_cdk import aws_ec2
from aws_cdk import aws_ecs
from aws_cdk import aws_ecs_patterns
from aws_cdk import aws_secretsmanager
from aws_cdk import aws_sqs
from constructs import Construct


class FargateWorkersStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        ecs_cluster: aws_ecs.Cluster,
        celery_queue: aws_sqs.Queue,
        secrets: Mapping[str, aws_secretsmanager.Secret],
        task_cpu: int = 256,
        task_memory_mib: int = 1024,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.celery_beat = aws_ecs_patterns.QueueProcessingFargateService(
            self,
            "CeleryBeat",
            queue=celery_queue,
            platform_version=aws_ecs.FargatePlatformVersion.LATEST,
            cluster=ecs_cluster,
            task_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.PUBLIC),
            assign_public_ip=True,
            cpu=task_cpu,
            memory_limit_mib=task_memory_mib,
            image=aws_ecs.ContainerImage.from_asset(
                directory="../service",
                file="docker/Dockerfile",
            ),
            container_name="CeleryBeat",
            environment={
                "SQS_DEFAULT_QUEUE_URL": celery_queue.queue_url,
            },
            secrets=secrets,
            command=["bash", "-c", "poetry run celery -A ppr beat -l info"],
        )

        self.celery_workers = aws_ecs_patterns.QueueProcessingFargateService(
            self,
            "CeleryWorkers",
            queue=celery_queue,
            platform_version=aws_ecs.FargatePlatformVersion.LATEST,
            cluster=ecs_cluster,
            task_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.PUBLIC),
            assign_public_ip=True,
            cpu=task_cpu,
            memory_limit_mib=task_memory_mib,
            image=aws_ecs.ContainerImage.from_asset(
                directory="../service",
                file="docker/Dockerfile",
            ),
            container_name="CeleryWorkers",
            environment={
                "SQS_DEFAULT_QUEUE_URL": celery_queue.queue_url,
            },
            secrets=secrets,
            command=["bash", "-c", "poetry run celery -A ppr worker -l info"],
            max_scaling_capacity=10,
            scaling_steps=[
                {"upper": 0, "change": -1},  # 0 msgs = 0 workers
                {"lower": 1, "change": +1},  # 1 msg = 1 worker
                {"lower": 100, "change": +1},  # 100 msgs = 2 workers
                {"lower": 200, "change": +2},  # 200 msgs = 4 workers
                {"lower": 2000, "change": +6},  # 2000 msgs = 10 workers
            ],
        )
