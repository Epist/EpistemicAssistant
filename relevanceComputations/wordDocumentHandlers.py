def importWordDocuments(directory):
    from nlpDoc import nlpDoc
    from docx import Document
    import os.path
    import sys
    
    #This should be the sample list of word documents
    #directory = "/Users/Larry/Code/EpistemicAssistant/sampleWordDocs/" #forDebugging
    files = os.listdir(directory)
    
    docs=[]
    for file in files:
        extension = os.path.splitext(directory+file)[1]
        if extension == '.docx':
            currentWordDoc = Document(directory+file)
            currentDoc = nlpDoc(extractDocumentText(currentWordDoc))
            currentDoc.documentType = 'Word'
            currentDoc.filename = directory+file
            docs.append(currentDoc)
            
    #Extract plaintext from document

  
    return docs 
    
def extractDocumentText(doc):
    doctext = ''
    for para in doc.paragraphs:
        doctext = doctext+' '+para.text
    return doctext
        
    
    
    
    