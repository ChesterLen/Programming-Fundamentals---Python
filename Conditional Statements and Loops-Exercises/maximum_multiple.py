divisor = int(input())
boundary = int(input())
max_int = 0
for _ in range(1, boundary + 1):
    if _ % divisor == 0:
        if max_int < _:
            max_int = _
if max_int <= boundary:
    if max_int > 0:
        print(max_int)
