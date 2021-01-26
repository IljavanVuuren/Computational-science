# Project Computational Science
# Numerical method for model of a network on which a virus spreads
# while vaccination is applied on 25 timesteps.

# Run this file in a terminal using "python numerical_method.py".

# Group 16
# Ilja van Vuuren
# Nick Moone
# Willem Breedveld

import matplotlib.pyplot as plt
import numpy as np

# Make lists to store data for plotting.
infected_list = []
susceptible_list = []
recovered_list = []
infected_timestep = []
time_list = []

# Initialize parameters.
N = 17400000
infected = 135607
recovered = 2000000
susceptible = N-(infected+recovered)
vaccinated = 141000/N

k = 1/15
b = 1.75
steps = 1

infected_average = infected/N
susceptible_average = susceptible/N
recovered_average = recovered/N

# Makes numerical approximation  per timestep.
for t in np.arange(0, 26, steps):
    slope_infected = (b*susceptible_average*infected_average)-(k*infected_average)
    slope_susceptible = -b*susceptible_average*infected_average
    slope_recovered = k*infected_average

    infected_list.append(infected_average)
    susceptible_list.append(susceptible_average)
    recovered_list.append(recovered_average)
    infected_timestep.append(slope_infected*steps)
    time_list.append(t)

    infected_average = infected_average+(slope_infected*steps)-vaccinated
    susceptible_average = susceptible_average+(slope_susceptible*steps)
    recovered_average = recovered_average+(slope_recovered*steps)+vaccinated

# Show the plots.
plt.plot(time_list, infected_list, '--', color='orange', label='Total amount of infected')
plt.plot(time_list, susceptible_list, '--', color='purple', label='Total amount of susceptible')
plt.plot(time_list, recovered_list, '--', color='royalblue', label='Total amount of recovered')
plt.plot(time_list, infected_timestep, color='red', label='Amount infected per timestep')
plt.title('Simulation of numerical method (SIR method)')
plt.xlabel('time (steps x 15 days)')
plt.ylabel('part of population')
plt.legend()

plt.show()
