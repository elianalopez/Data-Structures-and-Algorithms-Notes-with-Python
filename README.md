<br />
 <p align="center">
    <img src="https://github.com/elianalopez/Data-Structures-and-Algorithms-Notes-with-Python/blob/main/Images/DS%26ANotes.png" width="400" height="263">
    <h1 align="center">📝 Data Structures and Algorithms Notes with Python</h1>
    <p align="center" class="h6">By Eliana Lopez</p>
This repository contains a deep dive on Data Structures and Algorithms theory and concepts along with Python based examples of many popular algorithms and data structures.


<!-- TABLE OF CONTENTS -->
## Table of Contents  
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>click to expand</summary>
 
- [Introduction and the Basics](#Introduction-and-the-Basics)  
- [Time & Space Complexity](#Time--Space-Complexity)
</details>
<!-- AUTO-GENERATED-CONTENT:END -->


## Introduction and the Basics
For this introduction I am going to define key terms so we can do into more depth about the applications and uses of data structures and algorithms.
These will be the key terms defined in this section:
* Data Types
* Abstract Data Types
* Algorithm
* Data Structure

### Data Types
Data types are important because they illustrate the kind of value in the variable and tells us what operations can be performed on any particular data. Down below is an intuitive definition  of what a data type is:

* An attribute of data that informs the interpreter on how to classify the variable. 

In Python there are four categories of data types: *numeric, sequential, Booleans, and dictionary* 
I have created a diagram of these categories of data types along with their respective data types down below.

<p align="center"><img src="https://github.com/elianalopez/Data-Structures-and-Algorithms-Notes-with-Python/blob/main/Images/DataTypes.PNG" width="85%" height="85%"></p>

### What is an Abstract Data Types (ADT)?

For me, I like to think of an abstract data type as a thought process of the rules and operations of data, there is no concrete implementation, but just thoughts and ideas on how this process might work.

* A logical process on how we view data and allowed operations without the regard on how it will be implemented.

Note: An ADT is the *what it does.*

### What is an Algorithm?
Overall this is the most intuitive definition  of an algorithm:

* A set of instructions used to solved a problem
 
Outside of computing, one example of an algorithm can be a recipe from a cookbook to craft a meal. Where we follow a certain set of instruction from the cook book to create our meal, which would thus solve the problem of our hunger. 

### What is a Data Structure?

The *implementation of an abstract data type* can be referred to a data structure but intuitively is a way of organizing data so it can be used effectively.

* A data structure is a format for accessing, storing, organizing, or structuring data.

Overall it is a technique of how data can inter-relate to each other logically or mathematically, or in layman's terms *how it does it.*

**The Connection between Data Structures and Abstract Data Types:**

**ADT gives us the blue print while a data structure tells us how to implement it**

### The Interconnection between Data Structures and Algorithms
To put it simply, data structures need algorithms and algorithms need data structures.

**The connection between algorithms and data structures is that an algorithm processes data and that data is then stored into a data structure.**

This is an illustration of the interconnection of a data structure and an algorithm:
<p align="center"><img src="https://github.com/elianalopez/Data-Structures-and-Algorithms-Notes-with-Python/blob/main/Images/Example.PNG" width="480" height="150"></p>

## Time & Space Complexity 

Often, there is more than one way to solve the same problem with different programs. So how would you be able to compare the performance of different algorithms, *is one program better than the other?*

Well the answer to that question is quite simple, you have to see *which program is more efficient*. 

There are two ways to determine which algorithm is more efficient:
* The amount of space or memory an algorithm requires
* The amount of time an algorithm requires to execute

Overall time and space complexity can be impacted from several factors such as hardware, operating system.

### Time Complexity
The time complexity is the amount of time an algorithm takes to complete its process, and this time is usually measured by the input n, in order to compare its efficiency with other algorithms. 

There are three types of asymptotic notations utilized to illustrate the run time complexity:
**Big O - O(n)**
* Worst Case
* Upperbound
* Slowest runtime
**Big Theta - Θ(n)**
* Average Case
* Average runtime
* Tight Bound of function complexity
**Big Omega - Ω(n)**
* Best Case
* Fastest runtime
* Lowerbound


#### Big-O
Big-O notation is utilized to describe the performance or complexity of an algorithm, it does with by its tail behavior (see the graph below). Big-O is typically described as the worst case scenario because the more complex your algorithm, along with large amounts of data, the longer it will take to operate with time. 
When thinking about Big-O, ask yourself this question, *how does an algorithm speed scale when the input scale become **very large**?*

What is the n of O(n)?
* The parameter 𝑛 is often referred to as *the size of the problem*

#### Common Functions for Big-O
* O(1) - *Constant Time*
<br> As an algorithm gets *very very* large, the run time of the algorithm would remain the same. If you notice from the graph below, the O(1) function remains constant as input gets bigger and bigger down the x-axis.
* O(log(n)) - *Logarithmic Time*
<br> The run time shapes into any typical log function, so as an algorithm gets *very very* large, this will lead to a small increase in log(n).
* O(n) - *Linear Time*
<br> The algorithm will take on the order of n operations to insert an item, so it is in proportion to the input size. 
* O(nlog(n)) - *Logarithmic Linear Time*
<br> The algorithm is *doing log(n) work n times* which is where multiplication comes in place. 
* O(n²) - *Quadratic Time*
<br> The algorithm is proportionally the squared number of inputs.
* O(2^n) - *Exponential Time*
<br> The algorithm is growths a constant amount of time, (in this case doubles) within each addition of input n.
* O(n!) - *Factorial Time*
<br> Any algorithm that calculates all permutation of a given array is O(N!).

<p align="center"><img src="https://github.com/elianalopez/Data-Structures-and-Algorithms-Notes-with-Python/blob/main/Images/Big-O.PNG" width="500" height="400"></p>

**Note for Big-O** 
As seen in the graph above you can notice that Big-O gives us a tight-upperbound to functions.

**Note for O(log(n)):**
Normally logarithmic are typically base 2. One thing to think about while looking at a log is, *what must I power my base (of 2) by to get n.* Example on how to solve this problem is down below. 
<p align="center"><img src="https://github.com/elianalopez/Data-Structures-and-Algorithms-Notes-with-Python/blob/main/Images/log.PNG" width="270" height="50"></p>


### Space Complexity

When determining space complexity, you have to ask, *how does the space usage of our algorithm change as input becomes larger?* An alternative question you can ask is, *How much memory, in a worse case scenario, is needed?*

* Space complexity includes both *auxiliary space* (temporary space) and used space

Similar to time complexity, space complexity can also be expressed using Big-O notation, such as O(n), O(nlog(n)), O(n²).

*What space does your program create?*
* *does it create a single array of n-elements?*
* *does it create log(n) elements?*
* *ect...*

*Note: Runtime stack is a part of space complexity* 

### Optimizing Time or Optimizing Space?
If we had to choose between either optimizing time or optimizing space. 
Overall, it depends on your needs, but in a production setting, optimizing time is the main priority because **we can buy memory, but we can't buy time!**
This can lead to the best trade off of both increasing the space and lowering the time!
