# Assignment 1

# Part (a): Plot a line graph for temperature readings
import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 22, 19, 23, 21, 24, 20]

plt.plot(days, temperatures)
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Readings Over a Week')
plt.show()

# Part (b): Generate arithmetic sequence
sequence = [5 + i*3 for i in range(8)]
print("Arithmetic sequence:", sequence)

# Part (c): Calculate volume under the surface z = x^2 + y^2 over [0,1]x[0,1]
n = 100
delta = 1.0 / n
volume = 0.0
for i in range(n):
    for j in range(n):
        x = (i + 0.5) * delta
        y = (j + 0.5) * delta
        z = x**2 + y**2
        volume += z * delta * delta
print("Approximate volume:", volume)
