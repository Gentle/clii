import itertools
import sys
import threading
import time

from util import getTerminalSize

class ProgressIndicator(object):
    def __init__(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def start(self):
        raise NotImplementedError
    
    def step(self):
        raise NotImplementedError
    
    def stop(self):
        raise NotImplementedError


class Spinner(ProgressIndicator):

    def __init__(self, message=u'', final=u'done'):
        self.message = message
        self.final = final
        self._iter = itertools.cycle(r'\|/-')
        super(Spinner, self).__init__()

    def start(self):
        self.stdout.write(u'%s %s ' % (self.message, self._iter.next()))
        self.stdout.flush()

    def step(self, count=1): # count is ignored here
        self.stdout.write(u'\b\b%s ' % self._iter.next())
        self.stdout.flush()

    def stop(self):
        self.stdout.write(u'\b\b%s\n' % self.final)
        self.stdout.flush()

class TimedSpinner(Spinner):
    def __init__(self, message=u'', final=u'done', interval=0.1):
        super(TimedSpinner, self).__init__(message, final)
        self.interval = interval

    def run(self):
        while self.running:
            self.step()
            time.sleep(self.interval)

    def start(self):
        super(TimedSpinner, self).start()
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()
        super(TimedSpinner, self).stop()

class ProgressBar(ProgressIndicator):
    def __init__(self, message=u'', total=100):
        self.message = message + u' '
        self.total = total
        self.count = 1
        super(ProgressBar, self).__init__()

    def _bar(self, clear=True):
        """
        draws a progressbar with percentage value
        clear has to be false on first run
        and true on consecutive runs
        """
        width = getTerminalSize()[0] - len(self.message) - 1
        if clear:
            self.stdout.write(u'\b' * width)
        done = float(self.count) * width / float(self.total)
        self.stdout.write(u'[')
        for i in xrange(width - 2 - 4): # 2="[]" 4="  1%"
            if i < done:
                self.stdout.write(u'#')
            else:
                self.stdout.write(u' ')
        self.stdout.write(u']')
        self.stdout.write(u'%3d%%' % (self.count * 100.0 / self.total))
        self.stdout.flush()

    def start(self):
        self.stdout.write(self.message)
        self._bar(False)
        self.stdout.flush()

    def step(self, count=1):
        self.count += count
        if self.count >= self.total:
            self.count = self.total
        self._bar()
        self.stdout.flush()
        
    def stop(self):
        self.stdout.write(u'\n')
        self.stdout.flush()

