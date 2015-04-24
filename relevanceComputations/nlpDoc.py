class nlpDoc:
    
    rawText = ''
    tokenizedText = []
    filename = ''
    fullFilename = ''
    documentType = ''
    
    def __init__(self, rawText):
        self.rawText = rawText