#######################################################################################################################################
# ENGR 315
# Assignement 2 
# Drew Cutright
# Due: 11-6-2026
# 
# Notes: This assignement was used to demonstrate my ability to calculate statistical 
# analyses on RSI data from an accelerometer and a force plate sensor. 
#
#######################################################################################################################################

# import packages
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import os

########################
######## Task 1 ########
########################

# Print the task name to the terminal
print('\n')
print('Task 1')

# Define a variable as the location of the all_participant_data_rsi.csv file
data_location = 'data/drop-jump/all_participant_data_rsi.csv'

# Check that the data_location statement calls csv file
for iteration in range(3):

    # if it doesn't, then we add a delimeter
    if os.path.exists(data_location) == False:
        data_locaiton = '../' + data_location 
    else:
        # if the path exists, we print to the end user that the file does exist
        print('File location exists')
        print('\n')
        break

# Import data from data_location
all_participant_df = pd.read_csv(data_location)

# Create seperate arrays for acceleration and force plate data
array_acceleration = all_participant_df['accelerometer_rsi'].to_numpy()
array_force_plate = all_participant_df['force_plate_rsi'].to_numpy()

# Compute t-test between arrays
t_value, p_value_acc_fp = stats.ttest_ind(array_acceleration, array_force_plate)

# Print p value
print("T-test P-Value = ",p_value_acc_fp)

# Print t value
print("T-test T-Value = ",t_value,'\n')

# State null hypothesis 
print("Null Hypothesis: There is significant statistical difference between the data from the accelerometer sensor and the force plate" \
" sensor.", '\n')

# state alternative hypothesis
print("Alternative Hypothesis: There is no significant statistical difference between the data from " \
"the accelerometer sensor and the force plate sensor, and we can conclude that the data samples are relatively equivalent.",'\n')

# Define and state alpha
alpha = 0.05
print("We define alpha as",alpha)

# State if null hypothesis can be rejected
if p_value_acc_fp < alpha:
    print("We reject the null-hypothesis.",'\n')
else:
    print("We fail to reject the null-hypothesis.",'\n')


########################
######## Task 2 ########
########################

# Print the task name to the terminal
print('Task 2')

# Fit the accelerometer data to a normal distribution
mu, std = stats.norm.fit(array_acceleration)

# Find the number of data points in the accelerometer data
number_of_samples = len(array_acceleration)

print("Fitted Mean:",mu)
print("Fitted Standard Deviation:",std,'\n')

# Chi-squared test

# Get the observed data

# Define a number of bins for the histogram
num_bins = 25
# Get the bin edges, by using the maximum and minimum of the accelerometer data. 
# We add 1 to the number of bins, because there are always 1 more edge than bins.
bin_edges = np.linspace(start=array_acceleration.min(), stop=array_acceleration.max(), num=num_bins + 1)

# Calculate Observed Counts per bin
observed_data, _ = np.histogram(array_acceleration, bins=bin_edges)

# Calculate Expected Counts using the mean and std

# We use the Cumulative Distribution Function to find the probability of a point falling in each bin
cdf_values = stats.norm.cdf(bin_edges, loc=mu, scale=std)

# Probability per bin is the difference between the upper edge CDF and lower edge CDF
bin_probabilities = np.diff(cdf_values)

# We normalize the probabilities so they sum up to 1. This lets us include all of the points in the distribution.
bin_probabilities /= bin_probabilities.sum()

# Now we can calculate the expected data points using the probabilities and the number of samples.
expected_data = number_of_samples * bin_probabilities

# We conduct the chi squared test on observed and expected data
chi2_stat, p_val = stats.chisquare(f_obs=observed_data, f_exp=expected_data)

# Print analysis to the terminal
print('Chi-squared analysis:')
print('chi-squared stat =', chi2_stat)
print('p-value =', p_val)
print('\n')

# For a given p value, we either print that the normal distribution is or is not a good fit for the RSI data.
if p_val < 0.05:
    print("Since the p-value is smaller than alpha, we have determined that the normal distribution is a good fit for the accelerometer data.", '\n')
else:
    print("Since the p-value is greater than alpha, we have determined that the normal distribution is not a good fit for the accelerometer data.", '\n')

# Plot histogram and normal distribution
plt.hist(array_acceleration, bins=bin_edges, density=True, color='purple', edgecolor = 'black', alpha=0.5, label='Observed Data')

# We need to get lots of x points to create a line for the nomral distribution. We do this using linspace
# and use the max and min of the RSI data. 
x = np.linspace(array_acceleration.min(), array_acceleration.max(), 500)

# We can then plot the normal fit.
plt.plot(x, stats.norm.pdf(x, loc=mu, scale=std),
         color='black', label=f'Normal Dist (μ={mu:.2f}, σ={std:.2f})')

# Other various plot components
plt.title('Normal Distribution Fit on Accelerometer RSI Data')
plt.xlabel('RSI')
plt.ylabel('Density')
plt.legend()
plt.show()


########################
######## Task 3 ########
########################

# print the task name to the terminal
print('Task 3')

# This section we will pull out participant F's data into a seperate data frame, and complete
# a statistical analysis on it.

# Pre-define a variable as the F_trial_index. This is to be iterated through to consolidate all "F" rows
# into a single data frame.
F_trail = 'F_trial_'

# There are 10 trials for Character F, but we start at 1 so the stop needs 11.
for i in range(1, 11):

    # Name of the trial is F_trial_#, where the # ranges 1 through 10. This loop iterates through each trial and appends 
    # the data to a seperate data frame.

    # Renames the row string
    Trial_num = f'{F_trail}{i}'

    # We can't "append" a new row to a data frame that doesn't exist, so the first row is the start of the data frame.
    if i == 1:
        Character_F_df = all_participant_df[all_participant_df.iloc[:, 0] == Trial_num]

    # Now that the df exists, we can start appending the new row to the whole df.
    else:
        new_row = all_participant_df[all_participant_df.iloc[:, 0] == Trial_num]
        Character_F_df = pd.concat([Character_F_df, new_row], ignore_index=True)

# Now that the data frame has been constructed, we can print it to the terminal.
print(Character_F_df)

# Calculate confidence intervals

# We predefine the results array and the confidence interval value.
results = {}
confidence = 0.95

# This loop computes the mean, upper, and lower confidence intervales for both the acceleration
for col in ['force_plate_rsi', 'accelerometer_rsi']:
  
    # We pull out the data for one of the two columns
    column_data = Character_F_df[col]

    # We find the length, mean, and standard deviation of the column
    n = len(column_data)                # Number of rows
    mu = np.mean(column_data)           # Mean of the column
    std_err = stats.sem(column_data)    # Standard error function

    # The margin of error is the standard eror times the percent point function
    margin_of_error = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)

    # This creates a dictionary of the column, which we can turn into a data frame.
    results[col] = {
      "Mean": mu,
      "Lower_CI": mu - margin_of_error,
      "Upper_CI": mu + margin_of_error,

  }

# Convert the dictionary to a data frame so that printing is clear
results_df = pd.DataFrame(results)

# Print the data frame of confidence interval results
print('\n')
print(results_df)
print('\n')
