import boto3

#how to delete a single object from an S3 bucket_________________________

s3_resource = boto3.client("s3")

#s3_resource.delete_object(Bucket = 'wk16temp', Key = 'uploadTestPaintball.png')
#________________________________________________________________________


#how to delete multiple objects from an S3 bucket________________________
import os
import glob

#find all the objects from the bucket
objects = s3_resource.list_objects(Bucket = "wk16temp")["Contents"]

#iterate and delete
for object in objects:
    print(object["Key"])
    s3_resource.delete_object(Bucket = 'wk16temp',
    Key = object["Key"])
#________________________________________________________________________