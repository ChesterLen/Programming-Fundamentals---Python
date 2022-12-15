text = input().split(" ")
filtered = filter(lambda x: len(x) % 2 == 0, text)
for i in filtered:
    print(i)
