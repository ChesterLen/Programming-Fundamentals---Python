    1. Count Chars in a String
Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"

    Examples:

    Input: text

    Output: t -> 2
            e -> 1
            x -> 1

    2. A Miner Task
You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"

    3. Capitals
Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", ").
Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

    4. Phonebook
Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
In case the contact isn't found, print: "Contact {name} does not exist."

    5. Legendary Farming
You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
    • "Shadowmourne" - requires 250 Shards
    • "Valanyr" - requires 250 Fragments
    • "Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
You will be given lines of input in the format:
"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
In the end, print the remaining shards, fragments, motes in the format:
"shards: {number_of_shards}
fragments: {number_of_fragments}
motes: {number_of_motes}"
Finally, print the collected junk items in the order of appearance.

    6. Orders
Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
    • If the product doesn't exist yet, add it with its starting quantity.
    • If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product.
Input
    • Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
    • The product data is always delimited by a single space.
Output
    • Print information about each product in the following format:
"{product_name} -> {total_price}"
    • Format the total price to the 2nd digit after the decimal separator.

    7. SoftUni Parking
SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work.
It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
The program receives 2 types of commands:
    • "register {username} {license_plate_number}":
        ◦ The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
"ERROR: already registered with plate number {license_plate_number}"
        ◦ If the check above passes successfully, the user should be registered, so the system should print:
 "{username} registered {license_plate_number} successfully"
    • "unregister {username}":
        ◦ If the user is not present in the database, the system should print:
"ERROR: user {username} not found"
        ◦ If the check above passes successfully, the system should print:
"{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users and their license plates in the format:
    • "{username} => {license_plate_number}"
Input
    • First line: n - number of commands - integer
    • Next n lines: commands in one of the two possible formats:
        ◦ Register: "register {username} {license_plate_number}"
        ◦ Unregister: "unregister {username}"

    8. Courses
Write a program that keeps the information about courses. Each course has a name and registered students.
You will be receiving a course name and a student name until you receive the command "end".
You should register each user into the corresponding course. If the given course does not exist, add it.
When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.
Input
    • Until the "end" command is received, you will be receiving input lines in the format:
"{course_name} : {student_name}"
    • The product data is always delimited by " : "
Output
    • Print the information about each course in the following format:
"{course_name}: {registered_students}"
    • Print the information about each student in the following format:
"-- {student_name}"

    9.  Student Academy
Write a program that keeps the information about students and their grades.
On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.

    10. Company Users
Write a program that keeps the information about companies and their employees.
You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"

    11. Force Book
The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles.
You should store information for every unique force user registered in the application.
You will receive several input lines in one of the following formats:
"{force_side} | {force_user}"
"{force_user} -> {force_side}"
The "force_user" and "force_side" are strings, containing any character.
If you receive "force_side | force_user":
    • If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
    • Only if there is no such force user in any force side -> add the force user to the corresponding side.
    • If there is such force user already -> skip the command and continue to the next operation.
If you receive a "force_user -> force_side":
    • If there is such force user already -> change their side.
    • If there is no such force user in any force side -> add the force user to the corresponding force side.
    • If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
    • Then you should print on the console: "{force_user} joins the {force_side} side!".
You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
In case there are no force users on a side, you shouldn't print the side information.

    12. SoftUni Exam Results
Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly.
You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and their submissions and points.
If a student has two or more submissions for the same language, save only his maximum points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished", print each of the participants in the following format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
After that, print each language used in the exam in the following format:
"Submissions:
{language1} - {submissions_count}
{language2} - {submissions_count}
…
{language3} - {submissions_count}"
