#lambda to clean up snapshots. will delete all except last three
import boto3

def lambda_handler(event, context):
    
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    
    #get a list of all the regions
    regions = [region['RegionName']
        for region in ec2_client.describe_regions()['Regions']]
        
    for region in regions:
        print('Instances in EC2 Region {}:'.format(region))
        ec2 = boto3.resource('ec2',region_name=region)
        
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]
        
        #sort snapshots by date ascending
        snapshots.sort(key=lambda x: x["StartTime"])
        
        #remove snapshots we want to keep (i.e. 3 most recent)
        snapshots = snapshots[:-3]
        
        for snapshot in snapshots:
            id = snapshot['SnapshotId']
            try:
                print("Deleting snaptshot:",id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print("Snapshot {} in use, skipping.".format(id))
                    continue