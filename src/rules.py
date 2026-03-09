import numpy as np


# Deterministic Rules

def autocatalysis(neighborhood):
    """
    """
    # initialize new state
    new_states = []

    # iterate for each row 
    for state in neighborhood: 
        if neighborhood[state][1] > (neighborhood[state][2] & neighborhood[state][3]):
            new_states.append(0)
        elif neighborhood[state][2] > (neighborhood[state][1] & neighborhood[state][3]):
            new_states.append(1)
        else:
            new_states.append(2)

    #turn list into array
    new_states = np.array(new_states)
    
    return new_states
    
def mutual_inhibition(neighborhood):
    """
    """
    # initialize new state
    new_states = []

    # iterate for each row 
    for state in neighborhood: 

    new_states = np.array(new_states)
    return new_states

# Stochastic Rules

def spontaneus_neutrality(epsilon, p_neutral, neighborhood):
    """
    """
    new_states = np.array(new_states)
    return new_states

def spontaneous_chirality(epsilon, p_chiral, neighborhood):
    """
    """
    new_states = np.array(new_states)
    return new_states

def diffusion(epsilon, p_copy, neighborhood):
    """
    """
    new_states = np.array(new_states)
    return new_states
