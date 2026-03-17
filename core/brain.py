class Brain:
    def __init__(self, api_key):
        self.api_key = api_key
    def process(self, command):
        return f"[Procesando comando]: {command}"
