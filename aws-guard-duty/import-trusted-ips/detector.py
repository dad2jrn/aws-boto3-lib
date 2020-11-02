import boto3
from botocore.exceptions import ClientError


def detector_id(region):
    """string

    Args:
        region (string): AWS Region name, example: 'us-east-1'

    Returns:
        string: Unique ID of the regional Guard Duty detector
    """
    client = boto3.client("guardduty", region_name=region)
    response = client.list_detectors()["DetectorIds"]
    return response.pop()
