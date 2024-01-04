from aws_cdk import Stack
from aws_cdk import aws_s3
from constructs import Construct


class S3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a public S3 bucket for the properties images retrieved from Google Street View etc.
        self.s3_bucket = aws_s3.Bucket(
            self,
            id="PropertiesPricesRegisterImagesBucket",
            bucket_name="properties-prices-register-static-images",
            public_read_access=True,
            block_public_access=aws_s3.BlockPublicAccess(
                block_public_acls=False,
                ignore_public_acls=False,
                block_public_policy=False,
                restrict_public_buckets=False,
            ),
        )
