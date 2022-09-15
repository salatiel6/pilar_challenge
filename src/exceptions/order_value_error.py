class OrderValueError(Exception):
    def __init__(self) -> None:
        self.message = "Invalid order value. It must be 'asc' or 'desc'"
