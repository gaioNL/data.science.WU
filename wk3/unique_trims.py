mport MapReduce
import sys


"""

Gaio 

Consider a set of key-value pairs where each key is sequence id
and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Write a MapReduce query to remove the last 10 characters from
each string of nucleotides, then remove any duplicates generated.

"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: sequence id
    # value: nucleotides sequence
    key = record[0]
    value = record[1][:-10]
    mr.emit_intermediate(1, value)

def reducer(key, list_of_strings):
    # key: dummy
    # values: trimmed sequences
    uni_set = []
    for v in list_of_strings:
        if v not in uni_set:
            uni_set.append(v)
    for u in uni_set:
        mr.emit(u)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)