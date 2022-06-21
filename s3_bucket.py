#!/usr/bin/env python3.7

#using boto3 to create a new S3 bucket

import boto3

aws_resource = boto3.resource("s3")

bucket = aws_resource.Bucket("wk16temp")

response = bucket.create(
    ACL = 'public-read',
    CreateBucketConfiguration = {
        'LocationConstraint': 'us-east-2'
    },
)


print(response)