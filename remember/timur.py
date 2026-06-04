d1, d2, d3 = int(input()), int(input()), int(input())

print(min(d1, d2) + min(d1 + d2, d3) + min(d3 + min(d1, d2), max(d1, d2)))
