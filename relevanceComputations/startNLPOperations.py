#Start the NLP Process

"""This file will have two functions:
- startNLP() which builds the corpus, models, etc
and
- startNLP_load() which loads prebuilt corpus models, etc
"""

def startNLP(modelType):
    #This builds the corpus and the model, etc. It is also possible to use these things prebuilt
    from gensim import corpora, models
    import logging
    from getDocSparseVector import getDocumentCorpus
    #Declare globals
    #global documents, corpus, documentDictionary, hdp
    
    #reload(getDocSparseVector)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #Use heirarchical dirichlet allocation topic modeling from gensim to compute the relevance between documents
    
    
    directory= "/Users/Larry/Code/EpistemicAssistant/sampleWordDocs/"
    #Imports a set of comparison documents and tokenizes them
    #Should not need to rebuild the corpus at each request...    
    documents = getDocumentCorpus(directory) #Get document objects
    texts =[]
    for doc in documents:
        texts.append(doc.tokenizedText)
    
    documentDictionary = corpora.Dictionary(texts)
    corpus = [documentDictionary.doc2bow(text) for text in texts]
                
    #Computes the HDA/nonparametric topic models
    if modelType == 'hdp':
        currentModel = models.HdpModel(corpus, id2word=documentDictionary)
    elif modelType == 'tfidf':
        #hdp = models.HdpModel(corpus, id2word=documentDictionary)
        currentModel = models.TfidfModel(corpus, id2word=documentDictionary)
    elif modelType == 'lda':
        currentModel = models.LdaModel(corpus, id2word=documentDictionary, num_topics=200)#Should try to fugure out a good number of topics
    else: print (currentModel+ ' not yet supported')

    
    return {'documents': documents, 'corpus': corpus, "documentDictionary": documentDictionary, "currentModel": currentModel}
    
def startNLP_load():
    import cPickle as pickle
    documentDictionary = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documentDictionary.p", "rb"))#load document dictionary
    corpus = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/corpus.p", "rb")) #load corpus
    hdp = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/hdp.p", "rb"))#load hdp model
    documents = pickle.load(open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documents.p", "rb"))#load documents
    return {'documents': documents, 'corpus': corpus, "documentDictionary": documentDictionary, "hdp": hdp}

    

