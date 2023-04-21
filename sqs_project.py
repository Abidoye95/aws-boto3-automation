import boto3

sqs = boto3.resource('sqs', region_name = 'us-east-1')


queue = sqs.create_queue(
  QueueName='W15Project_SQS', 
  Attributes={'DelaySeconds': '5', 'VisibilityTimeout': '60'})

print(queue.url)