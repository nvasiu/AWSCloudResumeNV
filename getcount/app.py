import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table_name = "cloud-resume-nv"
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key={ 'ID': '1' })
    except Exception as e:
        print(e)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": json.dumps({
            "count": str(response["Item"]["visitcount"]),
        })
    }
