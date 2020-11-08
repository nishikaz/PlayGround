class BagOfWords():
    def __init__(self, text=None, vocab=None, binary=False, lower=True):
        self.vocab = vocab
        self.text = text
        self.binary = binary
        self.lower = lower
        self.bow = {}

        if vocab != None:
            self.setVocab()

        if text != None:
            self.make()

    def setVocab(self):
        '''
        convert text/list to set
        '''
        if type(self.vocab) == str:
            if self.lower == True:
                texts = self.vocab.lower().split()
            else:
                texts = self.vocab.split()
        else:
            if self.lower == True:
                texts = [text.lower() for text in self.vocab]
        self.vocab = set(texts)

    def extendVocab(self, extend):
        '''
        extend self.vocab
        '''
        assert extend != None, 'Missing value.'
        if type(extend) == str:
            if self.lower == True:
                extend = set(extend.lower().split())
            else:
                extend = set(extend.split())
        else:
            if self.lower == True:
                extend = set([each.lower() for each in extend])
            else:
                extend = set([each for each in extend])
        self.vocab |= extend
        self.make()

    def make(self, text=None, vocab=None, binary=False, lower=True):
        '''
        make Bag of Words from text and save it in object.
        '''
        if text != None:
            self.text = text

        assert self.text != None, 'Input texts are required.'

        if self.vocab == None:
            self.vocab = self.text
            self.setVocab()

        if self.lower == True:
            text = self.text.lower()
        else:
            text = self.text

        self.bow = {word:0 for word in self.vocab}
        for word in self.vocab:
            self.bow[word] += text.count(word)

        if self.binary == True:
            self.bow = {word:1 if count > 0 else 0 for word, count in self.bow}