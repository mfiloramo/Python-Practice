import matplotlib.pyplot as plt

# This is a simple exercise in plotting a simple line graph.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis="both", labelsize=14)

plt.show()


# This is a simple exercise in plotting a simple scatter graph.
# These would be simple coordinates for the scatter graph.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# These efficiently create a range of numbers for the coordinates of the scatter graph.
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Creates a generic-looking scatter.
plt.scatter(x_values, y_values, edgecolor="none", s=40)

# Creates a scatter with custom colors, passed as a tuple, with RGB values (respectively).
# The RGB values can be from 0 to 1.
plt.scatter(x_values, y_values, c=(0, 0, 0.8), s=40)

# Creates a scatter with a gradient colormap, assigned by the user.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
# Alternatively, plt.savefig("squares_plot.png", bbox_inches = "tight")
# would save an image of the plot. The first argument is the filename. The second
# trims whitespace in the image. You may omit this argument if you do want the whitespace.

# Create and plot a simulated random walk.
from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        return choice([1, -1]) * choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_step = RandomWalk.get_step(self)
            y_step = RandomWalk.get_step(self)

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    # Makes it so that the colors shift from light to dark (in a given hue) as they ascend.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=1)
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)  # This would make a line graph of the RandomWalk.

    # Emphasize the first and last points.
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
