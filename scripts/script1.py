from itertools import chain, combinations, product

# Function to generate all non-empty subsets of a list
def non_empty_subsets(lst):
    return chain(*map(lambda x: combinations(lst, x), range(1, len(lst) + 1)))

# Function to generate all combinations with more than one element from each list allowed
def generate_combinations(list_of_lists):
    all_subsets = [list(non_empty_subsets(lst)) for lst in list_of_lists]
    
    all_combinations = product(*all_subsets)
    
    combinations_list = [list(chain(*combination)) for combination in all_combinations]
    
    return combinations_list

list_of_lists = [["lord", "ord ", "rd o"], ["puti", "utin"], ["trum", "rump"]]
combinations = generate_combinations(list_of_lists)

for combination in combinations:
    print(combination)
