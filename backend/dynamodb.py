import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

table = dynamodb.Table("robot_sensor_data_v2")