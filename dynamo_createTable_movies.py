import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Movies2',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH' # partition key
            
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE' # sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print('Table status:',table.table_status)

print('Waiting for',table.name,'to complete creating...')
#block execution until table is ready
table.meta.client.get_waiter('table_exists').wait(TableName='Movies2')
print('Table status:',dynamodb.Table('Movies2').table_status)