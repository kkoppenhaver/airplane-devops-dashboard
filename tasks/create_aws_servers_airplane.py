import airplane
import boto3


@airplane.task(
    slug="create_aws_servers",
    name="Create AWS Servers",
)
def create_aws_servers():
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instances = ec2.create_instances(
        ImageId="ami-0aa7d40eeae50c9a9",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="keanan-aws"
    )
    
    return 'EC2 instance is being created.'
