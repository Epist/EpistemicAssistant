#Build corpus
def buildCorpus():
    from gensim import corpora, models, similarities
    import logging
    from getDocSparseVector import getDocumentCorpus, cleanAndTokenize
    import cPickle as pickle

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
    if 'hdp' in locals():
        print 'HDP already built. Using existing model'
    else:
        hdp = models.HdpModel(corpus, id2word=documentDictionary)
    
    
    pickle.dump(corpus, open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/corpus.p", "wb"))#Save corpus 
    
    pickle.dump(documentDictionary, open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documentDictionary.p", "wb"))#Save documentDictionary
    
    pickle.dump(hdp, open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/hdp.p", "wb"))#Save Hdp
    
    pickle.dump(documents, open("/Users/Larry/Code/EpistemicAssistant/relevanceComputations/documents.p", "wb"))#Save documents