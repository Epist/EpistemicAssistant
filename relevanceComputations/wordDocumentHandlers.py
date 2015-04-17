def importWordDocuments(directory):
    from docx import Document
    import os.path
    import sys
    
    #This should be the sample list of word documents
    #directory = "/Users/Larry/Code/EpistemicAssistant/sampleWordDocs/" #forDebugging
    files = os.listdir(directory)
    
    docs = []
    for file in files:
        extension = os.path.splitext(directory+file)[1]
        if extension == '.docx':
            docs.append(Document(directory+file))
    
    #Extract plaintext from document
    docTexts=[]
    for doc in docs:
        docTexts.append(extractDocumentText(doc))
  
    return docTexts 
    
def extractDocumentText(doc):
    doctext = ''
    for para in doc.paragraphs:
        doctext = doctext+' '+para.text
    return doctext
        
    
    
    
    