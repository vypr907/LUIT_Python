import boto3

#not needed, but saving for future use
#from pathlib import Path
#file = Path("/LUIT_Python/paintball.png")

#how to upload single file ______________________________________
s3_resource = boto3.client("s3")

s3_resource.upload_file(
    Filename = "./LUIT_Python/paintball.png",
    Bucket = "wk16temp",
    Key = "uploadTestPaintball.png")
#_________________________________________________________________


#how to upload multiple files ____________________________________    
import os
import glob

cwd = os.getcwd()
cwd = cwd + "/LUIT_Python/randomFiles/"

#print(cwd)

#lets upload *ONLY* .png files (in this case, should actually only be one file)
files = glob.glob(cwd + "*.png")

#print(files)

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
        Filename = file,
        Bucket = "wk16temp",
        Key = file.split("/")[-1])
#_________________________________________________________________