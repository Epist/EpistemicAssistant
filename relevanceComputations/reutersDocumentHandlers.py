def importReutersDocuments(directory):
    directory = '/Users/Larry/Code/EpistemicAssistant/reuters'
    from nlpDoc import nlpDoc
    import os
    import fnmatch
    import re
    import codecs
    
        
    #Recursively crawls directory and gets all word documents
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, '*.sgm'):
            files.append(os.path.join(root, filename))
    
    #Opens the reuters documents, extracts the text, and builds nlpDocs 
    docs=[]
    for file in files:
        currentDocFile = open(file,'r')
        #currentDocFile = codecs.open(file,'r',"utf-8")
        currentFileText = extractDocumentText(currentDocFile)
        titles = re.findall('(?<=\<TITLE\>)(.*?)(?=\<\/TITLE\>)', currentFileText)
        bodies = re.findall('(?<=\<BODY\>)(.*?)(?=\<\/BODY\>)', currentFileText)
        for index, article in enumerate(bodies):
            currentDoc = nlpDoc(article)
            currentDoc.documentType = 'Reuters'
            currentDoc.fullFilename = file
            #currentDoc.filename = os.path.splitext(os.path.basename(file))[0]
            currentDoc.filename = titles[index]
            docs.append(currentDoc)
            
    #Extract plaintext from document

  
    return docs 
    
def extractDocumentText(doc):
    text = doc.read()
    doctext = text.replace('\n',' ')
    return doctext
    
    
    
    