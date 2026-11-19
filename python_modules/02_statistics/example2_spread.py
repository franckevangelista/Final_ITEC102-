import statistics

class_a = [75, 76, 74, 75, 75]
class_b = [50, 100, 60, 90, 75]

for name, data in (("Class A", class_a), ("Class B", class_b)):
    print(name)
    print("  Mean:   ", statistics.mean(data))
    print("  Stdev:  ", round(statistics.stdev(data), 2))
    print("  Range:  ", max(data) - min(data))

# stdev = sample, pstdev = whole population
print(round(statistics.stdev(class_b), 2), round(statistics.pstdev(class_b), 2))
