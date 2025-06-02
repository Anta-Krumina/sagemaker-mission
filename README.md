# sagemaker-mission
Repository contains required infrastructure code to deploy SageMaker Studio and deploy AWS pre-trained model all using Python CDK. 2 seperate CloudFormation stack are going to be created, one for SageMaker Studio and another one for model deployment.

## deployment steps
Step 1: Clone this repository and cd into sagemaker-mission

`git clone https://github.com/Anta-Krumina/sagemaker-mission.git`  <br>

`cd sagemaker-mission/`

Step 2: Create and activate virtual environment:

`python3 -m venv .cdk-sagemaker-venv` <br>

`source .cdk-sagemaker-venv/bin/activate`


Step 3: Install the required dependencies:

`pip3 install -r requirements.txt`

Step 4: Synthesize the templates =  produce AWS CloudFormation template for each stack defined in the application:

`cdk synthesize`

Step 5: Deploy the solution.

`cdk deploy --all`

### To deploy model manually
1. Opem SageMaker Studio
1.1. navigate to Amazon SageMaker AI > Domains > User Profile > Launch > Studio
2. Deploy Model
2.2. Jumpstart > Choose any model > Deploy
