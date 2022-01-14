# Python Coding Standard
*T level students 2021/2022*<br />

**Contents**<br />
1. [Introduction](TLEVEL-2021-22-CodingStandards.md#introduction)<br />
2. [Clean Code](TLEVEL-2021-22-CodingStandards.md#clean-code)<br />
   - [Implications of having a bad code](TLEVEL-2021-22-CodingStandards.md#implications-of-having-a-bad-code)<br />
   - [What is a clean code?](TLEVEL-2021-22-CodingStandards.md#what-is-a-clean-code)<br />
   - [Smells of bad code](TLEVEL-2021-22-CodingStandards.md#smells-of-bad-code)<br />
3. [Conventions and style guide](TLEVEL-2021-22-CodingStandards.md#conventions-and-style-guide)<br />
4. [Defensive Programming](TLEVEL-2021-22-CodingStandards.md#defensive-programming)<br />

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
-**Redundant comments,** which comments which explain something obvious. You are writing code twice and forcing developers to read the code twice.  For example, this is a redundant comment:<br /> 
 `print("Final cost:" + total_cost) #Print final cost`<br />
The comment above is unnecessary and redundant.<br />
<img src="/image-assests/Wood.jpg" alt="" data-canonical-src="/image-assests/Wood.jpg" width="183" height="233" />

-**Position makers comments**
Some programmers use comments like the one below to mark a position in the source code or to gather a group of function together. They are unnecessary and should not be used; they make the source code destructed while it needs to be one piece of code that can be read like a poem.<br />
<img src="/image-assests/Poem.png" alt="" data-canonical-src="/image-assests/Poem.png" width="167" height="44" />


## Conventions and style guide
### Indentation
### Maximum line length
### Comments
#### Do not use a comment when you can use a function or a variable.
#### Inline comments
#### Block Comments
### Naming styles
### Names to Avoid
### Strings quote

## Defensive Programming
### Implementing defensive programming
