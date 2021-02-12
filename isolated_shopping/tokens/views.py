import os
from rest_framework.views import APIView
from rest_framework.response import Response
from ibm_watson import IAMTokenManager

# speech-to-text token retrieval
# api: localhost:8000/tokens/speech-to-text
class SpeechToTextTokenProcess(APIView):
    def get(self, request, format=None):
        iam_token_manager = IAMTokenManager(apikey=os.environ['SPEECH_TO_TEXT_IAM_APIKEY'])
        token = iam_token_manager.get_token()
        return Response({'accessToken': token, 'url': os.environ['SPEECH_TO_TEXT_URL', test: 'test']})

# text-to-speech token retrieval
# api: localhost:8000/tokens/text-to-speech
class TextToSpeechTokenProcess(APIView):
    def get(self, request, format=None):
        iam_token_manager = IAMTokenManager(apikey=os.environ['TEXT_TO_SPEECH_IAM_APIKEY'])
        token = iam_token_manager.get_token()
        return Response({'accessToken': token, 'url': os.environ['TEXT_TO_SPEECH_URL']})
