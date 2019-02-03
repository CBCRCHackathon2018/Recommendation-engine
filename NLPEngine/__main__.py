from SmartParser import SmartParser

def ParseText(text):
    sp = SmartParser()
    sp.SetText(text)
    return sp.NounChunks()


print(ParseText("The 180 is a show that's meant to get Canadians talking about what's going on in our country."))