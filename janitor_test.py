import boto3

s3 = boto3.client('s3')
print("Fetching your AWS S3 Buckets from GitHub Codespaces...")

try:
    response = s3.list_buckets()
    if response['Buckets']:
        print("\nSUCCESS! Found the following buckets:")
        for bucket in response['Buckets']:
            print(f" -> {bucket['Name']}")
    else:
        print("\nSUCCESS! Connected to AWS, but you don't have any S3 buckets yet.")
except Exception as e:
    print(f"\nSomething went wrong: {e}")
