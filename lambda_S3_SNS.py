#uses a lambda to send the item name to an email (via SNS) whenever item gets uploaded to an S3 bucket
import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):

    records = event["Records"]
    for record in records:
        key = record["s3"]["object"]["key"] #key being the name of the uploaded object
        print(key)
        
        response = sns.publish (
            TargetArn = "arn:aws:sns:us-east-2:107900886402:s3_topic", #topic that has the lambda and an email address subscribed to it
            Message = json.dumps(key)
            )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
