import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import sys

# Initializing dicts that keep track of node states.
susceptible = {}
infected = {}
immune = {}

n_neighbors = []  # Amount of neighbours for every node (for vaccine strategy).

# Lists for storing and plotting data.
infected_over_time_1 = []

# Initializes the graph.
def initialize_network():
    # Create a graph with of size N and cardinality k.
    network = nx.fast_gnp_random_graph(N, k / N)

    # Make all nodes susceptible.
    for i in range(N):
        susceptible[i] = True
        infected[i] = False
        immune[i] = False

    # Takes a random sample of size start_infected and makes them infected.
    random_susceptibles = random.sample([node for node, sscptbl in susceptible.items() if sscptbl], start_infected)
    for node in random_susceptibles:
        susceptible[node] = False
        infected[node] = True

    # Takes a random sample of size start_immune and makes them immune.
    random_susceptibles = random.sample([node for node, sscptbl in susceptible.items() if sscptbl], start_immune)
    for node in random_susceptibles:
        susceptible[node] = False
        immune[node] = True

    # Add to data list.
    infected_over_time_1.append(amount_infected/N)

    if vaccination_strategy == "connections":
        def sort_n_neighbors(e):
            node, n = e
            return n

        # Calculate amount of neighbours for every node and sort.
        for i in range(N):
            n_neighbors.append((i, len(list(nx.all_neighbors(network, i)))))
        n_neighbors.sort(key=sort_n_neighbors)

    return network


# Does one timestep (15 days).
def timestep():
    global graph
    global amount_infected

    # Infect (move from susceptible to infected).
    for node, infctd in infected.items():
        if infctd:
            # Takes all neighbors of the node.
            neighbors = nx.all_neighbors(graph, node)
            for neighbor in neighbors:
                if susceptible[neighbor]:
                    # do a random chance of infecting him and add one infected to counter.
                    if infect_chance > random.uniform(0, 1):
                        susceptible[neighbor] = False
                        infected[neighbor] = True

                        amount_infected += 1

            # Immune (move from infected to immune).
            infected[node] = False
            immune[node] = True

    # Vaccine (move from susceptible to immune).
    if vaccination_strategy == "random":
        # Takes a random sample of size vaccination_rate and makes them immune.
        random_susceptibles = random.sample([node for node, sscptbl in susceptible.items() if sscptbl], vaccination_rate)
        for node in random_susceptibles:
            susceptible[node] = False
            immune[node] = True
    elif vaccination_strategy == "connections":
        # Keep track of how many nodes are vaccined this step.
        vaccined_step = 0
        while vaccined_step < vaccination_rate:
            node, _ = n_neighbors.pop()
            if susceptible[node]:
                susceptible[node] = False
                immune[node] = True
                vaccined_step += 1


if __name__ == "__main__":
    vaccination_strategy = "random"

    # Read parameters if they are all given.
    if len(sys.argv) == 8:
        N = int(sys.argv[1])  # Number of nodes.
        k = int(sys.argv[2])  # Connectivity.
        start_infected = amount_infected = int(sys.argv[3])  # Amount of innitially infected nodes.
        infect_chance = float(sys.argv[4])  # Chance that one node infects the other node.
        start_immune = int(sys.argv[5])  # Amount of persons immune when the simulation starts.
        vaccination_rate = int(sys.argv[6])  # Amount of persons vaccined per step.
        steps = int(sys.argv[7])  # Amount of steps that the simulation runs.
    # Use default parameters if none are given.
    elif len(sys.argv) == 1:
        print("Using default parameters.")
        N = 100000
        k = 5
        start_infected = amount_infected = 1
        infect_chance = 0.5
        start_immune = 10**2
        vaccination_rate = 10
        steps = 10
    # Print error message if the amound of given parameters is incorrect.
    else:
        print("Correct way to call program with parameters:\n  python main.py <nodes> <connectivity> <initial_infected> <infection_chance> <initial_immune> <vaccinations_per_step> <steps>")
        exit()

    graph = initialize_network()
    print("Initialization finished.")

    for step in range(steps):
        timestep()
        infected_over_time_1.append(amount_infected/N)
    

    plt.plot(infected_over_time_1, label='Important info here')
    plt.xlabel('time (steps x 15 days)')
    plt.ylabel('infected')
    plt.legend(loc='lower right')

    plt.show()
