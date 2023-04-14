import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId = "vpc-01c12f960c1fe1905"
)
print(response)
