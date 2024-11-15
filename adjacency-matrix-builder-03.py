# constructs a list of pairs from the original data file
def get_pairs(data_file):

  pairs = set()
  global identifiers
  identifiers = set()
  with open(data_file) as pairs_list:

    # constructs a set of pairs of nodes from the data and a separate set of numeric identifiers from the data
    for line in pairs_list:

      # within the larger pairs set, adds a tuple for each pair
      current_pair = line[:-1]
      current_pair = current_pair.split(" ")
      for num in range(2):
        current_pair[num] = int(current_pair[num])

        # converts the identifier to zero-based indexing
        current_pair[num] -= 1

        # adds the node to the set of identifiers
        identifiers.add(current_pair[num])
      current_pair = tuple(current_pair)
      pairs.add(current_pair)
  
  # uses the set of identifiers to find and save the number of nodes in the network
  global num_nodes
  num_nodes = len(identifiers)
  
  # returns the list of pairs
  return (pairs)

# constructs an adjacency matrix for the pairs of nodes
def adjacency_matrix(pairs_set, new_file):

  with open(new_file, "w") as new_file:

    # constructs a template for each row vector without edges
    for number in identifiers:
      row_vector = []
      for i in range(num_nodes):
        row_vector.append(0)
      
      for tuple in pairs_set:
        if number in tuple:
          if tuple[0] == number:
            row_vector[tuple[1]] = 1
          else:
            row_vector[tuple[0]] = 1
      
      # writes the matrix to a text file
      # Credit: this line of code came from ChatGPT
      new_file.write(" ".join(map(str, row_vector)) + "\n")

sample_pairs = get_pairs("Social network simulations/random_pairs.txt")
adjacency_matrix(sample_pairs, "matrix.txt")