#!/usr/bin/env python3

from aws_cdk import core

from sagemakerStudioCDK.sagemaker_studio_stack import SagemakerStudioStack
from sagemakerStudioCDK.jumpstart_model_stack import JumpStartModelStack

import os
import boto3

sts_client = boto3.client("sts")
account_id = os.environ.get('CDK_DEFAULT_ACCOUNT', sts_client.get_caller_identity()["Account"])
region = os.environ.get('CDK_DEFAULT_REGION', 'eu-central-1')

model_package_arn = (
    "arn:aws:sagemaker:eu-central-1:865070037744:model-package/huggingface-eqa-distilbert-base-cased"
)

app = core.App()

SagemakerStudioStack(app, "SagemakerStudioStack", env={"account": account_id, 'region': region})


JumpStartModelStack(
    app,
    "JumpStartModelStack",
    env={"account": account_id, "region": region},
    model_package_arn=model_package_arn,
    # instance_type="ml.m5.large",  # optional override
)

app.synth()

