bitcoin_count = int(input())
chinese_juana_count = float(input())
commission = float(input())
dollar = 1.76
euro = 1.95
bitcoin = bitcoin_count * 1168
chinese_juan = chinese_juana_count * 0.15 * dollar
total_sum = bitcoin + chinese_juan
total_sum /= euro
commission_sum = total_sum * commission / 100
total_sum -= commission_sum
print(f"{total_sum:.2f}")
