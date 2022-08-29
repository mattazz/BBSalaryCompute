import pandas as pd
import openpyxl
from datetime import date
from os.path import exists
import numpy

print('''
 ____        _                   ____                            _
/ ___|  __ _| | __ _ _ __ _   _ / ___|___  _ __ ___  _ __  _   _| |_ ___
\___ \ / _` | |/ _` | '__| | | | |   / _ \| '_ ` _ \| '_ \| | | | __/ _ 
 ___) | (_| | | (_| | |  | |_| | |__| (_) | | | | | | |_) | |_| | ||  __/
|____/ \__,_|_|\__,_|_|   \__, |\____\___/|_| |_| |_| .__/ \__,_|\__\___|

Bang Bang Salary computation with deductions for net pay slip generation
V0.2
@Mattazz
''')

# Set up defaults
philHealth = 0 # ER 2% if > 10000 wage, else 200
sss = 0
pagIbig = 100 # Always the case
wage = 533

# ID : ['NAME', Wage, Philhealth, SSS, PagIbig]
employeeDic = {
    '0': ['Janet Apostol', wage, philHealth, sss, pagIbig],
    '1': ['Rizalyn Repalda', wage, philHealth, sss, pagIbig]
}
print()

# Compute for monthly Wage
daysWorked = int(input('How many days worked?: '))
monthlyWage = daysWorked * wage

# Calculate for Philhealth
if monthlyWage < 10000:
    philHealth = 200
else:
    philHealth = round(monthlyWage * 0.02, 2)


print(f''' Employee Stats: 
    Daily Wage: {wage}
    Monthly Wage: {monthlyWage}
    Philhealth: {philHealth}
    SSS: {sss}
    Pag Ibig: {pagIbig}
    ''')
