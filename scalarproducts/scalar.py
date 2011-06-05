### Imran Raja
### Scalar Problem (GCJ)
f = open("A-large-practice.in", "r")
case_count = int(f.readline())
case_count_iterator = 1

def line_to_array(vector):
  """Converts the line of text into an array"""
  modified_vector = vector.split(" ")
  modified_vector = [int(element) for element in modified_vector]
  modified_vector.sort()
  return modified_vector

while case_count_iterator < 1001:
  number_of_elements = int(f.readline())

  vector_one = f.readline()
  vector_one = line_to_array(vector_one)

  vector_two = f.readline()
  vector_two = line_to_array(vector_two)
  vector_two.reverse()

  print "Case #%s: %s" % (case_count_iterator, reduce(lambda x,y: x+y, [vector_one[i] * vector_two[i] for i in range(len(vector_one))]))
  case_count_iterator+=1

