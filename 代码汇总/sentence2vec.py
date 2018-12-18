#coding = utf-8
import numpy as np
import codecs
from gensim.models import word2vec
import sys

#定义文件名
wordfile = "cut.txt"
sentencevecfile = "sentenvec.txt"
plainfile = "vec.txt"

#构造词向量,存储本地模型
sentences = word2vec.Text8Corpus(wordfile)
model = word2vec.Word2Vec(sentences, size= 10, min_count = 1)
model.save("wordvec.model")

#初始化句向量列表
f1 = codecs.open(wordfile,"r",encoding = 'utf-8')
f2 = codecs.open(sentencevecfile,"w",encoding = 'utf-8')
f3 = codecs.open(plainfile,"w",encoding = 'utf-8')
sentencevec = np.zeros((6202,10))

#合成句向量
i = 0
lines = f1.readlines()
for line in lines :
	words = line.split()
	for word in words:
		if word != '$':
			if word != '':
				sentencevec[i] += model[word]
		if word == '$':
			i += 1

#输出文件--带注释
for i in range(6202):
	f2.write("job description %d :" %(i+1))
	f2.write("\n")
	f2.write(str(sentencevec[i]))
	f2.write("\n")
	f2.write("\n")

#输出文件--不带注释
for i in range(6202):
	f3.write(str(sentencevec[i]))
	f3.write("\n")

	
