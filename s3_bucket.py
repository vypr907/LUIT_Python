#!/usr/bin/env python3.7

#using boto3 to create a new S3 bucket

import boto3

aws_resource = boto3.resource("s3") #create the resource to call the right AWS thing

bucket = aws_resource.Bucket("wk16temp") #name that shizzle

response = bucket.create(
    ACL = 'public-read',   #set the access settings for your bucket
    CreateBucketConfiguration = {
        'LocationConstraint': 'us-east-2'
    },
)


print(response)