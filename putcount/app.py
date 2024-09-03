import json
import boto3

dynamodb = boto3.resource('dynamodb')

table_name = "cloud-resume-nv"
table = dynamodb.Table(table_name)

def lambda_handler(event, context):

    try:
        response = table.update_item(
            Key={
                'ID': '1'
            },
            UpdateExpression="ADD visitcount :val",
            ExpressionAttributeValues={
                ':val' : 1
            },
            ReturnValues="UPDATED_NEW"
        )
    except Exception as e:
        print(e)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST"
        }
    }