with open('day1.txt', 'r') as f:
  report = [int(line.rstrip()) for line in f]
  total = 0
  for i in range(1, len(report)):
    if(report[i] > report[i-1]):
      total += 1

print(total)
    