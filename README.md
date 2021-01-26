# Project Computational Science
# Implementation for model of a network on which a virus spreads
# while vaccination is applied.

#Group 16
#Ilja van Vuuren
#Nick Moone
#Willem Breedveld

There are two files with python code: the network model and the numerical method. 

The network model will create a networkx model which is then used to simulate a virus spreading through the community and the effects of a vaccine on this spread.

The numerical method is used to confirm the accuracy of the results.

To gain the network test results similar to the ones from the report these parameters were used:

N = 17471000
k = 5
start_infected = amount_infected = 135607
infect_chance = 0.35
start_immune = amount_immune = 2000000
vaccination_rate = 141000
vaccination_strategy = "random"
steps = 25

When run the network model will automatically use these parameters but they can also be manually inserted through command line arguments as can be seen in the code.

To gain the numerical method results similar to the ones from the report these parameters were used:

N = 17400000
infected = 135607
recovered = 2000000
susceptible = N-(infected+recovered)
vaccinated = 141000/N

k = 1/15
b = 1.75

infected_average = infected/N
susceptible_average = susceptible/N
recovered_average = recovered/N

steps = 26

When the numerical method is run it will use these parameters automatically.
