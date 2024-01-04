import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.network_stack import NetworkStack


def test_vpc_created():
    app = core.App()
    network_stack = NetworkStack(app, "NetworkStack")
    template = assertions.Template.from_stack(network_stack)
    template.has_resource_properties("AWS::EC2::VPC", {"EnableDnsSupport": True})
