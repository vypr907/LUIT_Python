import boto3

tags = []

def create_apache_ec2(client,tags):
    try:
        client.run_instances(MaxCount=1,
                         MinCount=1,
                         ImageId="ami-02d1e544b84bf7502",
                         InstanceType="t2.micro",
                         TagSpecifications=tags,
                         #KeyName="private-ec2",
                         #SecurityGroups=["launch-wizard-6"],
                         #UserData=boot_apache2_script,
                         )
        print("Started")
    except:
        print("Failed")
    


client = boto3.client('ec2')

#creating tags for instances
def tag_spec(user_key, user_value):
    global tags
    tags = [
            {
            "ResourceType":"instance",
            "Tags": [
                    {
                        "Key": user_key,
                        "Value": user_value
                    }
                ]
        }
    ]


#UNCOMMENT FOR USERDATA SCRIPT
#boot_apache2_script='''#!/bin/bash
#apt update -y
#apt upgrade -y
#apt-get install -y apache2
#systemctl start apache2
#systemctl enable apache2'''


def main():
    num_to_create = int(input("How many EC2 instances do you want to create: "))
    user_key = input("Please enter a tag for the instance. Key: ")
    user_value = input("Value: ")
    tag_spec(user_key,user_value)
    
    
    for i in range(num_to_create):
        create_apache_ec2(client,tags)
    


if __name__=="__main__":
    main()