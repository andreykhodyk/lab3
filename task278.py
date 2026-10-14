d = int(input())
r = int(input())
b = int(input())

d = d * 100
b = b * 100

years = 0
while d < b:
    d = d + d * r // 100
    years += 1

print(years)