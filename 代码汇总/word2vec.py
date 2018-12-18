#encoding=utf-8
from gensim.models import word2vec
import sys
sentences=word2vec.Text8Corpus(u'cut.txt')
model=word2vec.Word2Vec(sentences, size=10)
model.save('gaga.model')