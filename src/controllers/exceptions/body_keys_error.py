class BodyKeysError(Exception):
    def __init__(self, key) -> None:
        self.message = f"Missing param: '{key}'"
