import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.database_stack import DatabaseStack
from infrastructure.fargate_workers_stack import FargateWorkersStack
from infrastructure.network_stack import NetworkStack
from infrastructure.queue_stack import QueuesStack
from infrastructure.secrets_stack import SecretsStack


def test_fargate_workers_created():
    app = core.App()
    network_stack = NetworkStack(app, "NetworkStack")
    database_stack = DatabaseStack(app, "DatabaseStack", database_name="test_db", vpc=network_stack.vpc)
    secrets_stack = SecretsStack(app, "SecretsStack", database_secrets=database_stack.aurora_serverless_db.secret)
    queue_stack = QueuesStack(app, "QueuesStack")
    fargate_workers_stack = FargateWorkersStack(
        app,
        "FargateServiceStack",
        ecs_cluster=network_stack.ecs_cluster,
        secrets=secrets_stack.secrets,
        celery_queue=queue_stack.celery_queue,
    )
    template = assertions.Template.from_stack(fargate_workers_stack)
    template.resource_properties_count_is("AWS::ECS::Service", {"LaunchType": "FARGATE"}, 2)
