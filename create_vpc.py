import boto3
#create vpc #
client=boto3.client("ec2")
client.create_vpc(CidrBlock= '10.0.0.0/16')
    
    
