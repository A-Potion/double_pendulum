#This code is provided by Hack Club for use in our #accelerate program.
#It is licensed under the MIT License (see LICENSE).
#Feel free to use and modify it as you see fit!

#Remember to install Hackatime, and use it to track your coding time!

#Your goal is to think outside the box. Think about what cool features you could add to this model.

#You have two weeks for this. You must submit your progress by the end of the first week, and your final project by the end of the second week.

import math
from flask import Flask, render_template
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.server.server import Server
from bokeh.io import show

app = Flask(__name__)

class pendulum_vertici: # Class representing each ball of the pendulum

    def __init__(self, x, y):
        self._x = x
        self._y = y
        
        self._x_velocity = 0
        self._y_velocity = 0
        
        self._x_acceleration = 0
        self._y_acceleration = 0

        self._x_tension = 0
        self._y_tension = 0

        self._tension_acute_vertical_angle = 0


    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_x_velocity(self):
        return self._x_velocity
    
    def get_y_velocity(self):
        return self._y_velocity
    
    def get_velocity(self):
        return (self._x_velocity**2 + self._y_velocity**2)**0.5
    
    def get_velocity_angle(self):
        return math.atan2(self._y_velocity, self._x_velocity)


@app.route('/')
def index():
    return render_template('index.html')