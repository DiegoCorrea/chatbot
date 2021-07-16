import json

from chatterbot.trainers import ChatterBotCorpusTrainer
from django.http import JsonResponse
from chatterbot import ChatBot
from rest_framework.views import APIView

from apps.bot.Config import Config


def training():
    chatbot = ChatBot(name=Config.botname, storage_adapter=Config.storage_adapter, database_uri=Config.database_uri,
                      logic_adapters=Config.logic_adapters, preprocessors=Config.preprocessors, read_only=True)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.portuguese')
    return chatbot


class ChatterBotApiView(APIView):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = training()

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        body_unicode = request.body
        body = json.loads(body_unicode)

        if 'text' not in body:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(body['text'])

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name,
        })
