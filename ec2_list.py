import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

reservations = response["Reservations"]

for reservation in reservations:
    instances = reservation["Instances"]
    for instance in instances:
        instanceId = instance["InstanceId"]
        if("i-03c38a1757c4f0702" != instanceId): #don't list Cloud9 EC2
            print(instanceId)