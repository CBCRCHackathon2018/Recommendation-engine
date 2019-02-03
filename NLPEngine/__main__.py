from SmartParser import SmartParser

def ParseText(text):
    sp = SmartParser(text)
    return sp.NounChunks()
    