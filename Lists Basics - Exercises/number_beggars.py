money_list = input().split(", ")
beggars_count = int(input())
total_beggars_sum = []
money_list_as_digits = []
index_step = 0
for money in money_list:
    money_list_as_digits.append(int(money))
while index_step < beggars_count:
    sum_for_current_beggar = 0
    for step_index in range(index_step, len(money_list_as_digits), beggars_count):
        sum_for_current_beggar += money_list_as_digits[step_index]
    total_beggars_sum.append(sum_for_current_beggar)
    index_step += 1
print(total_beggars_sum)
