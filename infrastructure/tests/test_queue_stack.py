import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.queue_stack import QueuesStack


def test_queues_created():
    app = core.App()
    queues_stack = QueuesStack(app, "QueuesStack")
    template = assertions.Template.from_stack(queues_stack)
    template.has_resource_properties("AWS::SQS::Queue", {"QueueName": "celery-queue"})
