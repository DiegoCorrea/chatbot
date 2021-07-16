from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response


class Config:
    botname = "Fofoqueiro da Esquina"
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter'
    database_uri = 'sqlite:///chatbot.sqlite3'
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": LevenshteinDistance,
            "response_selection_method": get_first_response
        }
    ]
    preprocessors = [
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii'
    ]
    corpus = "chatterbot.corpus.portuguese"
