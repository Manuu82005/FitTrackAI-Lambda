import boto3
import uuid

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
polly = boto3.client('polly')
dynamodb = boto3.resource('dynamodb')

TABLE = 'FitTrackUsers'

def lambda_handler(event, context):

    tip = "Treadmill improves cardiovascular fitness."

    audio = polly.synthesize_speech(
        Text=tip,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    return {
        "statusCode": 200,
        "message": "Workout processed"
    }
