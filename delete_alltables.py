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