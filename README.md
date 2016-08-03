# MostPopularSuperHeroAndDegreeofSeperation
Examined the Marvel Data-set to find out the most popular superhero in a densely connected Social graph. The idea of Social graph in this data-set is that the two super heroes are friends in this social graph if they co-exist in the same comic-book. The most popular super-hero is defined on the basis of this idea that with how many super-hero characters does it coexist in the comic books. Also programmed the concept of Breadth first Search in order to find out the degree of seperation between the source and the target super-heroes

#Pre-requisities
* Install Apache Spark
* Install Python
* Install pyCharm or any other IDE of your choice

#Procedure
```
$ Import collections
$ Import SparkContext and SparkConf
$ Create an RDD by calling sc.textFile
$ Perform operations on RDD to achieve the objective
$ while executing spark program write **spark-submit <filename.py>** on the command line
```

# Data-set description
* **Marvel-Graph.txt**:- This data-set consists of the super-heroes ids wherein the first id represnt the super-hero id and the rest of the line represents the super-heroes to whom it is friends with
* **Marvel-Names.txt**:- This data-set consist of the names of the super-heroes against their IDs

#Deployment
You can deploy it on Amazon's EMR
