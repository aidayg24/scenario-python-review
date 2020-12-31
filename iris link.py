import codecs
import csv
import urllib
from urllib import request

from scenario import ExtendedList


url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
stream = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))
# Return a reader object which will iterate over lines in the given csv file.

iris_lst = []
for row in csv_file:
    iris = ExtendedList(row)
    iris_lst.append(iris)

# print(iris_lst[1:])
for i in iris_lst:
    next_val(i)