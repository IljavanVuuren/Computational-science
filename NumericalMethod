# Make lists to store data
infected_list = []
time_list = []

# Initialize variables
N = 100000
infected = 0.1*N
susceptible = N-0.1*N
b = 0.000000503
steps = 0.1

# Makes numerical approximation.
for t in np.arange(0, 100, steps):
    
    slope_infected = (1-(1-b)**infected)*susceptible
    slope_susceptible = -(1-(1-b)**infected)*susceptible
    infected_average = infected/N
    infected_list.append(infected_average)
    time_list.append(t)

    infected = infected+(slope_infected*steps)
    susceptible = susceptible+(slope_susceptible*steps)

# Plot the results.
plt.plot(time_list, infected_list, label='SIR model')
plt.xlabel('time')
plt.ylabel('infected')
plt.legend(loc='upper left')

plt.show()
