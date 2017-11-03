import MapReduce
import sys

"""
Gaio

Problem 6
Assume you have two matrices A and B in a sparse matrix format,
where each record is of the form i, j, value. Design a MapReduce
algorithm to compute the matrix multiplication A x B

"""

# A and B are both 5 by 5 matrices

mr = MapReduce.MapReduce()

def mapper(record):
    # key: matrix id
    # values: (row, column, value)
    key = record[0]
    if key == "a":
        for i in range(5):
            mr.emit_intermediate((record[1],i),(record[2],record[3]))
    if key == "b":
        for i in range(5):
            mr.emit_intermediate((i,record[2]),(record[1],record[3]))

def reducer(key, list_of_values):
    # key: 
    # values: to be summed
    s = 0
    dict1 = {}
    dict2 = {}
    for v in list_of_values:
        if v[0] in dict1:
            dict2[v[0]] = v[1]
        else:
            dict1[v[0]] = v[1]
    for k in dict2.keys():
        s = s + dict2[k] * dict1[k]
    mr.emit((key[0],key[1],s))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)