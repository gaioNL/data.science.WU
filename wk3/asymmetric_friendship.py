import MapReduce
import sys

"""
Gaio

Generate a list of all non-symmetric friend relationships.

Each input record is a 2 element list [personA, personB] , A is friend of B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    for i in range(len(record)):
        mr.emit_intermediate(record[i], record[1-i])

def reducer(key, list_of_friends):
    # key: person
    # value: list of friends
    for friend in list_of_friends:
        if list_of_values.count(friend) == 1:
            mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)