from flask import Flask
import math

app = Flask(__name__)

class Double_Pendulum:
    def __init__(self, origin_x: float=500, origin_y: float=250, l1: float=50, l2: float=50, m1: float=1, m2: float=1, g: float=9.81, theta1: float=30, theta2: float=0, omega1: float=2, omega2: float=1):
        self.origin_x = origin_y
        self.origin_y = origin_x
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.g = 2
        self.theta1 = theta1
        self.theta2 = theta2
        self.omega1 = omega1
        self.omega2 = omega2

        self.x1 = self.origin_x - self.l1 * math.sin(theta1)
        self.y1 = self.origin_y - self.l1 * math.cos(theta1)

        self.x2 = self.x1 - self.l2 * math.sin(theta2)
        self.y2 = self.y2 - self.l2 * math.cos(theta2)


    def step(self, dt: float=0.03):
        d1 = 


@app.route("/")
def hello_world():
    return "<p>hello, world!</p>"

@app.route("/pendulum-state")
def pendulum_state():
    return "<p>pendulum state</p>"