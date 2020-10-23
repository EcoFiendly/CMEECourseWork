# Week 2

*Author: Yewshen Lim*

*Created: Week 2*

This directory contains the scripts, data and results from week 2.

Languages used in this week:
1. Python

Requirements:
1. Python 3

## Scripts

Scripts are separated into two sections, personal and groupwork

## Personal

### 1. `basic_io1.py`

Script illustrates basic input

### 2. `basic_io2.py`

Script illustrates basic output

### 3. `basic_io3.py`

Script illustrates basic storage of objects

### 4. `basic_csv.py`

Script illustates the manipulation of csv files

### 5. `cfexercises1.py`

Control flow exercise 1, modified into a module

### 6. `loops.py`

Script illustrates for and while loops

### 7. `cfexercises2.py`

Script illustrates loops and conditionals combined

### 8. `oaks.py`

Script finds just taxa that are oak trees from a list of species using both loops and list comprehension

### 9. `scope.py`

Script illustrates variable scope, local and global. Variables inside functions arn invisible outside of it, nor do they persist once the function has run. These are called local variables, and are only accessible inside their function. However, "global variables" are visible inside and outside of functions.

### 10. `boilerplate.py`

Script contains sections of code that have to be included in many places with little or no alteration.

### 11. `using_name.py`

Script illustrates '__name__ == "__main__"'. This line directs the python interpreter to set the special __name__ variable to have a value "__main__", so that the file is usable as a script as well as an importable module. On the other hand, if some other module is the main program and your module is being imported, the interpreter looks at the filename of your module, strips off the .py and assigns that string to the module's __name__ variable instead and skips the command(s) under the if statement.

### 12. `sysargv.py`

Script showing argv is the 'argument variable'. Such variables are necessarily very common across programming languages, and play an important role - argv is a variable that holds the arguments passed to the script when it's ran.

### 13. `control_flow.py`

Script shows some functions exemplifying the use of control statements

### 14. `lc1.py`

Script uses loops and list comprehension to create three different sets of lists each, containing the latin names, common names and mean body masses for each species in the given tuple.

### 15. `lc2.py`

Script uses list comprehension and loops to create (1) lists of month and rainfall tuples where the amount of rain was greater than 100 mm, (2) list of just month names where the amount of rain was less than 50 mm.

### 16. `dictionary.py`

Script populates a dictionary called taxa_dic derived from taxa so that it order names to set of taxa.

### 17. `tuple.py`

Script prints latin name, common name and mass on separate lines or output block by species from a tuple.

### 18. `test_control_flow.py`

Some functions exemplifying the use of control statements

### 19. `debugme.py`

Example of debugging on a script

### 20. `align_seqs.py`

Script takes DNA sequences as input from a single external file and aligns two DNA sequences such that they are as similar as possible. The best alignment, along with its corresponding score is then saved in a text file to the /Results/ directory.
Also for practicing debugging via insertion of breakpoints.

Script starts by positioning the beginning of the shorter sequence at all positions (bases) of the longer one (the start position), and count the number of bases matched. The alignment with the highest score wins. Ties are possible, in which case, an arbitrary alignment (e.g. first or last) with the highest score is taken.

### 21. `oaks_debugme.py`

Debug practice, where the bug prevents oaks from being found. Debug by writing doctests.

## Groupwork

### 1. `align_seqs_fasta.py`

Improvement to align_seqs.py, where this script should take any two fasta sequences (in separate files) to be aligned as input. Would typically run using explicit inputs, but should still run if no inputs were given, using two fasta sequences from the /Data/ directory as defaults.

### 2. `align_seqs_better.py`

Improvement to align_seqs_fasta.py, where this script keeps multiple alignments if they equal in score to the best score. Outputs are saved to the /Results/ directory.

### 3. `oaks_debugme.py` (Same file as the above, no. 21)