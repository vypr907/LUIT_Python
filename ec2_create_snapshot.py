import boto3
ec2=boto3.client("ec2")

ec2.create_snapshot(Description='snapshot from base volume using python',VolumeId='vol-0f9175450a0bec37d')