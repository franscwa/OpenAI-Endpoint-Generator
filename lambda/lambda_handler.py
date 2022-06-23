
def lambda_handler(event, context):
    # TODO implement
    import boto3
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('api-gen-feedback')
    
    response = table.put_item(
       Item={
            'prompt': event['prompt'],
            'temperature': event['temperature'],
            'top_p': event['top_p'],
            'successful': event['successful']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }