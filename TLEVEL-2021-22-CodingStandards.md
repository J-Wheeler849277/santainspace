# Python Coding Standard
*T level students 2021/2022*<br />

**Contents**<br />
1. [Introduction](TLEVEL-2021-22-CodingStandards.md#introduction)<br />
2. [Clean Code](TLEVEL-2021-22-CodingStandards.md#clean-code)<br />
   - [Implications of having a bad code](TLEVEL-2021-22-CodingStandards.md#implications-of-having-a-bad-code)<br />
   - [What is a clean code?](TLEVEL-2021-22-CodingStandards.md#what-is-a-clean-code)<br />
   - [Smells of bad code](TLEVEL-2021-22-CodingStandards.md#smells-of-bad-code)<br />
3. [Conventions and style guide](TLEVEL-2021-22-CodingStandards.md#conventions-and-style-guide)<br />
   - [Indentation](TLEVEL-2021-22-CodingStandards.md#indentation)<br />
   - [Maximum line length](TLEVEL-2021-22-CodingStandards.md#maximum-line-length)<br />
   - [Comments](TLEVEL-2021-22-CodingStandards.md#comments)<br />
     - [Do not use a comment when you can use a function or a variable.](TLEVEL-2021-22-CodingStandards.md#do-not-use-a-comment-when-you-can-use-a-function-or-a-variable.)<br />
     - [Inline comments](TLEVEL-2021-22-CodingStandards.md#inline-comments)<br />
     - [Block Comments](TLEVEL-2021-22-CodingStandards.md#block-comments)<br />
   - [Naming styles](TLEVEL-2021-22-CodingStandards.md#naming-styles)<br />
   - [Names to Avoid.](TLEVEL-2021-22-CodingStandards.md#names-to-avoid.)<br />
   - [Strings quote](TLEVEL-2021-22-CodingStandards.md#strings-quote)<br />
4. [Defensive Programming](TLEVEL-2021-22-CodingStandards.md#defensive-programming)<br />
   - [Implementing defensive programming](TLEVEL-2021-22-CodingStandards.md#implementing-defensive-programming)<br />

## Signatures
[Signatures are located here](standards-signatures.md)

## Introduction
This document will outline the standards python coding convention that should be followed by T level students during the academic year 2021/2022. 

## Clean Code
Having a clean code is critical while developing software; therefore, it is the first thing that will be introduced in this document. And it will be mentioned again and again throughout the document. Any code written by the programmers who follow this coding convention should be clean.

Most of the topics that covered in this section are available in a book called “Clean Code by Robert C. Martin”. It is a book that almost all software developers read. 

### Implications of having a bad code.
A bad code will make it harder for developers to maintain the software in the future. Moreover, a bad code is more likely to contain more logical problems. Bad code also can decrease your productivity as a programmer; because you might spend a lot of time debugging and figuring out what you need to implement and where it needs to be implemented.

Yes, you might spend some time to ensure that your code is clean, but a clean code will save you a lot of time, I promise. 

### What is a clean code?
Here are some very well-known and deeply experienced programmers thought.

**Bjarne Stroustrup, inventor of C++ and author of The C++ Programming Language:**
> I like my code to be elegant and efficient. The logic should be straightforward to make it hard for bugs to hide, the dependencies minimal to ease maintenance, error handling complete according to an articulated strategy, and performance close to optimal so as not to tempt people to make the code messy with unprincipled optimizations. Clean code does one thing well.

**Grady Booch, author of Object-Oriented Analysis and Design with Applications:**
> Clean code is simple and direct. Clean code reads like well-written prose. Clean code never obscures the designer’s intent but rather is full of crisp abstractions and straightforward lines of control.

**“Big” Dave Thomas, founder of OTI, the godfather of the Eclipse strategy**
> Clean code can be read and enhanced by a developer other than its original author. It has unit and acceptance tests. It has meaningful names. It provides one way rather than many ways of doing one thing. It has minimal dependencies, which are explicitly defined, and provides a clear and minimal API. Code should be literate since depending on the language, not all necessary information can be expressed clearly in code alone.

### Smells of bad code.
Here are some smells that if you see in a code, you can tell that it’s a bad code.<br />
- **Redundant comments,** which comments which explain something obvious. You are writing code twice and forcing developers to read the code twice.  For example, this is a redundant comment:<br /> 
 `print("Final cost:" + total_cost) #Print final cost`<br />
The comment above is unnecessary and redundant.<br />
<img src="/image-assests/Wood.jpg" alt="" data-canonical-src="/image-assests/Wood.jpg" width="183" height="233" />

- **Position makers comments**
Some programmers use comments like the one below to mark a position in the source code or to gather a group of function together. They are unnecessary and should not be used; they make the source code destructed while it needs to be one piece of code that can be read like a poem.<br />
<img src="/image-assests/Poem.png" alt="" data-canonical-src="/image-assests/Poem.png" width="251" height="66" />

- **Commented-out code**
Commented out code decreases the readability of the code. Other programmers who work on the same program will have to read it even if it does not do anything in the program. It is ok to comment code temporarily to test and debug the program, but do not leave commented code in the source file.

## Conventions and style guide
This is a fork of PEP 8 -- Style Guide for Python Code. If anything is not mentioned here please refer to the pep document:<br />https://www.python.org/dev/peps/pep-0008/
### Indentation
- Use 4 spaces per indentation level.
- Spaces are the preferred indentation method.
- Tabs should be used solely to remain consistent with code that is already indented with tabs.
- Python 3 disallows mixing the use of tabs and spaces for indentation.

In your IDE, you should change the indentation method to 4 spaces.

When invoking the Python 2 command line interpreter with the `-t` option, it issues warnings about code that illegally mixes tabs and spaces. When using `-tt` these warnings become errors. These options are highly recommended!

### Maximum line length
Limit all lines to a maximum of 79 characters.
### Comments
Comments should be used only when necessary. Try to make the code self-explanatory instead of writing a comment when possible.
#### Do not use a comment when you can use a function or a variable.
Consider this code:
```
user_age = input("Input your age: ")
gender = input("Input your gender: ")

if user_age >= 18 and gender == "male": # Check if the person is an adult male
   print("An adult male")
```
Would not be better if we replace the comment with a function:
```
user_age = input("Input your age: ")
gender = input("Input your gender: ")

def isAdultMale(age, gender):
   return user_age >= 18 and gender == "male"

if isAdultMale(user_age, gender):
   print("An adult male")
```

#### Inline comments
An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.<br />
Inline comments are unnecessary and in fact, distracting if they state the obvious.<br />
Do not do this:<br />
<img src="/image-assests/inline.png" alt="" data-canonical-src="/image-assests/inline.png" width="398" height="48" />

#### Block Comments
Block comments generally apply to some (or all) code that follows them and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).<br />
Paragraphs inside a block comment are separated by a line containing a single #.

### Naming styles
There are different styles for writing names for variables, functions, and variables. You should use these each time you name something.

- Camel case: “myCar” (use it for functions names)
- Snake case: “my_car” (use it for variables names)
- Pascal case: “MyCar” (use it for classes names)

If a variable is going to store a boolean it should be started with “is_”. For example: “is_adult”.<br />
**Note:** Follow the naming conventions of the files you work on when you work on old files. Please keep the naming consistent.

### Names to Avoid
Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single-character variable names.

In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

### Strings quote
A string should be contained with double quotes (“). A substring (a string inside a string) should be contained in a single quote (‘),

## Defensive Programming
Defensive programming is the practice of writing software to enable continuous operation after and while experiencing unplanned issues. Defensive programming practices are often used where high availability, safety, or security is needed.

Defensive programming is an approach to improve software and source code.

When firmware knows there is an issue, and it likely knows what the issue is, but yet it doesn’t help solve the issue. The software was built with “Defensive Programming” practices in mind, which allows for the firmware to keep running even when incorrect behaviour occurs.

### Implementing defensive programming
- **Asserts** – keyword used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an Assertion Error.
<img src="/image-assests/Asserts.png" alt="" data-canonical-src="/image-assests/Asserts.png" width="291" height="172" />

- **Logging** – normally a log file that records events whilst the software is running.
<img src="/image-assests/Logging.png" alt="" data-canonical-src="/image-assests/Logging.png" width="219" height="188" />

- **Unit testing** – testing an individual unit or component functionality.

Python comes with the tools and libraries that support automated testing for your system.
