import tkinter as tk
import random

class Pet():
    def __init__(self):
        self.window = tk.Tk()
        
        # Load the image for the pet
        self.img = tk.PhotoImage(file='stella.png')  # Replace with the path to your image
        
        self.timestamp = 0
        self.window.config(background='black')
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)  # Makes window frameless
        self.window.attributes('-topmost', True)  # Puts window on top
        
        self.label = tk.Label(self.window, bd=0, bg='black')  # Creates a label as a container for the image
        self.label.configure(image=self.img)
        self.label.pack()
        
        # Initial position of the pet (randomized)
        self.x = random.randint(100, 1400)
        self.y = random.randint(100, 700)
        
        # Initial speed of the pet
        self.speed = 2
        
        # Random directions for movement
        self.dx = random.choice([-1, 1])  # Horizontal movement direction (left or right)
        self.dy = random.choice([-1, 1])  # Vertical movement direction (up or down)
        
        # Set the initial geometry for the pet's window
        self.window.geometry('1920x1080+{}+{}'.format(str(self.x), str(self.y)))
        
        # Start the movement loop
        self.window.after(0, self.update)
        
        self.window.mainloop()

    def update(self):
        # Move the pet in the current direction
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        # Bounce the pet off the left and right edges
        if self.x <= 0 or self.x >= 1500 - 128:  # Subtracting image width (128px) from window width
            self.dx = -self.dx  # Reverse horizontal direction
        
        # Bounce the pet off the top and bottom edges
        if self.y <= 0 or self.y >= 800 - 128:  # Subtracting image height (128px) from window height
            self.dy = -self.dy  # Reverse vertical direction
        
        # Update the position of the pet's window
        self.window.geometry('128x128+{}+{}'.format(int(self.x), int(self.y)))
        
        # Update the image (no change, it's always the same image)
        self.label.configure(image=self.img)
        
        # Update at regular intervals
        self.window.after(20, self.update)  # 20 milliseconds between updates
        
        # Keep the window on top of others
        self.window.lift()

# Initialize the pet
Pet()
