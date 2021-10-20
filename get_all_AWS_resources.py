# Print out formatted JSON of all AWS resources by TAG

import boto3
import json

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
