import boto3

num_to_create = int(input("How many EC2 instances do you want to create: "))

def create_apache_ec2(client):
    try:
        client.run_instances(MaxCount=1,
                         MinCount=1,
                         ImageId="ami-02d1e544b84bf7502",
                         InstanceType="t2.micro",
                         #KeyName="private-ec2",
                         #SecurityGroups=["launch-wizard-6"],
                         #UserData=boot_apache2_script,
                         )
        print("Started")
    except:
        print("Failed")
    


client = boto3.client('ec2')


#UNCOMMENT FOR USERDATA SCRIPT
#boot_apache2_script='''#!/bin/bash
#apt update -y
#apt upgrade -y
#apt-get install -y apache2
#systemctl start apache2
#systemctl enable apache2'''

for i in range(num_to_create):
    create_apache_ec2(client)
