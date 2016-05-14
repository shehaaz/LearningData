from flask import Flask
from pyspark import SparkContext

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
    return "Lines with a: %i, lines with b: %i" % (numAs, numBs)


if __name__ == '__main__':
    sc = SparkContext("local", "Simple App")
    textFile = sc.textFile("/Users/Shehaaz/PycharmProjects/learningSparkWithFlask/README.md").cache()
    numAs = textFile.filter(lambda s: 'a' in s).count()
    numBs = textFile.filter(lambda s: 'b' in s).count()
    print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
    app.run()