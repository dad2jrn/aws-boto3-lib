import boto3
from botocore.exceptions import ClientError

from detector import detector_id

REGIONS = ["us-east-1", "us-east-2", "us-west-1", "us-west-2"]


def main():
    """Main method to run the app"""
    # Loop through all the regions where Guard Duty is enabled
    for region in REGIONS:
        try:
            response = client.create_ip_set(
                DetectorId=detector_id(region),  # [REQUIRED] - This is the unique ID of the Detector
                Name="Trusted IPs",  # [REQUIRED] - The name of the IP set (ex. My Trusted IPs)
                Format="TXT",  # [REQUIRED] - 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE'
                Location="https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key",  # [REQUIRED] - HTTPS Path to bucket object
                Activate=True,  # [REQUIRED] - enable or disable the set (True|False)
                # [Optional but recommended]
                Tags={
                    "key1": "value1",
                    "key2": "value2",
                },
            )
            print(
                f"Successfully added IP set to Detector {detector} in region {region}."
            )
        except ClientError as error:
            print(
                f"Oh snap... Looks like something when wrong.  Here is the error I got: {error}"
            )
