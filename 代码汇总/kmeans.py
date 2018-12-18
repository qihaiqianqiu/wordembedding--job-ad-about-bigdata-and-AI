# coding=utf-8
import codecs
from numpy import *
from sklearn.metrics.pairwise import cosine_similarity
# 加载数据
fileName = 'vecnum.txt'
outcome = 'clusteroutcome.txt'
def loadDataSet(fileName):  # 解析文件，得到一个浮点数字类型的矩阵
    dataMat = []              # 文件的最后一个字段是类别标签
    f = open(fileName)
    for line in f.readlines():
        curLine = line.strip().split()
        fltLine = map(float, curLine)    # 将每个元素转成float类型
        dataMat.append(fltLine)
    return dataMat

#def distEclud(vecA, vecB):
#    return sqrt(sum(power(vecA - vecB, 2))) # 求两个向量之间的距离

#计算余弦相似度
def Cosine(vec1, vec2):
    npvec1, npvec2 = array(vec1), array(vec2)
    return npvec1.dot(transpose(npvec2))/(math.sqrt((npvec1**2).sum()) * math.sqrt((npvec2**2).sum()))
    #点乘需转置

# 构建聚簇中心，取k个随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))   # 每个质心有n个坐标值，总共要k个质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

# k-means 聚类算法
def kMeans(dataSet, k, distMeans = Cosine, createCent = randCent):
    #计数器
    f = codecs.open(outcome, "w", encoding = 'utf-8')
    h = 0
    stastic = []
    for i in range(k):
        stastic.append(h)
    m = shape(dataSet)[0]   # m = 6201
    clusterAssment = mat(zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
    # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k)
    clusterChanged = True   # 用来判断聚类是否已经收敛
    time = 0
    set_printoptions(threshold=nan)
    while clusterChanged:
        for i in range(k):
                stastic[i] = 0
        clusterChanged = False;
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            minDist = inf; minIndex = -1;
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            if clusterAssment[i,0] != minIndex : clusterChanged = True;  # 如果分配发生变化，则需要继续迭代
            clusterAssment[i,:] = minIndex,minDist   # 并将第i个数据点的分配情况存入字典
            stastic[minIndex] += 1
        for cent in range(k):   # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去第一列等于cent的所有列
            centroids[cent,:] = mean(ptsInClust, axis = 0)  # 算出这些数据的中心点
        time += 1
        if (time == 25):
            f.write(str(centroids))
            f.write("\n")
            f.write("\n")
            f.write(str(stastic))
            f.write("\n")
            f.write("\n")
            f.write(str(clusterAssment[:,0]))
            f.write("\n")
        if(time == 26):
            break
        #print(clusterAssment)
    return centroids, clusterAssment
# --------------------测试----------------------------------------------------
# 用测试数据及测试kmeans算法
datMat = mat(loadDataSet(fileName))
stableCentroids,clustAssing = kMeans(datMat,20)
"""
file = open(outcome,"aw")
file.write(stableCentroids)
file.write("\n")
file.write(clustAssing)
"""