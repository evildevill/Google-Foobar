from itertools import combinations

def solution(num_buns, num_required):
    # Initialize the list of keyrings for each bunny
    keyrings = [[] for num in range(num_buns)]
    
    # Calculate the number of copies of each key needed
    copies_per_key = num_buns - num_required + 1
    
    # Generate combinations of bunnies to assign keys
    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            # Assign the key to the bunny's keyring
            keyrings[bunny].append(key)
    
    return keyrings
