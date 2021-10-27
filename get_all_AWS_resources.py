# Print out formatted JSON of all AWS resources by TAG

import boto3
import json


def get_available_regions(service):
    available_regions = []
    all_regions = boto3.Session().get_available_regions(service)
    for region in all_regions:
        sts = boto3.Session(region_name=region).client('sts')
        try:
            sts.get_caller_identity()
            available_regions.append(region)
        except Exception as e: #ClientError
            if e.response['Error']['Code'] == "InvalidClientTokenId":
                pass
            else:
                raise
    return available_regions


def get_ec2_instances(region):
    found_instances = {}
    ec2_client = boto3.client("ec2", region_name=region)
    reservations = ec2_client.describe_instances().get("Reservations")
#    print(reservations)
#        Filters=[
#        {
#            "Name": "instance-state-name",
#            "Values": ["running"],
#        }]).get("Reservations")
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
#            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            instance_state = instance["State"]["Name"]
            instance_tags = instance["Tags"]
            found_instances[instance_id] = [instance_tags,instance_type,private_ip,instance_state]
    return found_instances


#ec2_regions = ["ca-central-1"]
ec2_regions = ['ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
#ec2_regions = get_available_regions("ec2")

for region_to_inspect in ec2_regions:
    ec2_in_region_list = get_ec2_instances(region_to_inspect)
    if len(ec2_in_region_list) > 0:
        print(f"EC2 instances in region {region_to_inspect}:\n{json.dumps(ec2_in_region_list, indent=4)}")


"""
#Select by tags

client = boto3.client('resourcegroupstaggingapi')
resources_list_json = client.get_resources(
    TagFilters=[
        {
            'Key': 'Owner',
            'Values': [
                'GamKon',
            ]
        },
    ],
)

print("__________________________________________________________________")
json_formatted_str = json.dumps(resources_list_json, indent=2)
print(json_formatted_str)
"""