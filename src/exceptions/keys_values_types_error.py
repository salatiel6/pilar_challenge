class KeysValuesTypesError(Exception):
    def __init__(self, key) -> None:
        self.message = f"Invalid type of the key: {key}"
