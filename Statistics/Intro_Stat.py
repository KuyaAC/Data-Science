"""Beginner-friendly examples of descriptive statistics."""

import statistics


# Quiz scores for five students
scores = [72, 85, 90, 85, 98]

print("Scores:", scores)
print("Count:", len(scores))

# Measures of center
print("Mean (average):", statistics.mean(scores))
print("Median (middle value):", statistics.median(scores))
print("Mode (most common value):", statistics.mode(scores))

# Measures of spread
print("Range:", max(scores) - min(scores))
print("Population variance:", statistics.pvariance(scores))
print("Population standard deviation:", statistics.pstdev(scores))

# Sample measures apply when the data is a sample from a larger population.
print("Sample variance:", statistics.variance(scores))
print("Sample standard deviation:", statistics.stdev(scores))

print("Sorted scores:", sorted(scores))
