!pip install chatterbot
!pip install chatterbot-corpus
!python -m spacy download en_core_web_sm

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
from chatterbot.response_selection import get_first_response

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
chatbot = ChatBot("ERMIN",
                  tagger_language=ENGSM,
                  storage_adapters = 'chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter',
                      'chatterbot.logic.BestMatch',
                      {"import_path": "chatterbot.logic.BestMatch",
                       'default_response': 'I am sorry, but I do not understand. I am still learning.',
            "statement_comparison_function": 'chatterbot.comparisons.LevenshteinDistance',
            'response_selection_method': get_first_response
                          }
                      ],
                        database_uri = 'sqlite:///database.sqlite3')

training_data_simple = open('/content/training.txt').read().splitlines()
training_data_personal = open('/jarvis.txt').read().splitlines()

training_data = training_data_simple + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)

'name=input("Enter Your name:")
print('Welcome',name,'Let me know how can I help you?')
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
