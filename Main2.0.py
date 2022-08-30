import pandas as pd
from datetime import date

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


def make_line():
    print("=" * 80)


def selection1():
    print('''
_   _    _    _     _____   __  __  ___  _   _ _____ _   _ 
| | | |  / \  | |   |  ___| |  \/  |/ _ \| \ | |_   _| | | |
| |_| | / _ \ | |   | |_    | |\/| | | | |  \| | | | | |_| |
|  _  |/ ___ \| |___|  _|   | |  | | |_| | |\  | | | |  _  |
|_| |_/_/   \_\_____|_|     |_|  |_|\___/|_| \_| |_| |_| |_|
    ''')
    make_line()
    whichMonth = input("Which half of the month? (1 = 1st, 2 = 2nd) >")
    daysWorked = input("How many days worked? >")
    make_line()

    sel1_pagIbig = pagIbig
    sel1_philHealth = philHealth
    sel1_sss = sss
    monthlyWage = 26 * wage  # CHANGE THIS MAGIC NUMBER

    if whichMonth == '1':
        sel1_philHealth = 0
        sel1_sss = 0
    if whichMonth == '2':
        sel1_pagIbig = 0
        sel1_philHealth = monthlyWage * 0.02

    totalWage = int(daysWorked) * wage


    # Find SSS Employee Contribution
    df = pd.read_excel('SSSTable.xlsx', usecols='A:D')
    i = 1
    while i < len(df):
        minRange = df.iloc[i, 0]
        maxRange = df.iloc[i, 1]

        if monthlyWage > minRange:
            if monthlyWage < maxRange:
                # print("Found Range at cell", i, "Between", minRange, "and", maxRange)
                # print("Employer Contribution is", df.iloc[i,2])
                # print("Employee Contribution is", df.iloc[i,3])
                sssEmployerContrib = df.iloc[i, 2]
                sssEmployeeContrib = df.iloc[i, 3]
                if whichMonth == '2':
                    sel1_sss = sssEmployeeContrib
        i += 1
    netWage = totalWage - sel1_philHealth - sel1_sss - sel1_pagIbig
    make_line()

    # FOR OUTPUT
    outputChoice = input("Do you want to save this output? (y/n)")
    if outputChoice == 'y':
        employeeName = input("Input Employee name for output: ")
    else:
        employeeName = 'N/A'

    print(f'''Payroll:
            Name: {employeeName}
            Gross Wage: {totalWage}

            less Philhealth: {sel1_philHealth} 
            less SSS: {sel1_sss} 
            less Pag Ibig: {sel1_pagIbig} 

            Net Wage: {netWage}''')
    make_line()
    outputDict = pd.DataFrame({employeeName: [totalWage, sel1_philHealth, sel1_sss, sel1_pagIbig, netWage]})
    outputDict.index = ['Total Wage', 'less Philhealth', 'less SSS', 'less Pag Ibig', 'Net Wage']

    if outputChoice == 'y':
        filename = f'2.0BBSalary_{date.today()}.xlsx'
        outputDict.to_excel('Output/'+filename)
        print(f'{filename} saved')


def selection2():
    # Compute for monthly Wage
    print('''
 __  __  ___  _   _ _____ _   _ _  __   __ __        ___    ____ _____ 
|  \/  |/ _ \| \ | |_   _| | | | | \ \ / / \ \      / / \  / ___| ____|
| |\/| | | | |  \| | | | | |_| | |  \ V /   \ \ /\ / / _ \| |  _|  _|  
| |  | | |_| | |\  | | | |  _  | |___| |     \ V  V / ___ \ |_| | |___ 
|_|  |_|\___/|_| \_| |_| |_| |_|_____|_|      \_/\_/_/   \_\____|_____|
''')
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
        minRange = df.iloc[i, 0]
        maxRange = df.iloc[i, 1]

        if monthlyWage > minRange:
            if monthlyWage < maxRange:
                # print("Found Range at cell", i, "Between", minRange, "and", maxRange)
                # print("Employer Contribution is", df.iloc[i,2])
                # print("Employee Contribution is", df.iloc[i,3])
                sssEmployerContrib = df.iloc[i, 2]
                sssEmployeeContrib = df.iloc[i, 3]
                sss = sssEmployeeContrib
        i += 1

    # print('=' * 80)
    # print(f''' Employee Stats:
    #         Daily Wage: {wage}
    #         Monthly Wage: {monthlyWage}
    #         Philhealth: {philHealth}
    #         SSS: {sss}
    #         Pag Ibig: {pagIbig}''')
    # print('=' * 80)

    netWage = monthlyWage - philHealth - sssEmployeeContrib - pagIbig
    make_line()
    print(f''' Monthly Payroll:
            Monthly Wage: {monthlyWage}

            less Philhealth: {philHealth}
            less SSS: {sssEmployeeContrib}
            less Pag Ibig: {pagIbig}

            Net Wage: {netWage}''')
    print('=' * 80)
    outputDict = pd.DataFrame({'0': [monthlyWage, philHealth, sssEmployeeContrib, pagIbig, netWage]})
    outputDict.index = ['Monthly Wage', 'less Philhealth', 'less SSS', 'less Pag Ibig', 'Net Wage']
    # print(outputDict)

def selection3():
    print('''
 ____ ____ ____    ____  _____ _____ _  __
/ ___/ ___/ ___|  / ___|| ____| ____| |/ /
\___ \___ \___ \  \___ \|  _| |  _| | ' / 
 ___) |__) |__) |  ___) | |___| |___| . \ 
|____/____/____/  |____/|_____|_____|_|\_
                                          
    ''')
    make_line()
    print("Find SSS Contribution")
    monthlyWage = int(input("Input monthly wage of employee: "))

    # Find SSS Employee Contribution
    df = pd.read_excel('SSSTable.xlsx', usecols='A:D')
    i = 1
    while i < len(df):
        minRange = df.iloc[i, 0]
        maxRange = df.iloc[i, 1]

        if monthlyWage > minRange:
            if monthlyWage < maxRange:
                # print("Found Range at cell", i, "Between", minRange, "and", maxRange)
                # print("Employer Contribution is", df.iloc[i,2])
                # print("Employee Contribution is", df.iloc[i,3])
                sssEmployerContrib = df.iloc[i, 2]
                sssEmployeeContrib = df.iloc[i, 3]
                sss = sssEmployeeContrib
        i += 1
    make_line()
    print(f'''SSS RESULTS:
        Employer Contribution: {sssEmployerContrib}
        Employee Contribution: {sssEmployeeContrib}
        Total Contribution: {sssEmployeeContrib + sssEmployerContrib}''')
    make_line()


def selection4():
    print('''
\ \      / / \  / ___| ____|  / ___/ _ \|  \/  |  _ \| | | |_   _| ____|
 \ \ /\ / / _ \| |  _|  _|   | |  | | | | |\/| | |_) | | | | | | |  _|  
  \ V  V / ___ \ |_| | |___  | |__| |_| | |  | |  __/| |_| | | | | |___ 
   \_/\_/_/   \_\____|_____|  \____\___/|_|  |_|_|    \___/  |_| |_____|
   ''')
    make_line()
    neWage = int(input("Input daily wage: "))
    neDaysWorked = int(input("Input days worked: "))
    neTotalWage = neWage * neDaysWorked
    print(f'''
Wage: {neWage}
Days Worked: {neDaysWorked}

Total Wage: {neTotalWage}
''')


# Set up defaults
philHealth = 0  # ER 2% if > 10000 wage, else 200
sss = 0
pagIbig = 100  # Always the case
wage = 533

make_line()
# ID : ['NAME', Wage, Philhealth, SSS, PagIbig] -- CURRENTLY NOT USED IN THIS VERSION
employeeDic = {
    '0': ['Janet Apostol', wage, philHealth, sss, pagIbig],
    '1': ['Rizalyn Repalda', wage, philHealth, sss, pagIbig]
}
print()

# Menu
print(f'''MENU:
    (1) Compute for half month payroll (PAYSLIP)
    (2) Compute for monthly payroll
    (3) Find SSS Contribution
    (4) Non Employee Wage Computation
    ''')
userchoice = input('Input menu selection: ')


if userchoice == '1':
    selection1()
elif userchoice == '2':
    selection2()
elif userchoice == '3':
    selection3()
elif userchoice == '4':
    selection4()
else:
    print('Not implemented yet')




