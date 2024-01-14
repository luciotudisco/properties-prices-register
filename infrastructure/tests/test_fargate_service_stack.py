import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.database_stack import DatabaseStack
from infrastructure.fargate_service_stack import FargateServiceStack
from infrastructure.network_stack import NetworkStack
from infrastructure.secrets_stack import SecretsStack


def test_fargate_service_with_alb_created():
    app = core.App()
    network_stack = NetworkStack(app, "NetworkStack")
    database_stack = DatabaseStack(app, "DatabaseStack", database_name="test_db", vpc=network_stack.vpc)
    secrets_stack = SecretsStack(app, "SecretsStack", database_secrets=database_stack.aurora_serverless_db.secret)
    fargate_service_stack = FargateServiceStack(
        app, "FargateServiceStack", ecs_cluster=network_stack.ecs_cluster, secrets=secrets_stack.secrets
    )
    template = assertions.Template.from_stack(fargate_service_stack)
    template.has_resource_properties("AWS::ECS::Service", {"LaunchType": "FARGATE"})
    template.has_resource_properties("AWS::ElasticLoadBalancingV2::LoadBalancer", {"Type": "application"})
