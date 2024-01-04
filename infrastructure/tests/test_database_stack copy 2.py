import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.database_stack import DatabaseStack
from infrastructure.network_stack import NetworkStack


def test_db_created():
    app = core.App()
    network_stack = NetworkStack(app, "NetworkStack")
    database_stack = DatabaseStack(app, "DatabaseStack", database_name="test_db", vpc=network_stack.vpc)
    template = assertions.Template.from_stack(database_stack)
    template.has_resource_properties("AWS::RDS::DBCluster", {"DatabaseName": "test_db"})
