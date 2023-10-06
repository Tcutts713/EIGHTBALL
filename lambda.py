import random
import json

def lambda_handler(event, context):
    response = ["yes", "no", "outcome is cloudy", "ask again later"]

    
    question = event.get('body')
    if not question:
        return {
            'statusCode': 400,
            'body': json.dumps('No question provided')
        }

    random_answer = random.choice(response)

    response = {
        'statusCode': 200,
        'body': random_answer
    }

    return response
