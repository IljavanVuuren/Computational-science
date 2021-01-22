# Project Computational Science
# Numerical Method for model.

# Group 16
# Ilja van Vuuren
# Nick Moone
# Willem Breedveld

import matplotlib.pyplot as plt
import numpy as np

# Make lists to store data
infected_list = []
susceptible_list = []
recovered_list = []
time_list = []

# Initialize variables
N = 17400000
infected = 135607
recovered = 2000000
susceptible = N-(infected+recovered)

k = 1/15
b = 1.75
steps = 1

infected_average = infected/N
susceptible_average = susceptible/N
recovered_average = recovered/N

# Makes numerical approximation.
for t in np.arange(0, 25, steps):
    
    slope_infected = (b*susceptible_average*infected_average)-(k*infected_average)
    slope_susceptible = -b*susceptible_average*infected_average
    slope_recovered = k*infected_average

    infected_list.append(infected_average)
    susceptible_list.append(susceptible_average)
    recovered_list.append(recovered_average)
    time_list.append(t)

    infected_average = infected_average+(slope_infected*steps)
    susceptible_average = susceptible_average+(slope_susceptible*steps)
    recovered_average = recovered_average+(slope_recovered*steps)

# Plot the results.
plt.plot(time_list, infected_list, label='Infected')
plt.plot(time_list, susceptible_list, label='Susceptible')
plt.plot(time_list, recovered_list, label='Recovered')
plt.xlabel('time')
plt.ylabel('Fraction of population')
plt.legend()

plt.show()
