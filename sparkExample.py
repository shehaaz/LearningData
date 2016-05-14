from pyspark import SparkContext


sc = SparkContext("local", "Simple App")
textFile = sc.textFile("README.md").cache()
numAs = textFile.filter(lambda s: 'a' in s).count()
numBs = textFile.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))