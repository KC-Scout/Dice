from die import Die
import pygal

# Create two D6 die
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls and store results in a list
results = []
for roll in range(10):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
        
# Analyze the results.
frequencies = []
# Automatically generate x labels
x_labels = [] 
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    x_labels.append(str(value))
    
# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 Dice 1000 times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_dice_visual.svg')
