import aws_cdk as core
import aws_cdk.assertions as assertions

from infrastructure.s3_stack import S3Stack


def test_s3_buckets_created():
    app = core.App()
    s3_stack = S3Stack(app, "S3Stack")
    template = assertions.Template.from_stack(s3_stack)
    template.has_resource_properties("AWS::S3::Bucket", {"BucketName": "properties-prices-register-static-images"})
