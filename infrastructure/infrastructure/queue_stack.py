from aws_cdk import Stack
from aws_cdk import aws_sqs
from constructs import Construct


class QueuesStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.celery_queue = aws_sqs.Queue(self, "CelerySQSQueue", queue_name="celery-queue")
