# Statistical Engineering & Simulation Assignment

## Student Name: ziyad Ayub
## Course: Statistical Engineering & Simulation

---

# Project Overview

This project consists of two main parts:

- Part 1: A custom-built statistical engine (StatEngine) that calculates mean, median, mode, variance, standard deviation, and detects outliers using pure Python.
- Part 2: A Monte Carlo simulation that models a server crash probability and demonstrates the Law of Large Numbers (LLN).

The goal of this project is to understand statistical computations from scratch and observe how probability behaves in real-world simulations.

---

# Mathematical Logic

## Variance

Two types of variance are implemented:

- Population Variance:
  
  variance = Σ(x - mean)² / n

- Sample Variance (Bessel’s Correction):
  
  variance = Σ(x - mean)² / (n - 1)

The sample variance uses (n - 1) to correct bias when estimating from a sample.

---

## Median (Even vs Odd)

- If the number of elements is odd:
  - The middle value after sorting is selected

- If the number of elements is even:
  - The median is the average of the two middle values

---

# Part 1: Statistical Engine

## Features

- Mean, Median, Mode (supports multiple modes)
- Variance (sample and population)
- Standard Deviation
- Outlier detection using Z-score
- Error handling for invalid input

---

# Part 2: Simulation (Law of Large Numbers)

## Description

A simulation is performed where a server has a 4.5% chance of crashing per day.

The simulation runs for different numbers of days and calculates the observed probability.

---

## Key Insight

As the number of days increases, the observed probability approaches the true probability (0.045), demonstrating the Law of Large Numbers.
# Setup Instructions
 1. Clone the repository:
 2. Navigate to the project folder:
 3. Run the Python file:
# Testing
This project uses Python’s built-in unittest module to verify correctness.

## How to Run Tests

1. Make sure you are in the project directory

2. Run the following command:
    python -m unittest test_statengine.py
## What is Tested

- Mean, median, and mode calculations
- Sample vs population variance
- Outlier detection
- Handling empty input
- Handling invalid (non-numeric) data

All tests are designed to ensure the statistical engine behaves correctly, including edge cases.
   
