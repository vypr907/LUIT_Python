#how to describe AWS EBS volume snapshot using boto3 and python
import boto3
ec2=boto3.client("ec2")
ec2.describe_snapshots(SnapshotIds=['<snapshot id>'])