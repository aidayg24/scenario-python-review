import codecs
import csv
import urllib
from urllib import request

import psycopg2 as psycopg2

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

for item in iris_lst:
    lst2 = []
    it = iter(ExtendedList.next_val(item.the_list))
    while True:
        try:
            lst2.append(next(it))
        except StopIteration:
            break
    item.the_list = lst2
    print(item.the_list)

# connecting to database
conn = psycopg2.connect(host="localhost",
                        database="iris",
                        user="postgres",
                        password="134340aida",
                        port=5432
                        )

# insert_query = "INSERT INTO iris (sepal_l,sepal_w,petal_l,petal_w,class) " \
# "VALUES {},{},{},{},{}".format(one_row[0], one_row[1], one_row[2], one_row[3],
# target[iris_lst.index(line)])
# cursor = conn.cursor()
# cursor.execute(insert_query)