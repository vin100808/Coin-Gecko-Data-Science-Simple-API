# APIs and data collection in Python

## Introduction

This is a learning git repository for the course **Python Basics for Data Science** provided by edX.

## Tools

**JupyterLab** is used in this course constantly to allow students to practice. Think of it as a Notebook that is interactive, where student can write example codes and executes them at the same time without the need to download anything else. A very easy example would be trying to teach someone how to write/read a file, there are many different methods and usage, it is efficient and easy for learner to execute pre written or write on a code block on JupyterLab, and they could execute codes block by block.

## Projects

### Coin Gecko API

This example utilizes **pycoingecko** to retrive bitcoin data. Uses **pandas** to create a DataFrame instance, formats the Unix TimeStamp and Price at that time of the DataFrame, converts TimeStamp into readable time units, and group the data to find min, max, high, and low price of the day. Lastly, **plotly** helps to generate a candlestick plot for the DataFrame and creates an HTML file contains the plot.

Note:

- Need to be more familiar with how to manipulate data using **pandas** and **DataFrame** instances.
- Need to be more familiar with different kinds of plots/graphs and when to use them.
- For now focuses more on being familiar with these libraries rather than actually analyzing the data?

### Raptors Fan Club Member List

Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
Given the file `currentMem`, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the `exMem` file. Make sure that the format of the original files in preserved. (*Hint: Do this by reading/writing whole lines and ensuring the header remains* )
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the `cleanFiles` function.

### Text Analysis

You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

- Constructor (__init__) - This method should take the argument `text`, make it lower case, and remove all punctuation. Assume only the following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?). Assign this newly formatted text to a new attribute called `fmtText`.
- freqAll - This method should create and **return** dictionary of all unique words in the text, along with the number of times they occur in the text. Each key in the dictionary should be the unique word appearing in the text and the associated value should be the number of times it occurs in the text. Create this dictionary from the `fmtText` attribute.
- freqOf - This method should take a word as an argument and **return** the number of occurrences of that word in `fmtText`.

The skeleton code has been given to you. Docstrings can be ignored for the purpose of the exercise.
*Hint: Some useful functions are `replace()`, `lower()`, `split()`, `count()`*

