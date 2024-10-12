import numpy as np
import matplotlib.pyplot as plt

# Read direction cosines from the output.txt file
with open('output.txt', 'r') as file:
    lines = file.readlines()
    l = float(lines[1].split('=')[1].strip())
    m = float(lines[2].split('=')[1].strip())
    n = float(lines[3].split('=')[1].strip())

# Define a range of t values for plotting the line
t = np.linspace(-1, 1, 100)  # Adjust the range as needed

# Parametric equations of the line
x = 1 + 12 * t  # Assuming the line passes through (1, -2, 3)
y = -2 + 2 * t
z = 3 + 3 * t

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the line
ax.plot(x, y, z, label='Line AB', color='b')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Plot of Line AB')
ax.legend()

# Define the text for direction cosines
direction_cosines_text = f"Direction Cosines:\n l = {l:.2f}\n m = {m:.2f}\n n = {n:.2f}"

# Place the text in the plot
ax.text(0.5, -2, 5, direction_cosines_text, fontsize=12, ha='center', color='red')

# Save the plot as figure1.png
plt.savefig('figure1.png')
plt.close()  # Close the plot to free up memory

