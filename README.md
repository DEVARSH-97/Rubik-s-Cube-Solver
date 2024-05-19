# Rubik-s-Cube-Solver

This project implements an automatic Rubik's Cube solving machine using computer vision and motor control. The system is designed to capture input from a camera, display the cube faces on a computer screen, encode the data, and then pass it to the Kociemba algorithm for solving. The resulting moves are then translated into motor commands to solve the cube physically.

# Features

Camera Input: Captures the Rubik's Cube faces using a camera.

Color Detection Model: Utilizes machine learning for accurate color detection, trained to handle various lighting conditions.

Computer Screen Display: Shows the Rubik's Cube configuration on the computer screen.

Kociemba Algorithm: Applies the Kociemba algorithm to determine the optimal moves for solving the Rubik's Cube.

Motor Control: Executes the calculated moves on the physical cube using motors controlled by Raspberry Pi.
