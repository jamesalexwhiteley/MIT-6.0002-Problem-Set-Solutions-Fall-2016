###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
from collections import OrderedDict

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_data = open(filename,'r')
    data = cow_data.read()
    cows_list = data.split()

    cows_dict = {}

    for i in range(len(cows_list)):
        cow_list = cows_list[i].split(',')
        cows_dict[cow_list[0]] = cow_list[1]

    return(cows_dict)


def greedy_cow_transport(cows, limit=10):
    """
    Use a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    cows_sorted = OrderedDict(sorted(cows.items(), reverse=True, key=lambda x: x[1])) 

    while len(cows_sorted) > 0:
        trip = []
        taken = []
        trip_weight = 0
        for (cow, weight) in cows_sorted.copy().items():
            if trip_weight + float(weight) <= limit:
                trip_weight += float(weight)
                trip.append(cow)
                del cows_sorted[cow]

        trips.append(trip)

    return trips 

print(greedy_cow_transport(load_cows('ps1_cow_data.txt'),limit=10))

# Problem 3
def brute_force_cow_transport(cows_dict,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted_list = sorted(cows_dict.items(), key=lambda x: x[1], reverse = True)

    trips = []
    for partition in get_partitions(cows_sorted_list):
        trip = []
        for cow_list in partition: 
            limit = 10
            for cow_tuple in cow_list:
                limit -= int(cows_dict[cow_tuple[0]])
            if limit > 0:
                trip.append(cow_list)
            else:
                break 
        res = []
        if partition == trip:
            for item in partition:
                li = []
                for c in item:
                    li.append(c[0])
                res.append(li)
            return res

print(brute_force_cow_transport(load_cows('ps1_cow_data.txt'),limit=10))

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    print(greedy_cow_transport(load_cows('ps1_cow_data.txt'),limit=10))
    end = time.time()
    print((end - start))

    start = time.time()
    print(brute_force_cow_transport(load_cows('ps1_cow_data.txt'),limit=10))
    end = time.time()
    print((end - start))

# compare_cow_transport_algorithms()
