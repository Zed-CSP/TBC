# 2D Car Simulator

This project implements a simple 2D vehicle simulator using a bicycle model for vehicle dynamics. The simulator models a vehicle's motion including acceleration, steering, and trajectory plotting.

## Features

- 2D vehicle state simulation (position, velocity, heading angle)
- Bicycle model kinematics
- Trajectory visualization
- Acceleration analysis (longitudinal and lateral)

## Requirements

| Package    | Version |
|------------|---------|
| numpy      | 1.24.0  |
| matplotlib | 3.7.1   |

Install required packages using:

```bash
pip install numpy matplotlib
```

## Vehicle States

The simulator tracks the following vehicle states:
- `x`: Position on the x-axis (meters)
- `y`: Position on the y-axis (meters)
- `v`: Vehicle speed in the direction of travel (m/s)
- `theta`: Angle with respect to x-axis (radians)

## Running the Simulation

To run the car simulator:

```bash
python car_simulator.py
```

### Expected Output
The simulation will generate two plots:
1. Vehicle Trajectory Plot
   - Shows the complete path of the vehicle on an xy plane
   - Equal axis scaling for proper visualization
2. Acceleration Analysis Plot
   - Shows longitudinal and lateral accelerations over time
   - Includes legend and grid for better readability

## Simulation Parameters

The default simulation:
- Initial speed: 0 m/s
- Target speed: 10 m/s
- Acceleration: 0.4 m/s²
- Circle radius: ~100 m
- Simulation duration: 100 seconds
- Time step: 0.1 seconds
- Wheelbase: 2.89 m (Tesla Model Y specifications)

## Implementation Details

### CarSimulator Class
- Implements bicycle model kinematics
- Updates vehicle states based on:
  - Commanded acceleration
  - Wheel steering angle
  - Time step

### Main Simulation
1. Accelerates vehicle to target speed on straight path
2. Transitions to circular motion at constant speed
3. Records and plots trajectory and accelerations

## Notes
- All units follow SI convention:
  - Distances in meters (m)
  - Time in seconds (s)
  - Angles in radians (rad)
  - Velocities in meters per second (m/s)
  - Accelerations in meters per second squared (m/s²)

## Author
Chris