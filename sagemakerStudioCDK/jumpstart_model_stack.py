"""
A very small CDK stack that deploys one JumpStart model->endpoint
purely by pulling in the CloudFormation YAML with `CfnInclude`.

You only need to pass in the JumpStart model package ARN when
instantiating the stack from app.py.
"""

import pathlib
# from aws_cdk import (
#     aws_cloudformation_include as cfn_inc,
#     Stack,
# )
from constructs import Construct


from aws_cdk import (
	core, aws_iam as iam
)

import aws_cdk.cloudformation_include as cfn_inc

class JumpStartModelStack(core.Stack):


    # from sagemaker.jumpstart.model import JumpStartModel

    # model_id = "autogluon-forecasting-chronos-bolt-small"
    # my_model = JumpStartModel(model_id=model_id)
    # predictor = my_model.deploy()

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        model_package_arn: str,
        instance_type: str = "ml.t2.medium",
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ----------------------------------------------------------
        # Locate the YAML template that lives under
        # sagemakerStudioConstructs/sagemakerJumpStartCloudformationStack/
        # ----------------------------------------------------------
        template_path = (
            pathlib.Path(__file__).parent.parent  # go up from SagemakerStudioStack/
            / "sagemakerStudioConstructs"
            / "sagemakerJumpStartCloudformationStack"
            / "sagemaker-jumpstart-endpoint-template.yaml"
        )

        # ----------------------------------------------------------
        # Pull the YAML into the stack
        # ----------------------------------------------------------
        include = cfn_inc.CfnInclude(
            self,
            "JumpStartEndpointTemplate",
            template_file=str(template_path),
            parameters={
                "JumpStartModelPackageArn": model_package_arn,
                "InstanceType": instance_type,
            },
        )

        # Handy attribute you can import-value or reference elsewhere
        self.endpoint_name = include.get_resource("JumpStartEndpoint").ref
