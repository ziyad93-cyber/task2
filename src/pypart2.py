import random

def simulate_crashes(days):
    crash_rate = 0.045

    crash_count = 0

    for day in range(days):
        random_value = random.random() 

        if random_value < crash_rate:
            crash_count += 1

    observed_probability = crash_count / days

    return crash_count, observed_probability


test_days = [10, 100, 1000, 10000]

for days in test_days:
    crashes, probability = simulate_crashes(days)

    print("For", days, "days:")
    print("Total crashes:", crashes)
    print("Observed probability:", round(probability, 4))
    print("----------------------------")