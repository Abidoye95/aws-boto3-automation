import boto3
client = boto3.client('ec2')

instance = client.run_instances(
        ImageId='ami-069aabeee6f53e7bf',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
)

print(instance)
