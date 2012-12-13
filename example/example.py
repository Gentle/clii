#!/usr/bin/python

import time

from clii.progress import Spinner, ProgressBar, TimedSpinner
from clii.completers import ListCompleter
from clii.wizard import Wizard

def spinner_test():
    s = Spinner(u'Spin!')
    s.start()
    for x in xrange(20):
        s.step()
        time.sleep(0.1)
    s.stop()

def progressbar_test():
    p = ProgressBar(u'Progress!')
    p.start()
    for x in xrange(100):
        p.step(1)
        time.sleep(0.1)
    p.stop()

def wizard_test():
    l = ['abc', 'bcd', 'cde', 'def']
    w = Wizard()
    s = w.ask('blub', ListCompleter(l), "abcde")
    print "s: %s"%s
    if w.yesno("Do you like cookies?"):
        print "yay"
    else:
        print "nay"
    c = w.choice("letter? (try one NOT in the list first)", ["a", "b", "c"])
    print "c=%s"%c
    
def timedspinner_test():
    s = TimedSpinner("spin!")
    s.start()
    time.sleep(2)
    s.stop()

if __name__ == '__main__':
    print "Spinner:"
    spinner_test()
    print "Progressbar:"
    progressbar_test()
    print "Fake spinner (timer spins):"
    timedspinner_test()
    print "some wizard examples (try tab completion):"
    wizard_test()
