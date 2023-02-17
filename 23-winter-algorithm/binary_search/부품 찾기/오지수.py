n = int(input())
parts = set(map(int, input().split()))

m = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if order in parts:
        print("yes", end=" ")
    else:
        print("no", end=" ")
