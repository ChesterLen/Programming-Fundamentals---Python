def valid_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    symbols_list = ["@", "#", "$", "^"]
    left_ticket_part = ticket[:10]
    right_ticket_part = ticket[10:]
    for symbol in symbols_list:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = symbol * uninterrupted_match_length
            if winning_symbol_repetitions in left_ticket_part and winning_symbol_repetitions in right_ticket_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(valid_ticket(ticket))
