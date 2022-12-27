"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(aws_access_key_id='AKIAWLIJRFR3TRJ7U3PI', aws_secret_access_key='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', region_name='us-east-1')
polly = session.client("polly")

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text="Hello world!", OutputFormat="mp3",
                                        VoiceId="Matthew")
    with open('speech.mp3', 'wb') as file: #saves speech to mp3 file
        file.write(response['AudioStream'].read())

except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)