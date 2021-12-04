with open('day1.txt', 'r') as f:
  report = [int(line.rstrip()) for line in f]
  total = 0
  for i in range(1, len(report)):
    if(sum(report[i:i+3]) > sum(report[i-1:i+2])):
      total += 1

print(total)
    