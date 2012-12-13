from clii.completers import ListCompleter

class TestListCompleter:

    def test_listcompleter_empty(self):
        l = []
        c = ListCompleter(l)
        assert c('a',0) == None
        assert c('a',1) == None

    def test_listcompleter_one(self):
        l = ['abc', 'bcd']
        c = ListCompleter(l)
        assert c('a',0) == 'abc'
        assert c('a',1) == None


    def test_listcompleter_two(self):
        l = ['abc', 'aee']
        c = ListCompleter(l)
        assert c('a',0) == 'abc'
        assert c('a',1) == 'aee'
        assert c('a',2) == None
