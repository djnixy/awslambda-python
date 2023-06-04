import boto3
import os

def lambda_handler(event, context):
    # Extract the instance ID from the event
    instance_id = event['instance_id']

    # Retrieve AWS credentials from environment variables
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    region = os.environ['AWS_REGION']

    # Create a Boto3 session using the environment variables
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region
    )

    # Create an EC2 client using the session
    ec2_client = session.client('ec2')

    # Stop the EC2 instance
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    # Return a response
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        message = f"EC2 instance {instance_id} has been stopped successfully."
    else:
        message = f"Failed to stop EC2 instance {instance_id}."

    return {
        'statusCode': 200,
        'body': message
    }
