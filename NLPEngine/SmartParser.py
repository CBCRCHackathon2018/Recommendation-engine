from google.cloud import language as ln
from google.cloud.language import enums
from google.cloud.language import types

class SmartParser:

    client = None
    document = None

    def __init__(self):
        # Instantiates a client
        self.client = ln.LanguageServiceClient()
    
    def SetText(self, text, language='en'):
        text.encode('utf-32')
        self.document = ln.types.Document(content=text, language=language, type='PLAIN_TEXT')

    def NounChunks(self):
        temp = []
        if self.document != None:
            response = self.client.analyze_entities(document=self.document, encoding_type='UTF32')
            for entity in response.entities:
                temp.append(str(entity.name))
        return temp