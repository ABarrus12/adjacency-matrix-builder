# constructs a list of pairs from the original data file
def get_pairs(data_file):

  pairs = []
  identifiers = set()
  pairs_list = open(data_file)

  # constructs a list of pairs of nodes from the data and a separate set of numeric identifiers from the data
  for line in pairs_list:
    # within the larger pairs list, adds a separate list for each pair
    current_pair = line[:-1]
    current_pair = current_pair.split(" ")
    for num in range(2):
      current_pair[num] = int(current_pair[num])
      # adds the node to the set of identifiers
      identifiers.add(current_pair[num])
    pairs.append(current_pair)
  
  # uses the set of identifiers to find and save the number of nodes in the network
  global num_nodes
  num_nodes = len(identifiers)
  
  # returns the list of pairs
  return (pairs)

# constructs an adjacency matrix for the pairs of nodes
def adjacency_matrix(pairs_matrix, new_file):

  # constructs a template for the adjacency matrix without edges
  matrix = []
  for a in range(num_nodes):
    matrix.append([])

    for b in range(num_nodes):
      matrix[a].append(0)

  # adds edges
  for num in range(len(pairs_matrix)):
    # saves the index in the  matrix list (i.e., the row in the adjacency matrix) that corresponds to each node in a pair
    a = pairs_matrix[num][0] - 1
    b = pairs_matrix[num][1] - 1

    # adds the edge for that pair
    matrix[a][b] = 1
    matrix[b][a] = 1

    if num % 10000 == 0:
      print (num)

  # writes the matrix to a text file
  new_file = open(new_file, "w")

  for a in range(len(matrix)):
    for b in range(len(matrix)):
      # if the entry is the last column of a row in the matrix, create a new line
      if b == len(matrix[a]) - 1:
        new_file.write(str(matrix[a][b]) + "\n")
      # otherwise, separate entries by a space
      else:
        new_file.write(str(matrix[a][b]) + " ")
      
  new_file.close()

sample_pairs = get_pairs("Social network simulations/random-pairs.txt")
adjacency_matrix(sample_pairs, "matrix.txt")
