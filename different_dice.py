from die import Die
import pygal

# Create a D6 and a D10 
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the results in a list
results = []
for value in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results
x_labels = []
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    x_labels.append(str(value))
    
# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and D10 dice 50,000 times" 
hist.x_labels = (x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('d6_d10_visual.svg')

