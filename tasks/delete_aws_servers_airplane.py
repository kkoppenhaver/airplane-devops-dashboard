import airplane
import boto3


@airplane.task(
    slug="delete_aws_servers",
    name="Delete AWS Servers"
)
def delete_aws_servers(instance_id :str):
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    ec2.instances.filter(InstanceIds = [instance_id]).terminate()

    return 'EC2 instance is being terminated.'
