# Movement Tracker 2D

## Description

This program simulates the movement of a person (P) in a 2D world, starting from the reference point `S` (0,0). The movement is based on a sequence of commands, where each command consists of a distance and a direction. The directions include North (N), South (S), East (E), West (W), North-East (NE), North-West (NW), South-East (SE), and South-West (SW). 

The program tracks the movement, calculates the total distance traveled from the starting point, and visually plots the path on a 2D coordinate plane using **Matplotlib**.

## Features
- **Track Movement**: Tracks the movement based on a sequence of distance and direction inputs.
- **Current Location**: Interprets and prints the current location relative to the starting point (`S`).
- **Total Distance**: Calculates and displays the total distance traveled.
- **2D Visualization**: Generates a 2D plot showing the movement path.

## Installation

Before running this program, make sure you have **Python 3.x** installed along with the following dependencies:

- **Matplotlib** for plotting the movement path
- **NumPy** for numerical calculations

To install the required dependencies, run the following command:

```bash
pip install matplotlib numpy
