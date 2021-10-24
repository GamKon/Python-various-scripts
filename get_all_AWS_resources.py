# Print out formatted JSON of all AWS resources by TAG

import boto3
import json

#from boto3.session import Session

def get_available_regions(service):
    available_regions = []
    all_regions = boto3.Session().get_available_regions(service)
    for region in all_regions:
        sts = boto3.Session(region_name=region).client('sts')
        try:
            sts.get_caller_identity()
            available_regions.append(region)
        except:# ClientError as e:
            #if e.response['Error']['Code'] == "InvalidClientTokenId":
                pass
            #else:
            #    raise
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
#            print(f"{instance_id}, {instance_type}, public_ip, {private_ip}")
            found_instances[instance_id] = [instance_type,private_ip]
    return found_instances
            

            
##my_session = Session()
#ec2_regions = my_session.get_available_regions("ec2")
#ec2_regions.remove("af-south-1")
#print(ec2_regions)
ec2_regions = get_available_regions("ec2")

for region_to_inspect in ec2_regions:
#    print(region_to_inspect)
    #test_region = "af-south-1"
    ec2_in_region_list = get_ec2_instances(region_to_inspect)
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