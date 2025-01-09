# returns the identifier of a pair (the first node listed)
def pair_id(e):
  return(e[0])

# constructs a list of pairs from the original data file
def get_edges(data_file):

  global pairs
  global reverse_pairs
  pairs = []
  reverse_pairs = []
  with open(data_file) as pairs_list:

    # constructs a list of edges (pairs) from the data and a twin list of the reverse pairs
    for line in pairs_list.readlines()[2:]:

      # within the larger edges and reverse edges lists, adds a sub-list for each pair
      current_pair = line[:-1]
      current_pair = current_pair.split(" ")
      for num in range(2):
        current_pair[num] = int(current_pair[num])

        # converts the identifier to zero-based indexing
        current_pair[num] -= 1

      # creates the reverse of the current pair
      twin_pair = [current_pair[1], current_pair[0]]

      pairs.append(current_pair)
      reverse_pairs.append(twin_pair)

      reverse_pairs.sort(key=pair_id)

  # constructs a list of all the nodes in the network
  global identifiers
  identifiers = []

  for pair in pairs:
    identifiers.append(pair[0])

  for pair in reverse_pairs:
    identifiers.append(pair[0])

  # sorts and removes duplicates from the list of identifiers
  identifiers.sort()
  identifiers = set(identifiers)
  identifiers = list(identifiers)
  
  # uses the set of identifiers to find and save the number of nodes in the network
  global num_nodes
  num_nodes = len(identifiers)

  # constructs a dictionary with the node identifiers as keys and lists of their edges as values
  global edges_dict
  edges_dict = {}
  for identifier in identifiers:
    identifier_set = set()
    for edge in pairs[:]:
      if edge[0] == identifier:
        identifier_set.add(tuple(edge))
    edges_dict[f"node_{identifier}_edges"] = identifier_set
  # credit: the two loops above (the code from "for identifier ... = identifier_set") were revised by ChatGPT

  # adds the reversed pairs to the dictionary (these are duplicates of the edges already there, because the adjacency matrix is symmetrical)
  for identifier in identifiers:
    for edge in reverse_pairs[:]:
      if edge[0] == identifier:
        edges_dict[f"node_{identifier}_edges"].add(tuple(edge))

# constructs an adjacency matrix for the pairs of nodes
def adjacency_matrix(new_file):
  
  # constructs each row of the matrix as list and writes it to the text file
  with open(new_file, "w") as new_file:
    for identifier in identifiers:
      row_vector = []
      for num in range(num_nodes):
        if (identifier, num) in edges_dict[f"node_{identifier}_edges"]:
          row_vector.append(1)
        else:
          row_vector.append(0)
      
      # writes the matrix to a text file
      new_file.write(" ".join(map(str, row_vector)) + "\n")
      # Credit: this line of code came from ChatGPT.

get_edges("test.txt")
adjacency_matrix("matrix.txt")
print ("test")