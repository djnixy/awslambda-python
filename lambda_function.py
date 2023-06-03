import boto3

def lambda_handler(event, context):
    # Extract the instance ID from the event
    instance_id = event['instance_id']

    # Create a Boto3 client for EC2
    ec2_client = boto3.client('ec2')

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