#how to delete an AWS EBS volume snapshot using boto3 and python

import boto3
ec2=boto3.client("ec2")

ec2.delete_snapshot(SnapshotId='<snapshot id goes here>')