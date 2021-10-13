# modified by Mahmood Mortazavi Dehkordi
from __future__ import print_function
import boto3
import base64

client = boto3.client('sns')
topic_arn = '' # This will be replaced with the configuration management

def lambda_handler(event, context):
    try:
        client.publish(TopicArn=topic_arn, Message='anormal orders', Subject='orders alarm')
        print('delivered successfully')
    except Exception:
        print('failed delivery')