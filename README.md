# Buffon's-needle-problem
This repository contains a Python implementation of Buffon's Needle algorithm to estimate the value of π. The implementation attempts to handle both cases (z ≤ D and z > D) based on the length of the needle and the distance between the plates. It uses Monte Carlo simulation for estimating π through random throws.

This Python project attempts to implement Buffon's Needle algorithm to estimate the value of π using a Monte Carlo simulation.
The algorithm simulates the dropping of a needle of length z onto a plane with parallel lines spaced D units apart. Based on the needle's intersection with the lines, we estimate the value of π.

The exercise is divided into two main cases:

A) Case 1: z ≤ D
In this case, we calculate the probability of the needle intersecting a line using random throws of the needle.

B) Case 2: z > D
When the needle's length is greater than the spacing between the lines, we adjust the simulation to account for this difference.

C) Using the Results
We use the probabilities from the two cases to estimate the value of π.

The program will print the estimated value of π based on the experiment.
