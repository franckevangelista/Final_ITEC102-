import statistics

grades = [62, 70, 75, 78, 80, 84, 88, 91, 95, 99]
q1, q2, q3 = statistics.quantiles(grades, n=4)
print(f"Q1={q1}, Q2 (median)={q2}, Q3={q3}")
print("Interquartile range:", q3 - q1)

try:
    statistics.mean([])
except statistics.StatisticsError as error:
    print("Error caught:", error)
