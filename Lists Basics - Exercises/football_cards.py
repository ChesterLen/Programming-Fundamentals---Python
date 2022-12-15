cards_sequence = input()
cards_sequence_split = cards_sequence.split()
team_A = 11
team_B = 11
for card in cards_sequence_split:
    if card[0] == "A":
        team_A -= 1
    elif card[0] == "B":
        team_B -= 1
    if team_A < 7 or team_B < 7:
        break
print(f"Team A - {team_A}; Team B - {team_B}")
if team_A < 7 or team_B < 7:
    print("Game was terminated")
