from aws_cdk import Aws
from aws_cdk import Stack
from aws_cdk import aws_ecs
from aws_cdk import aws_secretsmanager
from constructs import Construct


class SecretsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, database_secrets: aws_secretsmanager.ISecret, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Secret values required by the app which are stored in the Secrets Manager
        # This values will be injected as env vars on runtime
        self.secrets = {
            "DB_HOST": aws_ecs.Secret.from_secrets_manager(database_secrets, field="host"),
            "DB_PORT": aws_ecs.Secret.from_secrets_manager(database_secrets, field="port"),
            "DB_NAME": aws_ecs.Secret.from_secrets_manager(database_secrets, field="dbname"),
            "DB_USER": aws_ecs.Secret.from_secrets_manager(database_secrets, field="username"),
            "DB_PASSWORD": aws_ecs.Secret.from_secrets_manager(database_secrets, field="password"),
            "DJANGO_SECRET_KEY": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("DJANGO_SECRET_KEY")),  # nosec
            "AWS_ACCESS_KEY_ID": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("AWS_ACCESS_KEY_ID")),  # nosec
            "AWS_SECRET_ACCESS_KEY": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("AWS_SECRET_ACCESS_KEY")),  # nosec
            "GOOGLE_MAPS_API_KEY": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("GOOGLE_MAPS_API_KEY")),  # nosec
            "ALGOLIA_APP_ID": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("ALGOLIA_APP_ID")),  # nosec
            "ALGOLIA_API_KEY": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("ALGOLIA_API_KEY")),  # nosec
            "SENTRY_DNS": aws_ecs.Secret.from_secrets_manager(self._from_secret_name("SENTRY_DNS")),  # nosec
        }

    def _from_secret_name(self, secret_name: str) -> aws_secretsmanager.Secret:
        return aws_secretsmanager.Secret.from_secret_partial_arn(
            self, secret_name, secret_partial_arn=f"arn:aws:secretsmanager:{Aws.REGION}:{Aws.ACCOUNT_ID}:secret:{secret_name}"
        )
