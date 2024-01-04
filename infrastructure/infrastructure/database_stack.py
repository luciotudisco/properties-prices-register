from aws_cdk import Duration
from aws_cdk import Stack
from aws_cdk import aws_ec2
from aws_cdk import aws_rds
from constructs import Construct


class DatabaseStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: aws_ec2.Vpc,
        database_name: str,
        min_capacity: aws_rds.AuroraCapacityUnit = aws_rds.AuroraCapacityUnit.ACU_2,
        max_capacity: aws_rds.AuroraCapacityUnit = aws_rds.AuroraCapacityUnit.ACU_4,
        auto_pause_minutes: int = 30,  # Shutdown after minutes of inactivity to save costs
        backup_retention_days: int = 1,  # 1 day retention is free
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.aurora_serverless_db = aws_rds.ServerlessCluster(
            self,
            "AuroraServerlessCluster",
            engine=aws_rds.DatabaseClusterEngine.aurora_postgres(version=aws_rds.AuroraPostgresEngineVersion.VER_13_9),
            vpc=vpc,
            vpc_subnets=aws_ec2.SubnetSelection(subnet_type=aws_ec2.SubnetType.PUBLIC),
            default_database_name=database_name,
            backup_retention=Duration.days(backup_retention_days),
            deletion_protection=True,
            enable_data_api=True,  # Allow running queries in AWS console (free)
            scaling=aws_rds.ServerlessScalingOptions(
                auto_pause=Duration.minutes(auto_pause_minutes),
                min_capacity=min_capacity,
                max_capacity=max_capacity,
            ),
        )
