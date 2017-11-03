import MapReduce
import sys

"""
Gaio:execute join query

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    # key: order id
    orderID    = list_of_values[0]
    lines = list_of_values[1:]

    for l in lines:
        mr.emit(orderID + l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)