"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

import mutagen
from mutagen.mp3 import MP3

import moviepy
from moviepy.editor import VideoFileClip, AudioFileClip

import random

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = none
polly = session.client("polly")

def tts(text):

    title = text.split()

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                            VoiceId="Matthew", Engine = 'neural')
        with open('audio.mp3', 'wb') as file: #saves speech to mp3 file
            file.write(response['AudioStream'].read())

    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

def background(aud, vids):
    audio = MP3(f"{aud}.mp3")
    aud_length = audio.info.length

    video = (VideoFileClip(f"assets/{vids}.mp4")
                .without_audio()
                .resize(height=1920)
                .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)
            )
    vid_length = video.duration

    start_time = random.uniform(0, vid_length-aud_length)

    audio = AudioFileClip(f"{aud}.mp3")

    cropped_vid = video.subclip(start_time, start_time + aud_length).set_audio(audio)
    

    cropped_vid.write_videofile('new.mp4')

def main():
    text = "We were 17 and 18. I considered a break up when I realized that he had an ugly habit of threatening to hurt/harm himself if I potentially did something he didn't like, and that it would 'obviously' (lol) be my fault. But this quote of his is what made me turbo-emergency-exit instead of break up amicably: \"When you and I have a family with kids, and I ever get the feeling you might be cheating on me, I'll shoot the kids first - in front of you, so you will witness that - then I'll shoot you, and then myself.\"This was said within a lighthearted \"what might our future together look like, way down the line?\" type of conversation. Edited 1: I appreciate the interest, but I am also a bit sad (though not surprised) to read that others have had encounters with the same type. Would you guys like to read what happened after, how it ended exactly? Obviously I'll need to be vague on the details. Where would posting make the most sense?"
    tts(text)
    background('audio', 'minecraft')
if __name__ == '__main__':
     main()
     
