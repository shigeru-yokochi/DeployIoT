import json
import boto3

print('Loading function')  
iot = boto3.client('iot-data')

def lambda_handler(event, context):
    if event['body']['ref'] != "refs/heads/master":
        return "Not master."
        
    topic = 'sdkTest/sub'
    payload = {
        "message": "Lambda test"
    }
    try:
        iot.publish(
            topic=topic,
            qos=0,
            payload=json.dumps(payload, ensure_ascii=False)
        )
 
        return "Succeeeded."
    
    except Exception as e:
        print(e)
        return "Failed."
        