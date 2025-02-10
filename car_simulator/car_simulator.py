# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)
# - NOTE: all units are SI: meters (m) for distances, seconds (s) for
#   time, radians (rad) for angles...
#
# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time

import numpy as np
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):
        # Update velocity using acceleration
        self.v = self.v + a * dt
        
        # Update theta (heading angle) based on wheel angle and velocity
        # Using bicycle model: theta_dot = v * tan(wheel_angle) / wheelbase
        self.theta = self.theta + (self.v * np.tan(wheel_angle) / self.wheelbase) * dt
        
        # Update position
        self.x = self.x + self.v * np.cos(self.theta) * dt
        self.y = self.y + self.v * np.sin(self.theta) * dt

def main():
    wheelbase = 2.89  # ************ tesla model Y wheelbase ;) ************
    v0 = 0
    theta0 = 0
    simulator = CarSimulator(wheelbase, v0, theta0)
    dt = 0.1  # time step
    
    # Simulation time array (100 seconds)
    t = np.arange(0, 100 + dt, dt)
    
    # Arrays to store results
    x_hist = []
    y_hist = []
    v_hist = []
    a_long_hist = []  # longitudinal acceleration
    a_lat_hist = []   # lateral acceleration
    
    target_speed = 10  # m/s
    acceleration = 0.4  # m/s^2
    
    # Calculate required wheel angle for 100m radius circle
    # For circular motion: R = wheelbase / tan(wheel_angle)
    circle_radius = 100
    wheel_angle_circle = -np.arctan(wheelbase / circle_radius)  # negative for clockwise
    
    for t_i in t:
        # Store current state
        x_hist.append(simulator.x)
        y_hist.append(simulator.y)
        v_hist.append(simulator.v)
        
        # Determine acceleration command
        if simulator.v < target_speed:
            a = acceleration
            wheel_angle = 0
        else:
            a = 0
            wheel_angle = wheel_angle_circle
        
        # Calculate accelerations
        a_long_hist.append(a)
        # Lateral acceleration = v^2/R when turning
        a_lat = simulator.v**2 * np.tan(wheel_angle) / simulator.wheelbase if wheel_angle != 0 else 0
        a_lat_hist.append(a_lat)
        
        # Simulate one step
        simulator.simulatorStep(a, wheel_angle, dt)
    
    # Plot trajectory
    plt.figure(figsize=(10, 10))
    plt.plot(x_hist, y_hist)
    plt.title('Vehicle Trajectory')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.axis('equal')
    plt.grid(True)
    plt.show()
    
    # Plot accelerations
    plt.figure(figsize=(10, 5))
    plt.plot(t, a_long_hist, label='Longitudinal')
    plt.plot(t, a_lat_hist, label='Lateral')
    plt.title('Vehicle Accelerations')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
