
class Symbol:
    def __init__(self):
        self.color = ""
        self.icon = ""


class Card(Symbol):
    def __init__(self):
        super().__init__()
        self.value = ""

