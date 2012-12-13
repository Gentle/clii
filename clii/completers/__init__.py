class Completer(object):
    def __call__(self, text, state):
        raise NotImplementedError

class ListCompleter(Completer):
    def __init__(self, items):
        """
        basic Completer for list of strings
        items must be a list and each element must provide .startswith
        """
        self.items = items

    def __call__(self, text, state):
        options = [i for i in self.items if str(i).startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

