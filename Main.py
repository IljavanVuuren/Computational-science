import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import sys

# Initializing arrays
infected = {}
susceptible = {}
immune = {}  # Also define immune dict for least time complexity.
infected_over_time_1 = []
n_neighbors = []  # Amount of neighbours for every node.

# Initializes the graph with amount of infected as well as susceptible.
def initialize_network():
    # Create a graph with N and K.
    network = nx.fast_gnp_random_graph(N, k / N)

    # Changes all to susceptible.
    for i in range(N):
        susceptible[i] = True
        infected[i] = False
        immune[i] = False

    # Takes a random sample of size start_infected and makes them infected.
    random_sample = random.sample(list(susceptible), start_infected)
    for node in random_sample:
        susceptible[node] = False
        infected[node] = True

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
def timestep(graph):

    # Infect (move from susceptible to infected).
    for key, value in infected.items():
        if value:
            # Takes all neighbors of the node.
            neighbors = nx.all_neighbors(graph, key)
            for neighbor in neighbors:
                if susceptible[neighbor]:
                    # do a random chance of infecting him and add one infected to counter.
                    if infect_chance > random.uniform(0, 1):
                        susceptible[neighbor] = False
                        infected[neighbor] = True

                        global amount_infected
                        amount_infected += 1

            # Immune (move from infected to immune).
            infected[key] = False
            immune[key] = True

    # Vaccine (move from susceptible to immune).
    if vaccination_strategy == "random":
        # Takes a random sample of size vaccination_rate and makes them immune.
        random_sample = random.sample(list({k: v for k, v in susceptible.items() if v == True}), vaccination_rate)
        for node in random_sample:
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
    vaccination_strategy = "connections"

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
        N = 10**5
        k = 9
        start_infected = amount_infected = 10**3
        infect_chance = 0.1
        start_immune = 10**2
        vaccination_rate = 1
        steps = 100
    # Print error message if the amound of given parameters is incorrect.
    else:
        print("Correct way to call program with parameters:\n  python main.py <nodes> <connectivity> <initial_infected> <infection_chance> <initial_immune> <vaccinations_per_step> <steps>")
        exit()

    G = initialize_network()
    print("Initialization finished.")

    for step in range(steps):
        normalized_infected = amount_infected/N
        infected_over_time_1.append(normalized_infected)
        print("Step", step)
        timestep(G)
        print(amount_infected)

    plt.plot(infected_over_time_1, label='Important info here')
    plt.xlabel('time (steps)')
    plt.ylabel('infected')
    plt.legend(loc='lower right')

    plt.show()
