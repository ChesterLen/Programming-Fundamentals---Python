    1. Which Are In?
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

    Examples:

    Input: arp, live, strong                         Output: ['arp', 'live', 'strong']
           lively, alive, harp, sharp, armstrong

    Input: tarp, mice, bull                          Output: []
           lively, alive, harp, sharp, armstrong

    2. Next Version
You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version.
For example, if the current version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below.
Note: there will be no case in which the first number will become greater than 9.

    Examples:

    Input: 1.2.3    Output: 1.2.4

    Input: 1.3.9    Output: 1.4.0

    Input: 3.9.9    Output: 4.0.0

    3. Word Filter
Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even.
Print each word on a new line.

    Examples:

    Input: kiwi orange banana apple    Output: kiwi
                                               orange
                                               banana

    Input: pizza cake pasta chips      Output: cake

    4. Number Classification
Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number

    Examples:

    Input: 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33     Output: Positive: 1, 0, 5, 3, 4, 12, 19
                                                                 Negative: -2, -100, -20, -33
                                                                 Even: -2, 0, 4, -100, -20, 12
                                                                 Odd: 1, 5, 3, 19, -33

    Input: 1, 2, 53, 2, 21                               Output: Positive: 1, 2, 53, 2, 21
                                                                 Negative:
                                                                 Even: 2, 2
                                                                 Odd: 1, 53, 21

    5. Office Chairs
You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
Keep track of the free chairs:
    • If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
    • Otherwise, print: "Game On, {total_free_chairs} free chairs left".

    Examples:

    Input: 4            Output: Game On, 4 free chairs left
           XXXX 4
           XX 1
           XXXXXX 3
           XXX 3

    Input: 3             Output: 1 more chairs needed in room 2
           XXXXXXX 5             2 more chairs needed in room 3
           XXXX 5
           XXXXXX 8

    6. Electron Distribution
You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.
You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more electrons left. The rules for electron distribution are as follows:
    • The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
    • You should start filling the shells from the first one at the first position.
    • If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.
In the end, print a list with the filled shells.

    7. Group of 10's
Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
    • The numbers 2, 8, 4, and 10 fall into the group of 10's.
    • The numbers 13, 19, 14, and 15 fall into the group of 20's.

    8. Decipher This!
You are given a secret message you should decipher. To do that, you need to know that in each word:
    • the second and the last letter are switched (e.g., Holle means Hello)
    • the first letter is replaced by its character code (e.g., 72 means H)

    9. Anonymous Threat
Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and unbelievably clever merging and dividing data into partitions.
As the lead security developer in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data.
You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:
    • merge {startIndex} {endIndex}
    • divide {index} {partitions}
Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them.
Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length. The count of the substrings should be equal to the given partitions.
Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest.
Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.

    10. Pokemon Don't Go
Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression. And so Ely now plays Pokemon Don't Go.
In Pokemon Don't Go, when you walk to a certain pokemon, those closest to you naturally get further, and those further from you, get closer.
You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin receiving integers, which will correspond to indexes in that sequence.
When you receive an index, you must remove the element at that index from the sequence (as if you've captured the pokemon).
    • You must increase the value of all elements in the sequence which are less or equal to the removed element with the value of the removed element.
    • You must decrease the value of all elements in the sequence which are greater than the removed element with the value of the removed element.
If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy the first element to its place.
The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.
The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).
