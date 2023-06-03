import boto3

def lambda_handler(event, context):
    # Extract the instance ID and secret key from the event
    instance_id = event['instance_id']
    aws_access_key_id = event['aws_access_key_id']
    aws_secret_access_key = event['aws_secret_access_key']

    # Create a Boto3 session using the provided credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
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