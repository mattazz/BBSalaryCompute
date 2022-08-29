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


def selection2():
    pass


# Set up defaults
philHealth = 0  # ER 2% if > 10000 wage, else 200
sss = 0
pagIbig = 100  # Always the case
wage = 533

# ID : ['NAME', Wage, Philhealth, SSS, PagIbig]
employeeDic = {
    '0': ['Janet Apostol', wage, philHealth, sss, pagIbig],
    '1': ['Rizalyn Repalda', wage, philHealth, sss, pagIbig]
}
print()

# Menu
print(f'''MENU:
    (1) Compute for half month payroll
    (2) Compute for monthly payroll
    ''')
userchoice = input('Input menu selection: ')

if userchoice == '2':
    # Compute for monthly Wage
    daysWorked = int(input('How many days worked?: '))
    monthlyWage = daysWorked * wage

    # Calculate for Philhealth
    if monthlyWage < 10000:
        philHealth = 200
    else:
        philHealth = round(monthlyWage * 0.02, 2)

    # Find SSS Employee Contribution
    df = pd.read_excel('SSSTable.xlsx', usecols='A:D')
    i = 1
    while i < len(df):
        minRange = df.iloc[i,0]
        maxRange = df.iloc[i,1]

        if monthlyWage > minRange:
            if monthlyWage < maxRange:
                # print("Found Range at cell", i, "Between", minRange, "and", maxRange)
                # print("Employer Contribution is", df.iloc[i,2])
                # print("Employee Contribution is", df.iloc[i,3])
                sssEmployerContrib = df.iloc[i,2]
                sssEmployeeContrib = df.iloc[i,3]
                sss = int(sssEmployeeContrib)
        i += 1
    print('=' * 80)
    print(f''' Employee Stats: 
        Daily Wage: {wage}
        Monthly Wage: {monthlyWage}
        Philhealth: {philHealth}
        SSS: {sss}
        Pag Ibig: {pagIbig}''')
    print('=' * 80)

    netWage = monthlyWage - philHealth - sssEmployeeContrib - pagIbig

    print(f''' Monthly Payroll:
        Monthly Wage: {monthlyWage}
        
        less Philhealth: {philHealth}
        less SSS: {sssEmployeeContrib}
        less Pag Ibig: {pagIbig}
        
        Net Wage: {netWage}''')
    print('=' * 80)
else:
    print('Not implemented yet')



