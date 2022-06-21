import boto3

s3_resource = boto3.client("s3")

s3_resource.list_buckets()["Buckets"][0]["Name"]



print("___________________")         #    [item][list index][attribute]
creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
print(creation_date)
print("____________________")
creation_date.strftime("%d%m%y_%H:%M:%s") #alternate way to format the contents
print(creation_date)
print("____________________")

#print all the buckets and their creation date
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])