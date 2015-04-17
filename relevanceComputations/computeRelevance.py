
from gensim import corpora, models, similarities
import logging
from getDocSparseVector import getDocumentCorpus
#reload(getDocSparseVector)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#Use heirarchical dirichlet allocation topic modeling from gensim to compute the relevance between documents

#Need to import a document
#mainDocument = [(0, 1), (4, 1)];

directory= "/Users/Larry/Code/EpistemicAssistant/sampleWordDocs/"
#Need to import a set of comparison documents and parse them into words and n-grams
"""comparisonDocuments = [[(0, 1.0), (1, 1.0), (2, 1.0)],
    [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
    [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
    [(0, 1.0), (4, 2.0), (7, 1.0)],
    [(3, 1.0), (5, 1.0), (6, 1.0)],
    [(9, 1.0)],
    [(9, 1.0), (10, 1.0)],
    [(9, 1.0), (10, 1.0), (11, 1.0)],
    [(8, 1.0), (10, 1.0), (11, 1.0)]]"""
documents = getDocumentCorpus(directory) #Get document objects
texts =[]
for doc in documents:
    texts.append(doc.tokenizedText)
    #There has got to be a better way to do this...

documentDictionary = corpora.Dictionary(texts)
corpus = [documentDictionary.doc2bow(text) for text in texts]

mainDocument = documentDictionary.doc2bow(['coordination', 'communication', 'model', 'bayesian'])

#comparisonDocuments = getDocumentCorpus(directory)
    
#Need to transform each document into a sparse vector representation

#Need to compute the HDA/nonparametric topic models



#test
#hdp = hdpmodel.HdpModel(comparisonDocuments, id2word=dictionary) # step 1 -- initialize a model

tfidf = models.TfidfModel(corpus)

tfidfCorpus = tfidf[corpus]
mainDocumentTfidf = tfidf[mainDocument];


lsi = models.LsiModel(tfidfCorpus, id2word=documentDictionary, num_topics=5) # initialize an LSI transformation
corpus_lsi = lsi[tfidfCorpus] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

hdp = models.HdpModel(corpus, id2word=documentDictionary)

corpusHdp = hdp[corpus]
mainDocumentHdp = hdp[mainDocument]

similarityIndex = similarities.MatrixSimilarity(corpusHdp)
sims = similarityIndex[mainDocumentHdp]
sims = sorted(enumerate(sims), key=lambda item: -item[1])

topNum=6; #The number of documents to use as the top matches
topSims=sims[0:(topNum-1)]
topDocs = []
for sims in topSims:
    topDocs.append(documents[sims[0]])
    