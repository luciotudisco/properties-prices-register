from aws_cdk import Stack
from aws_cdk import aws_ec2
from aws_cdk import aws_ecs
from constructs import Construct


class NetworkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = aws_ec2.Vpc(
            self,
            "VPC",
            max_azs=2,  # default is all AZs in region
            nat_gateways=0,  # default is 1 NAT gateway per AZ
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                    map_public_ip_on_launch=True,
                ),
            ],
        )

        self.ecs_cluster = aws_ecs.Cluster(self, "ECSCluster", vpc=self.vpc)
