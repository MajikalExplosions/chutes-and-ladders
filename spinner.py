from tkinter import *
import random
import math
import time

class spinner:
    def __init__(self, centerX, centerY, radius, canvas):
        self.radius = radius
        self.centerX = centerX
        self.centerY = centerY
        self.canvas = canvas

        #creates the six sections of the spinner, the actual spinning line, labels, and the center circle
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=0, extent=60,
                               fill="red")
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=60, extent=60,
                               fill="blue")
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=120, extent=60,
                               fill="green")
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=180, extent=60,
                               fill="yellow")
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=240, extent=60,
                               fill="purple")
        self.canvas.create_arc(centerX - self.radius, centerY - self.radius, centerX + self.radius, centerY + self.radius, start=300, extent=60,
                               fill="orange")

        spinnerWidth = self.radius / 15
        self.spinner = self.canvas.create_line(centerX, centerY, centerX + (self.radius + math.cos(-math.pi / 6)), centerY + (math.sin(-math.pi / 6)), width=spinnerWidth, fill="black")

        ovalRadius = self.radius / 10
        self.canvas.create_oval(centerX - ovalRadius, centerY - ovalRadius, centerX + ovalRadius, centerY + ovalRadius, fill="brown")

        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(math.pi / 6), self.centerY - self.radius / 2 * math.sin(math.pi / 6), font=("Avenir", 30), text="1")
        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(math.pi / 2), self.centerY - self.radius / 2 * math.sin(math.pi / 2), font=("Avenir", 30), text="2")
        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(5 * math.pi / 6), self.centerY - self.radius / 2 * math.sin(5 * math.pi / 6), font=("Avenir", 30), text="3")
        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(7 * math.pi / 6), self.centerY - self.radius / 2 * math.sin(7 * math.pi / 6), font=("Avenir", 30), text="4")
        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(3 * math.pi / 2), self.centerY - self.radius / 2 * math.sin(3 * math.pi / 2), font=("Avenir", 30), text="5")
        self.canvas.create_text(self.centerX + self.radius / 2 * math.cos(11 * math.pi / 6), self.centerY - self.radius / 2 * math.sin(11 * math.pi / 6), font=("Avenir", 30), text="6")

    def spin(self):
        randNum = random.randrange(1, 7) #generates random integer between 1-6 to be returned

        #represents how much the spinner moves in each frame of animation
        #e.g. radianDivisor = 12 means it moves pi/12 radians in each frame
        radianDivisor = 12

        #spinner starts at arbitrary default of -pi/6 radians
        angle = -math.pi / 6

        #animates the spinner and makes it stop in the correct part depending on the value of randNum
        for i in range((radianDivisor * 12) + (4 * randNum)):
            angle += math.pi / radianDivisor
            self.rotateSpinner(angle)
            self.canvas._root().update()
            time.sleep(0.01)

        return randNum
    
    #rotates spinner for the specified angle (in radians)
    def rotateSpinner(self, angle):
        self.canvas.coords(self.spinner, self.centerX, self.centerY, self.centerX + (self.radius * math.cos(angle)),
                           self.centerY - (self.radius * math.sin(angle)))
