import boto3
client=boto3.client("ec2")
response = client.describe_vpcs()
print(response)
numb_of_vpc = response["Vpcs"]
print(len(numb_of_vpc))

for vpc in numb_of_vpc:
    print(vpc["VpcId"])

response= client.describe_vpcs(
    VpcIds=["vpc-0cc8e9d1e908b9cb9"])
print(response)
