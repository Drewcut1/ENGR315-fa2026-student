import sys
import os
import math
import numpy as np

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

# Questions from Canvas:
"""
1A) When was the first positive COVID case in Harrisonburg? 
    Plan: create a for loop that finds where column 3 in harrisonbug is = to 1, return index

1B) When was the first positive case in Rockingham County?
    Plan: create a for loop that finds where column 3 in Rockingham county is = to 1, return index

2A) On what date was the greatest number of new cases reported in Harrisonburg? 
    Plan: Find the maximum of column 3 in Harrisonburg.

2B) What date in Rockingham County?
    Plan: Find the maximum of column 3 in Rockingham County.

3A) What was the worst seven-day period in Harrisonburg city for new COVID cases? 
    Plan: Read the file for 7 rows in a for loop, find the amount of new cases of that seven days, 
    create a new "MAX Cases" variable, check if MAX Cases is larger than the previous 7 days, 
    if it is then define it as the new MAX Cases and record the index, print the recorded index and add 6 to
    to the last day.

3B) What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal. 
    Same plan as 3B

"""

### Parsing Data from covid folder

# Defining relative paths in variables
relative_path_us = "data/covid/us-counties.csv"

# Checking that paths return proper files
# If files do not exist, then we add ../ to move up a file depending on the end user's working 
# directory location. Three iterations should be sufficient.

for index in range(2): 

    # Checks path's existance
    if os.path.exists(relative_path_us) == True:
        print("\n", "Files Exist")                  
        break
    else:
        # This adds a parent directory shortcut to the variable
        relative_path_us = "../" + relative_path_us

# Put COVDID data into a list, then an array 
data_us = np.array(parse_nyt_data(relative_path_us))

### Sort through data to find only Harrisonburg and Rockingham County File entries
# Creating array of headers
headers = ["date","county", "state", "fips", "cases", "deaths"]

# Harrisonburg Data
Hburg_fips = "51660"
Hburg_data = data_us[data_us[:, 3] == Hburg_fips]   # Index which contains appropriate fips value returns
                                                    # data for specific region

# Rockingham County Data
Rcounty_fips = "51165"
Rcounty_data = data_us[data_us[:, 3] == Rcounty_fips] 

################################################################################################################
### Question 1 Code

# Create varibles for storing indecies of cases
Hburg_first_case_index = None
Rcounty_first_case_index = None

# Harisonburg for-loop to find first COVID case
index = 0

for index in range(Hburg_data.shape[0]):    # .shape[0] produces the array row count, which will used to iterate 
                                            # through the data
    if Hburg_data[index, 4] == 1:           # We are looking for the first case, which is the value one

        Hburg_first_case_index == index     # Records the first index
        break                               # Stops the loop so that we don't count "1" again

# Put the store the array in a new array
Hburg_first_case_text = Hburg_data[Hburg_first_case_index, 0, 0]    # Produces the array at the index, then the row, 
                                                                    # then the collumn, which relays the date.

# Print values to the terminal
print(end="\n")                                 # Gives some space to the output for readability
print("Question 1A")
print("The first case that appeared in Harrisonburg was on")
print(Hburg_first_case_text[0]) # pulls the text from the array 


# Rockingham County for-loop to find first COVID case
# This works the same way the previous for loop does, only the variable names were changed

for index in range(Rcounty_data.shape[0]):

    if Rcounty_data[index, 4] == 1:

        Rcounty_first_case_index == index

# Put the store the array in a new array so that we can access the text
Rcounty_first_case_text = Rcounty_data[Rcounty_first_case_index, 0, 0] # Produces the array at the index, then the row, then the collumn, which relays the date.

print(end="\n")                                 # Gives some space between outputs for readability
print("Question 1B")
print("The first case that appeared in Rockingham County was on")
print(Rcounty_first_case_text[0]) # pulls the text from the array 

################################################################################################################
### Question 2 
# Create an array of new cases. A loop will be iterated through and every new row will be subtracted by the previous row. The 
# differences between these are the new (also reduced) cases. The index at max of these arrays will output the index for the date at the max
# number of new cases.

# Create lists for only "cases" to improve computational speed
Hburg_cases = [int(x) for x in Hburg_data[:, 4]]                    # Copies "cases" data from larger array to an integer filled list
Hburg_new_cases = list([Hburg_cases[0]])                            # Provides emmty array for new HB cases
Rcounty_cases = [int(x) for x in Rcounty_data[:, 4]]                # Copies "cases" data from larger array
Rcounty_new_cases = list([Rcounty_cases[0]])                        # Provides emmty array for new RC cases

# Reset index
index = 0
# Vector for storing zero
nada_vector = 0

### Question 2A
# Loop which calculates the new cases
for index in range(1, len(Hburg_cases)): 

    if int(Hburg_cases[index]) == int(Hburg_cases[index-1]):                # Checks if the indecies are equivilant
        Hburg_new_cases.append(nada_vector)                                 # Adds zero to the list
    else:     
        Hburg_new_cases.append(Hburg_cases[index] - Hburg_cases[index - 1]) # Otherwise, subtracts new row from old row

# Finds the max of the list containing new cases        
Hburg_max = max(Hburg_new_cases)

# Finds the column of the max
Hburg_max_index = Hburg_new_cases.index(Hburg_max)

# Records the date at which the max appeared
Hburg_max_date = Hburg_data[Hburg_max_index, 0]

# Prints maximum new cases and date of new
print(end="\n")
print("Question 2A")
print("The max number of new cases in Harisonburg was")
print(Hburg_max)
print("which was on")
print(Hburg_max_date)

### Question 2B
# Loop which calculates the new cases
for index in range(1, len(Rcounty_cases)): 

    if int(Rcounty_cases[index]) == int(Rcounty_cases[index-1]):                    # Checks if the indecies are equivilant
        Rcounty_new_cases.append(nada_vector)                                       # Adds zero to the list
    else:     
        Rcounty_new_cases.append(Rcounty_cases[index] - Rcounty_cases[index - 1])   # Otherwise, subtracts new row from old row

# Finds the max of the list containing new cases        
Rcounty_max = max(Rcounty_new_cases)

# Finds the column of the max
Rcounty_max_index = Rcounty_new_cases.index(Rcounty_max)

# Records the date at which the max appeared
Rcounty_max_date = Hburg_data[Rcounty_max_index, 0]

# Prints maximum new cases and date of new
print(end="\n")
print("Qustion 2B")
print("The max number of new cases in Rockingham County was")
print(Rcounty_max)
print("which was on")
print(Rcounty_max_date)

##############################################################################################################
### Question 3 ###

# Find the week (set of seven days) which had the most number of new cases
# We already have the set of new cases. Now for every iteration, the value at the iteration index plus the 6
# iterations after will be the total for the week. The max of that list determines the worst week.

### Question 3A

# Create new lists to find week maxs
Hburg_week_totals = []
Rcounty_week_totals = []

# Reset index
index = 0

# Loop that finds the total of that week (set of seven days)
for index in range(len(Hburg_new_cases)-6): # minus six to stop at the last week

    day1 = Hburg_new_cases[index]               # I chose to write each iteration out explicetly because for-loops within for-loops are
    day2 = Hburg_new_cases[index + 1]           # hard to read and can get confusing.
    day3 = Hburg_new_cases[index + 2]           # This method ensures that each variable is overwritten.
    day4 = Hburg_new_cases[index + 3]
    day5 = Hburg_new_cases[index + 4]
    day6 = Hburg_new_cases[index + 5]
    day7 = Hburg_new_cases[index + 6]
    summation = day1 + day2 + day3 + day4 + day5 + day6 + day7      # After all new cases are found, they are added together to 
    Hburg_week_totals.append(summation)                             # find the total of the week

# Post processing week totals, max, index, and dates
Hburg_max_week_totals = max(Hburg_week_totals)      # Finds maximum of the totals
Hburg_max_week_totals_index = Hburg_week_totals.index(Hburg_max_week_totals)        # Finds the index of the max
Hburg_max_week_totals_date1 = Hburg_data[Hburg_max_week_totals_index, 0]            # Start day of the week
Hburg_max_week_totals_date2 = Hburg_data[Hburg_max_week_totals_index + 6, 0]        # Last day of the week

# Print out answers
print(end="\n")
print("Qustion 3B")
print("The worst week in Harrisonburg was the")
print(Hburg_max_week_totals_date1, "through the", Hburg_max_week_totals_date2)
print("with a total of", Hburg_max_week_totals, "new COVID-19 cases.")

### Question 3B

# Reset index
index = 0

# Loop that finds the total of that week (set of seven days)
for index in range(len(Rcounty_new_cases)-6): # minus six to stop at the last week

    day1 = Rcounty_new_cases[index]         #  I chose to write each iteration out explicetly because for-loops within for-loops are
    day2 = Rcounty_new_cases[index + 1]     # hard to read and can get confusing.  
    day3 = Rcounty_new_cases[index + 2]     # This method ensures that each variable is overwritten.
    day4 = Rcounty_new_cases[index + 3]
    day5 = Rcounty_new_cases[index + 4]
    day6 = Rcounty_new_cases[index + 5]
    day7 = Rcounty_new_cases[index + 6]
    summation = day1 + day2 + day3 + day4 + day5 + day6 + day7
    Rcounty_week_totals.append(summation)

# Calculate max, index, and dates of weeks
Rcounty_max_week_totals = max(Rcounty_week_totals)                                     # Finds max of set
Rcounty_max_week_totals_index = Rcounty_week_totals.index(Rcounty_max_week_totals)     # Finds index of the set
Rcounty_max_week_totals_date1 = Rcounty_data[Rcounty_max_week_totals_index, 0]         # Finds first day of the bad week
Rcounty_max_week_totals_date2 = Rcounty_data[Rcounty_max_week_totals_index + 6, 0]     # Finds last day of the bad week

# Print out answers to the terminal
print(end="\n")
print("Qustion 3A")
print("The worst week in Rockingham County was the")
print(Rcounty_max_week_totals_date1, "through the", Rcounty_max_week_totals_date2)
print("with a total of", Rcounty_max_week_totals, "new COVID-19 cases.")
print(end="\n")



