#!/usr/bin/env python3
import aws_cdk as cdk

from infrastructure.database_stack import DatabaseStack
from infrastructure.dns_stack import DNSStack
from infrastructure.fargate_portal_stack import FargatePortalStack
from infrastructure.fargate_service_stack import FargateServiceStack
from infrastructure.fargate_workers_stack import FargateWorkersStack
from infrastructure.network_stack import NetworkStack
from infrastructure.queue_stack import QueuesStack
from infrastructure.secrets_stack import SecretsStack

app = cdk.App()
env = cdk.Environment(account="367736719156", region="eu-west-1")

network_stack = NetworkStack(
    scope=app,
    construct_id="NetworkStack",
    env=env,
)

queue_stack = QueuesStack(
    scope=app,
    construct_id="QueuesStack",
    env=env,
)

database_stack = DatabaseStack(
    scope=app,
    construct_id="DatabaseStack",
    vpc=network_stack.vpc,
    database_name="ppr",
    env=env,
)

secrets_stack = SecretsStack(
    scope=app,
    construct_id="SecretsStack",
    database_secrets=database_stack.aurora_serverless_db.secret,
    env=env,
)

fargate_service_stack = FargateServiceStack(
    scope=app,
    construct_id="FargateServiceStack",
    ecs_cluster=network_stack.ecs_cluster,
    secrets=secrets_stack.secrets,
    env=env,
)

fargate_workers_stack = FargateWorkersStack(
    scope=app,
    construct_id="FargateWorkersStack",
    celery_queue=queue_stack.celery_queue,
    ecs_cluster=network_stack.ecs_cluster,
    secrets=secrets_stack.secrets,
    env=env,
)

fargate_portal_stack = FargatePortalStack(
    scope=app,
    construct_id="FargatePortalStack",
    ecs_cluster=network_stack.ecs_cluster,
    env=env,
)

dns_stack = DNSStack(
    scope=app,
    construct_id="DNSStack",
    domain_name="irishpropertiesprices.com",
    api_alb=fargate_service_stack.alb_fargate_service.load_balancer,
    portal_alb=fargate_portal_stack.alb_fargate_service.load_balancer,
    env=env,
)

app.synth()
