def importWordDocuments(directory):
    from nlpDoc import nlpDoc
    from docx import Document
    import os
    import fnmatch
    
    """This function finds all of the (.docx) word documents in a folder recursively
    and creates associated nlpDoc objects to return"""
        
    #Recursively crawls directory and gets all word documents
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.docx'):
            files.append(os.path.join(root, filename))
    
    #Opens the word documents, extracts the text, and builds nlpDocs 
    docs=[]
    for file in files:
        try:
            currentWordDoc = Document(file)
            currentDoc = nlpDoc(extractDocumentText(currentWordDoc))
            currentDoc.documentType = 'MS Word'
            currentDoc.fullFilename = file
            currentDoc.filename = os.path.splitext(os.path.basename(file))[0]
            docs.append(currentDoc)
        except:
            pass
            
    #Extract plaintext from document

  
    return docs 
    
def extractDocumentText(doc):
    doctext = ''
    for para in doc.paragraphs:
        doctext = doctext+' '+para.text
    return doctext
        
    
    
    
    