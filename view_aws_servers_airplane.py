import airplane
import boto3

@airplane.task(
    slug="view_aws_servers",
    name="View AWS Servers",
)
def view_aws_servers():
    ec2 = boto3.resource('ec2')

    data = []

    for instance in ec2.instances.all():
        data.append({
            "ID": instance.id,
            "Amazon Machine Image (AMI)": instance.image_id,
            "Type": instance.instance_type,
            "IP Address": instance.public_ip_address,
            "State": instance.state['Name']
        })

    # Sort the data in ascending order by ID.
    data = sorted(data, key=lambda u: u["ID"])

    if not data:
        return [{"Output": 'No servers found.'}]

    # You can return data to show output to users.
    # Output documentation: https://docs.airplane.dev/tasks/output
    return data
