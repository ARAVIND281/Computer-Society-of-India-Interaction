# Question

Python Grep Implementation

The goal of this task is to implement a simplified version of the grep command-line utility in Python. The task is to create a Python script that replicates as many features of the standard grep command as possible.

grep is a powerful command-line tool used for searching text patterns within files. It supports various options and regular expressions for efficient and flexible text searching.

Requirements: Participants are expected to implement as many features as possible from the grep man page(page which helps to understand the usage of a particular tool). Some of grep's features are listed below but you are free to implement more:

Basic Text Search:

Implement the ability to search for a specified pattern within a given file.
Allow for searching in multiple files (if specified).
Regular Expressions:

Support basic regular expressions for more advanced pattern matching.
Case Sensitivity:

Implement the option to perform case-sensitive or case-insensitive searches.
Output Formatting:

Display the matching lines along with the line numbers.
Provide an option to display only the count of matching lines.
File Inclusion/Exclusion:

Allow specifying files to include or exclude from the search using wildcards or regular expressions.
Recursive Search:

Provide an option for recursive searching through directories.
Context Lines:

Implement the ability to display a specified number of lines before and after each matching line.
Invert Match:

Support the ability to invert the match, displaying lines that do not match the specified pattern.
Word Match:

Allow for searching only whole words.
Colorized Output:

Implement the option to display matching text in color for improved visibility.
Evaluation Criteria: Submissions will be evaluated based on the following criteria:

Correctness and accuracy of the implemented features.
Code readability, organization, and adherence to best practices.
Creativity in handling edge cases and error scenarios.
Efficiency and performance of the implementation.
Documentation quality and completeness.

# HOW TO USE

Save the script as pygrep.py, and run it from the command line. For example, to search for the word "example" in all .txt files in the current directory, ignoring case, and displaying the count of matching lines, you could use:

python pygrep.py -i -c example *.txt

To extend this script, you could add more complex regular expression handling, file inclusion/exclusion logic, and more sophisticated output formatting. Remember, this script is a basic starting point and might need adjustments to match the full power and flexibility of the grep utility.
