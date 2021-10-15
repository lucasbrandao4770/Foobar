# What is the Foobar Challenge
"Google's Foobar Challenge is believed to be a secret hiring process by the company to recruit top programmers and developers around the world. And it is known that several developers at Google are hired by this process.

The challenge consists of five levels with a total of nine questions, with the level of difficulty increasing at each level."

Even without the hiring thing, it's still an exciting programming challenge to solve!

# Constraints
The Foobar Challenge can be answered using either Java or Python. I chose to use Python, and had to code under some restraints:

![Constraints](https://i.imgur.com/AOOSbar.png)

# Level 1 -> Minion Work Assignments 
![Level 1 - Problem](https://i.imgur.com/7c5PEZ1.png)
![Level 1 - Test Cases](https://i.imgur.com/voRkJiD.png)

The first level was really simple. Given a list of numbers and a restriction 'n', I was asked to remove from the list any number that is repeated more than 'n' times.

I used an dict-based approach to save the number of times each variable occurred, and then iterated through the dict saving only the keys that didn't repeat more than 'n' times.

# Level 2-1 -> Elevator Maintenance
![Level 2-1 - Problem](https://i.imgur.com/1y0OGHG.png)
![Level 2-1 - Test Cases](https://i.imgur.com/JPJrury.png)

The second level was a bit harder. Given a list of strings representing the a "version" system, I was asked to sort the list in ascending order.

To solve this one, I first tried using "sorted()" to sort the list. As expected, it didn't work. I proceeded to then create my own personalized sorting algorithm, using Bubble Sort. For that to work, I separated the strings with "split('.')", then created a data type using tuples for holding the versions, filling empty spaces with 'None'.

The list of tuples was then iterated through and sorted using my own Bubble Sort implementation. After that, all I had to do was to transform the tuples back to strings, and then return the sorted list.
