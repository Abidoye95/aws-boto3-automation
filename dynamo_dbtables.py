import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# create your table

table = dynamodb.create_table(
    TableName='Hulu_Top10Movies', #enter table name
    KeySchema=[
        {
            'AttributeName': 'ranking',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ranking',
            'AttributeType': 'N'    #number
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
# print message
print("Table status:", table.table_status)

# connect to dynamodb using boto3
import boto3

client = boto3.client('dynamodb',
  aws_access_key_id='AKIAVCJV2CXERONRWDGH',
  aws_secret_access_key='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',
  region_name='us-east-1')

#add items to table
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Hulu_Top10Movies') #input table name

#add items to table

with table.batch_writer() as batch:
	batch.put_item(Item={"ranking": 1, "title": "Prey"})
	batch.put_item(Item={"ranking": 2, "title": "Abandoned"})
	batch.put_item(Item={"ranking": 3, "title": "Medieval"})
	batch.put_item(Item={"ranking": 4, "title": "The Estate"})
	batch.put_item(Item={"ranking": 5, "title": "Boston strangler"})
	batch.put_item(Item={"ranking": 6, "title": "Enforcer"})
	batch.put_item(Item={"ranking": 7, "title": "Hating game"})
	batch.put_item(Item={"ranking": 8, "title": "Alone together"})
	batch.put_item(Item={"ranking": 9, "title": "Death saved my life"})
	batch.put_item(Item={"ranking": 10, "title": "Fear of rain"})
	
print(batch)




#query your table using boto3
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Hulu_Top10Movies')
response = table.query(
	 KeyConditionExpression=Key('ranking').eq(7) #input key to query
)

print(response)


# remove items in the table
import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Hulu_Top10Movies')
#remove item
response = table.delete_item(Key ={'ranking': 7, 'title': 'Hating game'}) #Item key

print(response)


# scan items in the table

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Hulu_Top10Movies')

response = table.scan()

print("The scan returned the following items:")
for item in response['Items']:
    print(item)



# delete the table
import boto3
client = boto3.client('dynamodb')
try:
    resp = client.delete_table(
        TableName="Hulu_Top10Movies", # input table name
    )
    print("Your Table was successfully deleted!")
except Exception as e:
    print("Error, Please try again:")
    print(e)
    


