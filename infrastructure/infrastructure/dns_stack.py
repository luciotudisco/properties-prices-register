from aws_cdk import Stack
from aws_cdk import aws_elasticloadbalancingv2
from aws_cdk import aws_route53
from aws_cdk import aws_route53_targets
from constructs import Construct


class DNSStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        domain_name: str,
        api_alb: aws_elasticloadbalancingv2.ApplicationLoadBalancer,
        portal_alb: aws_elasticloadbalancingv2.ApplicationLoadBalancer,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.hosted_zone = aws_route53.HostedZone.from_lookup(self, "HostedZone", domain_name=domain_name)

        self.api_dns_record = aws_route53.ARecord(
            self,
            "ARecordAPI",
            zone=self.hosted_zone,
            record_name="api",
            target=aws_route53.RecordTarget.from_alias(aws_route53_targets.LoadBalancerTarget(api_alb)),
        )

        self.portal_dns_record = aws_route53.ARecord(
            self,
            "ARecordPortal",
            zone=self.hosted_zone,
            target=aws_route53.RecordTarget.from_alias(aws_route53_targets.LoadBalancerTarget(portal_alb)),
        )
