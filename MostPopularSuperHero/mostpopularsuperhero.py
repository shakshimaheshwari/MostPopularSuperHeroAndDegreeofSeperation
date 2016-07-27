from pyspark import SparkConf, SparkContext
import collections

def parseLine(text):
    fields = text.split()
    superheroId = int(fields[0])
    return (superheroId, len(fields)-1)


def parseNames(text):
    fields = text.split('\"')
    return (int(fields[0]), fields[1].encode("utf-8"))

conf = SparkConf().setMaster("local").setAppName("SuperHero")
sc = SparkContext(conf = conf)

input = sc.textFile("C:/Sakshi/SparkCourse/MostPopularSuperHero/Marvel-Graph.txt")
superHeroIds = input.map(parseLine)

names = sc.textFile("C:/Sakshi/SparkCourse/MostPopularSuperHero/Marvel-Names.txt")
namesRdd = names.map(parseNames)

totalCount = superHeroIds.reduceByKey(lambda x,y : x+y)
flippedCount = totalCount.map(lambda (x,y) : (y,x))
mostPouplar= flippedCount.max()

mostPopularName = namesRdd.lookup(mostPouplar[1])[0]
print mostPopularName + " is most popular superhero , with" + \
    str(mostPouplar[0]) + " co-apperances"
