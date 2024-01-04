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
        alb: aws_elasticloadbalancingv2.ApplicationLoadBalancer,
        domain_name: str,
        subdomain_name: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.hosted_zone = aws_route53.HostedZone.from_lookup(self, "HostedZone", domain_name=domain_name)

        self.dns_record = aws_route53.ARecord(
            self,
            "ARecord",
            zone=self.hosted_zone,
            record_name=subdomain_name,
            target=aws_route53.RecordTarget.from_alias(aws_route53_targets.LoadBalancerTarget(alb)),
        )
