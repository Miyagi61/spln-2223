from gensim.models import Word2Vec

# define training data

sentences = [['this','is','the','first','sentence','for','word2vec'],
             ['this','is','the','second','sentence'],
             ['yet','another','sentence'],
             ['one','more','sentence'],
             ['and','the','final','sentence']]


model = Word2Vec(sentences,vector_size=100,window=5,min_count=1,sg=1,epochs=5,workers=3)
model.save('models/word2vec.model')


print(model.wv['sentence'])

