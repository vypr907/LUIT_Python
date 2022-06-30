#lambda to backup all EC2 instances with tag <backup:true>
from datetime import datetime

import boto3

def lambda_handler(event, context):
    #create the client
    ec2_client = boto3.client('ec2')
    
    #get a list of all the regions
    regions = [region['RegionName']
        for region in ec2_client.describe_regions()['Regions']]
        
    for region in regions:
        print('Instances in EC2 Region {}:'.format(region))
        ec2 = boto3.resource('ec2',region_name=region)
        
        #filter out tagged instances
        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup','Values': ['true']}
            ]
        )
        
        #create a timestamp
        #ISO 8601 timestamp, i.e. 2022-03-31T14:01:58
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        
        for i in instances.all():
            for v in i.volumes.all():
                desc = 'Backup of {0}, volume {1}, create {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)
                
                snapshot = v.create_snapshot(Description=desc)
                
                print("Created snapshot:",snapshot.id)