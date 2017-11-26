import boto3,botocore
from base_config import ACCESS_KEY,ACCESS_SECRET

s3 = boto3.client("s3",aws_access_key_id = ACCESS_KEY,aws_secret_access_key=ACCESS_SECRET)
