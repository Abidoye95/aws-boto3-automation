import boto3

s3 = boto3.client("s3")
response = s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME')
print(response)