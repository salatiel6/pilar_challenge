class WordsListError(Exception):
    def __init__(self) -> None:
        self.message = "Invalid words list. Make sure it is a list" \
                       " of strings, and that it doesn't has empty string"
