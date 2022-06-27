import boto3

ec2_client = boto3.client("ec2")

x = ec2_client.describe_instances()
data = x["Reservations"]

li=[]

for instances in data:
    instance = instances["Instances"]
    for ids in instance:
        instance_id = ids["InstanceId"]
        if ("i-0fb72f66a357269cd" != instance_id): #don't list Cloud9 EC2
            print(instance_id)
            li.append(instance_id)

#///NUKE\\\        
ec2_client.terminate_instances(InstanceIds=li)
        
        
