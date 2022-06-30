import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    print("hello from lambda")
    print((event))
    records = event["Records"]
    for record in records:
        key = record["s3"]["object"]["key"]
        print(key)
        
        response = sns.publish (
            TargetArn = "arn:aws:sns:us-east-2:107900886402:s3_topic",
            Message = json.dumps(key)
            )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
