class optional:
    def __init__(self, data):
        self.data = data if isinstance(data, dict) else {}

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            return None

    def __getattr__(self, name):
        return self.get(name)
