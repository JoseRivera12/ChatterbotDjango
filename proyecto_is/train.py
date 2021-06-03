from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import LevenshteinDistance
from chatterbot import comparisons, response_selection
from chatterbot.conversation import Statement

chatbot = ChatBot(
    'ORWELL',
    trainer='chatterbot.trainers.ListTrainer',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter', 
    database_uri='mongodb://mongodb:27017/chatbot',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[ 
        #'chatterbot.logic.MathematicalEvaluation', #Este es un logic_adapter que responde preguntas sobre matemáticas en inglés
        #'chatterbot.logic.TimeLogicAdapter', #Este es un logic_adapter que responde preguntas sobre la hora actual en inglés
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": get_most_frequent_response,
        }
    ],
        preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train( './soporte.yml' )
levenshtein_distance = LevenshteinDistance()

disparate=Statement('Te has equivocado') #convertimos una frase en un tipo statement
entradaDelUsuario="" #variable que contendrá lo que haya escrito el usuario
