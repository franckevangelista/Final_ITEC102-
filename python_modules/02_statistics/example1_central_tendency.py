import statistics

scores = [85, 90, 78, 92, 88, 90, 76, 90]

print("Mean:  ", statistics.mean(scores))
print("Median:", statistics.median(scores))
print("Mode:  ", statistics.mode(scores))
print("Low median:", statistics.median_low(scores))
print("High median:", statistics.median_high(scores))
