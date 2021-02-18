import os
from rest_framework.views import APIView
from rest_framework.response import Response
from ibm_watson import IAMTokenManager

# These generate IAM tokens which are temporary security credentials that are valid for 60 minutes.
# More information available at: https://cloud.ibm.com/docs/watson?topic=watson-iam

# speech-to-text token retrieval
# api: localhost:8000/tokens/speech-to-text
class SpeechToTextTokenProcess(APIView):
    def get(self, request, format=None):
        iam_token_manager = IAMTokenManager(apikey=os.environ['SPEECH_TO_TEXT_IAM_APIKEY'])
        token = iam_token_manager.get_token()
        return Response({'accessToken': token, 'url': os.environ['SPEECH_TO_TEXT_URL']})

# text-to-speech token retrieval
# api: localhost:8000/tokens/text-to-speech
class TextToSpeechTokenProcess(APIView):
    def get(self, request, format=None):
        iam_token_manager = IAMTokenManager(apikey=os.environ['TEXT_TO_SPEECH_IAM_APIKEY'])
        token = iam_token_manager.get_token()
        return Response({'accessToken': token, 'url': os.environ['TEXT_TO_SPEECH_URL']})

# assistant token retrieval
# api: localhost:8000/tokens/assistant
class AssistantTokenProcess(APIView):
    def get(self, request, format=None):
        iam_token_manager = IAMTokenManager(apikey=os.environ['ASSISTANT_IAM_APIKEY'])
        token = iam_token_manager.get_token()
        return Response({'accessToken': token, 'url': os.environ['ASSISTANT_URL']})
