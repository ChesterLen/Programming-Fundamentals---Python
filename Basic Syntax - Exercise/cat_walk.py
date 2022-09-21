minutes_walk_per_day = int(input())
walk_count_per_day = int(input())
calories_consumed_per_day = int(input())
calories_burned = 5
total_minutes_walk_per_day = minutes_walk_per_day * walk_count_per_day
total_calories_burned_per_day = total_minutes_walk_per_day * 5
total_calories_consumed_per_day = calories_consumed_per_day * 50 / 100
if total_calories_burned_per_day >= total_calories_consumed_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned_per_day}.")
