from SmartParser import SmartParser

sp = SmartParser()
sp.SetText("Police used non-lethal means to subdue man they believe was coming off a methamphetamine high")
print(sp.NounChunks())