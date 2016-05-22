#Learning Data

##MapReduce

It is a programming model to perform parallel processing on large data sets.

A basic MapReduce algorithm consists of the following steps

1. Map: Transform each item into `key-value` pairs
2. Collect all the pairs with identical `keys`
3. Reduce the collected pairs to produce a collection of `values` for the corresponding single `key`

##Spark with Python and Flask

* $Python -V

	`Python 2.7.10`

* Install Flask

	`pip install Flask`

* Install py4j to dynamically access Java objects in a Java Virtual Machine

	`pip install py4j`


* [Download and install SPARK](http://spark.apache.org/downloads.html)

* [Do the Quick Start](http://spark.apache.org/docs/latest/quick-start.html)

* How to run Python Spark Shell
	`$SPARK_HOME/bin/pyspark`

* [Fire up Pycharm and choose the correct Python version](http://stackoverflow.com/a/37231130/1352672)

* Add SPARK_HOME and PYHTONPATH vars to PyCharm
`Run -> Edit Configurations... -> 'Environment variables' browse button [...]`
![Imgur](http://i.imgur.com/CXBCcJp.png)


* [In PyCharm add Spark Python to PYTHONPATH]
(http://stackoverflow.com/a/34992894/1352672)



