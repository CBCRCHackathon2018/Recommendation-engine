import spacy as sp

class SmartParser:

    nlpEngine = sp.blank
    currContext = None

    def __init__(self, language='en_core_web_lg'):
        self.nlpEngine = sp.load(language)
    
    def SetText(self, text):
        text.encode('utf-8')
        self.currContext = self.nlpEngine(text)

    def GetLabels(self):
        if self.currContext != None:
            return self.CreateOutputList(self.currContext.ents, 'label_')

    def NounChunks(self):
        if self.currContext != None:
            return self.CreateOutputList(self.currContext.noun_chunks, 'text')

    def CreateOutputList(self, inputObject, suffix):
        contextBuf = inputObject
        outputBuf = []
        for entity in contextBuf:
            outputBuf.append(getattr(entity, suffix))
        return outputBuf