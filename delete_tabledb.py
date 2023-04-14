import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('Hulu_Top10Movies')
#Delete item
response = table.delete_item(Key ={'ranking': 7, 'title': 'Hating game'}) #Item key

print(response)