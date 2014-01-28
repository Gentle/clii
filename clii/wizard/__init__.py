import sys
import readline

from ..completers import ListCompleter

class Wizard(object):
    def __init__(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        readline.parse_and_bind("tab: complete") # this should be in some init_app function


    def ask(self, message, completer=None, default=""):
        """
        use this in wizards to query for values
        returns the default value on empty string,
        uses the completer hook for auto completion

        Note:
        readline.parse_and_bind("tab: complete")
        should be called elsewhere and preferably once only
        this should be in the cliapp class that doesn't exist yet
        """
        if default:
            message = "%s [%s]" % (message, default)
        readline.set_completer(completer)
        result = raw_input("%s " % message)
        readline.set_completer(None)
        if not result:
            return default
        return result

    def yesno(self, message, default=False):
        """
        use this in wizards to ask for boolean values
        """
        assert isinstance(default, bool)
        good = ['y', 'yes', 'j', 'ja']
        bad = ['n', 'no', 'nein']
        if default:
            y = 'Y'
            n = 'n'
        else:
            y = 'y'
            n = 'N'
        completer = ListCompleter(good + bad)
        while True:
            result = self.ask('%s [%s/%s]' % (message, y, n),
                              completer)
            if not result:
                return default
            if result.lower() in good:
                return True
            elif result.lower() in bad:
                return False
            self.say('please answer yes or no!')

    def choice(self, message, choices):
        """
        ask for an option out of a list
        the question gets repeated until a valid option has been chosen
        """
        completer = ListCompleter(choices)
        while True:
            result = self.ask(message, completer)
            if result in choices:
                readline.set_completer(None)
                return result
            self.say('"%s" is not a valid option, use tab completion for list' % result)

    def say(self, message):
       """
       use this in wizards to print additional information
       """ 
       self.stdout.write(message+"\n")

