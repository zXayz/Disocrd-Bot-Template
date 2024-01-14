
class SampleError(Exception):
    """Throw an custom exception"""
    def __init__(self, status_code: int | None = 400, text: str | None = None) -> None:
        self.status_code: int = status_code
        self.text: str = text
        super().__init__(f"Status Code: {status_code} | {text}")
        