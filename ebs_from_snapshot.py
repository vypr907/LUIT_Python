import boto3
ec2=boto3.client("ec2")

#create an AWS EBS Volume from snapshot using boto3 and python

ec2.create_volume(
    AvailabilityZone = 'us-east-2c',
    Encrypted = True,
    Size = 12,
    SnapshotId = 'snap-07100547d9ae39f13',
    VolumeType = 'gp2')
    