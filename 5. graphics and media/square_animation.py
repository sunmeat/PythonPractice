import tkinter as tk
import math

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Animated Square")

# Create a canvas inside the window
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a square on the canvas
square_size = 50
square = canvas.create_rectangle(0, 0, square_size, square_size, fill="red")

# Define the center coordinates of the window
center_x = 150
center_y = 150

# Define the radius and angle for circular motion
radius = 100
angle = 0

# Function for animating the square's circular motion
def animate():
    global angle

    # Calculate the new coordinates of the square
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    # Update the position of the square
    canvas.coords(square, x, y, x + square_size, y + square_size)

    # Increase the angle for the next animation step
    angle += 0.01

    # Schedule the next animation step after a short delay
    canvas.after(10, animate)

# Start the animation
animate()

# Run the event loop
root.mainloop()