import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import sys

# Initializing arrays
infected = {}
infected_over_time_1 = []

# Initializes the graph with amount of infected as well as susceptible.
def initialize_network(start_infected, N, k):
    # Create a graph with N and K.
    network = nx.fast_gnp_random_graph(N, k / N)

    # Changes all to susceptible.
    for i in range(N):
        infected[i] = False

    # Takes a random sample of size start_infected and makes them infected.
    random_sample = random.sample(list(infected), start_infected)

    for sample in random_sample:
        infected[sample] = True

    return network


# Does one timestep.
def timestep(graph, amount_infected, infect_chance):
    # Checks if infected if true does action.
    for key, value in infected.items():
        if value:
            # Takes all neighbors of the node.
            neighbors = nx.all_neighbors(graph, key)
            for neighbor in neighbors:
                if not infected[neighbor]:
                    # do a random chance of infecting him and add one infected to counter.
                    if infect_chance > random.uniform(0, 1):
                        infected[neighbor] = True
                        amount_infected += 1
    return amount_infected


if __name__ == "__main__":  

    # Read parameters if they are all given.
    if len(sys.argv) == 8:
        N = int(sys.argv[1])  # Number of nodes.
        k = int(sys.argv[2])  # Connectivity.
        start_infected = amount_infected = int(sys.argv[3])  # Amount of innitially infected nodes.
        infect_chance = float(sys.argv[4])  # Chance that one node infects the other node.
        start_vaccined = int(sys.argv[5])
        vaccination_rate = int(sys.argv[6])  # Amount of persons vaccined per step.
        steps = int(sys.argv[7])  # Amount of steps that the simulation runs.
    # Use default parameters if none are given.
    elif len(sys.argv) == 1:
        print("Using default parameters.")
        N = 10**5
        k = 5
        start_infected = amount_infected = 10**4
        infect_chance = 0.01
        start_vaccined = 0
        vaccination_rate = 10
        steps = 100
    # Print error message if the amound of given parameters is incorrect.
    else:
        print("Correct way to call program with parameters:\n  python main.py <nodes> <connectivity> <initial_infected> <infection_chance> <initial_vaccined> <vaccination_rate> <steps>")
        sys.exit()

    G = initialize_network(start_infected, N, k)

    for step in range(steps):
        normalized_infected = amount_infected/N
        infected_over_time_1.append(normalized_infected)
        amount_infected = timestep(G, amount_infected, infect_chance)

    plt.plot(infected_over_time_1, label='Important info here')
    plt.xlabel('time (steps)')
    plt.ylabel('infected')
    plt.legend(loc='upper left')

    plt.show()
