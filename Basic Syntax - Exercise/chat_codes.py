messages_count = int(input())
for message in range(1, messages_count + 1):
    message_code = int(input())
    if message_code == 88:
        print("Hello")
    elif message_code == 86:
        print("How are you?")
    elif not message_code == 88 and not message_code == 86:
        if message_code < 88:
            print("GREAT!")
    if message_code > 88:
        print("Bye.")
