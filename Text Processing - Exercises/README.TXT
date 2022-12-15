    1. Valid Usernames
Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
A valid username:
    • has length between 3 and 16 characters inclusive
    • can contain only letters, numbers, hyphens, and underscores
    • has no redundant symbols before, after, or in between

    2.  Character Multiplier
Create a program that receives two strings on a single line separated by a single space.
Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

    3.  Extract File
Write a program that reads the path to a file and subtracts the file name and its extension.

    4.  Caesar Cipher
Write a program that returns an encrypted version of the same text.
Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

    5.  Emoticon Finder
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.

    6.  Replace Repeating Chars
Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

    7.  String Explosion
Write a program that reads a string from the console that contains:
    • Explosions marked with '>'
    • Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
    • Any other characters
Your task is to delete x characters, starting after the exploded character ('>').
If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
When all characters are processed, print the final string.
Constraints

    8.  Letters Change Numbers
John invented a game with numbers and letters from the English alphabet. The game was simple.
You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:
    • First, if the letter in front of the number is:
        ◦ Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
        ◦ Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
    • Next, if the letter after the number is:
        ◦ Uppercase: subtract its position from the resulting number (starting from 1)
        ◦ Lowercase: add its position to the resulting number (starting from 1)
The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results.
Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
He kindly asks you to write a program that performs the operations described above and sums the final results of each string.

    9.  Rage Quit
Every gamer knows what rage-quitting means. It's when you're just not good enough, and you blame everybody else for losing a game - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console.
In the example, you need to write back "AAA".
First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
Next, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.

    10. Winning Ticket
The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the task of creating a program that automatically checks if a ticket is a winner.
You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:
    • A valid ticket has exactly 20 characters.
    • A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
    • In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
An example of a valid winning ticket:
"Cash$$$$$$Ca$$$$$$sh"
An example of a Jackpot winning valid ticket:
"$$$$$$$$$$$$$$$$$$$$"
