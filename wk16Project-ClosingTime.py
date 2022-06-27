#!/usr/bin/env python3.7

# --------------------------------------------------------------
# Program: Closing Time
# Programmer: Steven Laszloffy
# Project: LUIT Week 16
# Purpose: A simple program that shuts down all EC2 instances
# - protects the cloud9 instance
# - only stops "running" instances that have the Environment: Dev tag
# ---------------------------------------------------------------

import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

reservations = response["Reservations"]

tagKey = "Name"
tagVal = "Test"



#function to get the list of instances that have the right tag        
def list_ec2_by_tag(tagKey, tagVal):
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+tagKey,
                'Values': [tagVal]
            }
        ]
    )
    ec2List = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            ec2List.append(instance["InstanceId"])
            
    return ec2List
    
#function to terminate the correct instances
def ec2_nuke(tgt_list):
    
    #///NUKE\\\        
    ec2_client.terminate_instances(InstanceIds=tgt_list)
    


def main():
    print(list_ec2_by_tag(tagKey,tagVal))
    ec2_nuke(list_ec2_by_tag(tagKey,tagVal))


if __name__=="__main__":
    main()