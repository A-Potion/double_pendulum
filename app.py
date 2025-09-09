#This code is provided by Hack Club for use in our #accelerate program.
#It is licensed under the MIT License (see LICENSE).
#Feel free to use and modify it as you see fit!

#Remember to install Hackatime, and use it to track your coding time!

#Your goal is to think outside the box. Think about what cool features you could add to this model.

#You have two weeks for this. You must submit your progress by the end of the first week, and your final project by the end of the second week.

import math
from flask import Flask, render_template, jsonify
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.server.server import Server
from bokeh.io import show

app = Flask(__name__)


import threading

class DoublePendulum:
    def __init__(self, origin_x: float=300, origin_y: float=100, L1: float=120, L2: float=120, m1: float=10, m2: float=10, g: float=9.81, theta1: float=math.pi/2, theta2: float=math.pi/2, omega1: float=0.0, omega2: float=0.0):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.L1 = L1
        self.L2 = L2
        self.m1 = m1
        self.m2 = m2
        self.g = g
        # Initial conditions
        self.theta1 = theta1
        self.theta2 = theta2
        self.omega1 = omega1
        self.omega2 = omega2   
        self.x1 = self.origin_x + self.L1 * math.sin(self.theta1)
        self.y1 = self.origin_y + self.L1 * math.cos(self.theta1)
        self.x2 = self.x1 + self.L2 * math.sin(self.theta2)
        self.y2 = self.y1 + self.L2 * math.cos(self.theta2)

    def step(self, dt: float=0.06):
        delta = self.theta2 - self.theta1
        denom1 = (self.m1 + self.m2) * self.L1 - self.m2 * self.L1 * math.cos(delta) ** 2
        denom2 = (self.L2 / self.L1) * denom1

        a1 = (self.m2 * self.L1 * self.omega1 ** 2 * math.sin(delta) * math.cos(delta) +
              self.m2 * self.g * math.sin(self.theta2) * math.cos(delta) +
              self.m2 * self.L2 * self.omega2 ** 2 * math.sin(delta) -
              (self.m1 + self.m2) * self.g * math.sin(self.theta1)) / denom1

        a2 = (-self.m2 * self.L2 * self.omega2 ** 2 * math.sin(delta) * math.cos(delta) +
              (self.m1 + self.m2) * self.g * math.sin(self.theta1) * math.cos(delta) -
              (self.m1 + self.m2) * self.L1 * self.omega1 ** 2 * math.sin(delta) -
              (self.m1 + self.m2) * self.g * math.sin(self.theta2)) / denom2

        self.omega1 += a1 * dt
        self.omega2 += a2 * dt
        self.theta1 += self.omega1 * dt
        self.theta2 += self.omega2 * dt

        self.x1 = self.origin_x + self.L1 * math.sin(self.theta1)
        self.y1 = self.origin_y + self.L1 * math.cos(self.theta1)
        self.x2 = self.x1 + self.L2 * math.sin(self.theta2)
        self.y2 = self.y1 + self.L2 * math.cos(self.theta2)

    def get_coords(self):
        return [
            {'x': self.x1, 'y': self.y1},
            {'x': self.x2, 'y': self.y2}
        ]

# Create simulation instance
double_pendulum = DoublePendulum()

def run_simulation():
    while True:
        double_pendulum.step()
        threading.Event().wait(0.02)

# Start simulation in background thread
threading.Thread(target=run_simulation, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html', origin_x=double_pendulum.origin_x, origin_y=double_pendulum.origin_y)

# API route to get pendulum coordinates
@app.route('/coords')
def coords():
    return jsonify(double_pendulum.get_coords())