
import json
import urllib.parse
import boto3



print('Loading function')

s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    # print("event")
    # return(event)
    # print(event['queryStringParameters']['review'])

    
    text = event['review']
    # return {'a':'bbb'}
    # Get the object from the event and show its content type
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = comprehend.detect_sentiment(Text=text, LanguageCode='ja')
        # response['queryStringParameters'] = event['queryStringParameters']
        response['review'] = event['review']
        
        # print("CONTENT TYPE: " + response['ContentType'])
        print(response.keys())
        return response
    except Exception as e:
        print(e)
