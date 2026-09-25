"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###

# Equations: 
# final = principal * ((1 + (rate / 100)) ** n)

# Vars
Elon_invest = 33000000000
Rate_10yr = 3.96
Rate_20yr = 4.32
Year_10 = 10
Year_20 = 20

# Calculations

ten_year_final = Elon_invest * ((1 + (Rate_10yr / 100)) ** Year_10)
print(ten_year_final)

twenty_year_final = Elon_invest * ((1 + (Rate_20yr / 100)) ** Year_20)
print(twenty_year_final)

