class IsText():

    def __init__(self, allowed):
        self.allowed = allowed
    def __call__(self, message):
        if not message.text:
            return False
        return message.text.lower() in self.allowed



