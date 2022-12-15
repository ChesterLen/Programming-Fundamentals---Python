numbers = input().split(", ")
positive = [int(i) for i in numbers if int(i) >= 0]
negative = [int(i) for i in numbers if int(i) < 0]
even = [int(i) for i in numbers if int(i) % 2 == 0]
odd = [int(i) for i in numbers if int(i) % 2 != 0]
print("Positive:", ", ".join(str(i) for i in positive))
print("Negative:", ", ".join(str(i) for i in negative))
print("Even:", ", ".join(str(i) for i in even))
print("Odd:", ", ".join(str(i) for i in odd))
