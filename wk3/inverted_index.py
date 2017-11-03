import MapReduce
import sys

"""
Gaio Assignment1: inverted index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      #for each word, emit the couple (word, document ID)
      mr.emit_intermediate(w, key) 


def reducer(key, list_of_values):
    # key: word
    # value: documents in which the word appear
    list_of_values = list(set(list_of_values))
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
