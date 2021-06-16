class Symbol:
    def __init__(self):
        # COACHES' NOTES: You should have gotten the icon as parameter.
        # Moreover, self.color would have been inferred from the icon, with something
        # like `self.red_or_black()`
        self.color = ""
        self.icon = ""


class Card(Symbol):
    # COACHES' NOTES: The Card object right now does nothing.
    # It should have the value and the icon as parameter,
    # the latter being passed to the Symbol class.
    def __init__(self):
        super().__init__()
        self.value = ""
