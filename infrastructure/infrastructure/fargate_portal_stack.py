from aws_cdk import Duration
from aws_cdk import Stack
from aws_cdk import aws_certificatemanager
from aws_cdk import aws_ec2
from aws_cdk import aws_ecs
from aws_cdk import aws_ecs_patterns
from aws_cdk import aws_elasticloadbalancingv2
from aws_cdk import aws_ssm
from constructs import Construct


class FargatePortalStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        ecs_cluster: aws_ecs.Cluster,
        task_cpu: int = 256,
        task_memory_mib: int = 1024,
        tasks_count: int = 1,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.domain_certificate = aws_certificatemanager.Certificate.from_certificate_arn(
            self, "RootDomainCertificate", certificate_arn=aws_ssm.StringParameter.value_for_string_parameter(self, "RootDomainCertificate")
        )

        # Create the load balancer, ECS service and fargate task for the NextJS UI portal
        self.alb_fargate_service = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "ApplicationLoadBalancedFargatePortal",
            protocol=aws_elasticloadbalancingv2.ApplicationProtocol.HTTPS,
            certificate=self.domain_certificate,
            redirect_http=True,
            platform_version=aws_ecs.FargatePlatformVersion.LATEST,
            cluster=ecs_cluster,
            task_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.PUBLIC),
            assign_public_ip=True,
            cpu=task_cpu,
            memory_limit_mib=task_memory_mib,
            desired_count=tasks_count,
            task_image_options=aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=aws_ecs.ContainerImage.from_asset(
                    directory="../portal",
                    file="docker/Dockerfile",
                ),
                container_name="Portal",
                container_port=3000,
            ),
            public_load_balancer=True,
            health_check_grace_period=Duration.seconds(180),
        )

        self.alb_fargate_service.target_group.configure_health_check(
            path="/api/health",
            timeout=Duration.seconds(10),
            healthy_threshold_count=2,
            unhealthy_threshold_count=2,
            interval=Duration.seconds(30),
        )

        scalable_target = self.alb_fargate_service.service.auto_scale_task_count(min_capacity=1, max_capacity=2)
        scalable_target.scale_on_cpu_utilization("CpuScaling", target_utilization_percent=70)
