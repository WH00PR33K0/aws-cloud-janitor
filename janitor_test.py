import boto3

# Connect to the EC2 service instead of S3
ec2 = boto3.client('ec2', region_name='us-east-1') # Adjust region if needed

print("Starting Cloud Janitor Scan for Unused EBS Volumes...")

try:
    # Fetch details on all EBS storage volumes in this region
    response = ec2.describe_volumes()
    
    unused_volumes_count = 0
    
    print("\nScanning volume attachments...")
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        size = volume['Size']
        state = volume['State']
        
        # Check if the volume is unattached ('available' means it is not connected to any server)
        if state == 'available':
            print(f" -> [ALERT] Unused Volume Found! ID: {volume_id} | Size: {size}GB | State: {state}")
            unused_volumes_count += 1
            
            # NOTE FOR PRODUCTION: To actually delete them programmatically later, you would add:
            # ec2.delete_volume(VolumeId=volume_id)
            
    if unused_volumes_count == 0:
        print("\nSUCCESS! Clean scan. All storage volumes are actively attached to servers.")
    else:
        print(f"\nScan complete. Found {unused_volumes_count} orphaned storage volumes wasting money.")

except Exception as e:
    print(f"\nSomething went wrong during the scan: {e}")
