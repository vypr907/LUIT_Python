import boto3

resource = boto3.resource("s3")

bucketList = list(resource.buckets.all()) #can make a list from the returned data

print(len(bucketList)) #how many buckets do I have?

for bucket in resource.buckets.all(): #loop and print all my buckets
    print(bucket.name)
