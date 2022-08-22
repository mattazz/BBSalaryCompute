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
V0.1
@Mattazz
''')

# ID : ['NAME', Wage, Philhealth, SSS, PagIbig]
employeeDic = {
    '0': ['Janet Apostol', 533, 277.16, 600, 100],
    '1': ['Rizalyn Repalda', 533, 277.16, 600, 100]
}
print()
# Input getting data of girls
print('''Which employee:
    (0) Janet Apostol
    (1) Rizalyn Repalda
    (2) All
    ''')

# Input a valid response
while True:
    try:
        employeeSelect = input('Select (1/2): ')
        if int(employeeSelect) in range(0, 3):
            break
    except:
        pass
    print('Input a valid number')

# To be used for "All Output" portion
allDict = []

if employeeSelect == '2':
    print('_All_ feature not implemented yet')

    for i in range(0,len(employeeDic)):
        inputName = employeeDic[str(i)][0]
        inputWageperDay = employeeDic[str(i)][1]
        inputPhilhealth = employeeDic[str(i)][2]
        inputSSS = employeeDic[str(i)][3]
        inputPagibig = employeeDic[str(i)][4]

        print()
        print(f'Getting wage info...')
        print('=' * 80)
        print(f'''
                Name: {inputName}
                Wage per Day: {inputWageperDay}
                Phil-health: {inputPhilhealth}
                SSS: {inputSSS}
                Pag-Ibig: {inputPagibig}
            ''')
        print('=' * 80)

        print()
        wageDays = input('Input the number of days to compute for wage: ')
        wageDays = int(wageDays)

        salaryAmount = int(wageDays) * int(employeeDic[str(i)][1])

        # Computing benefit deductions
        sssDeduction = int(employeeDic[str(i)][3]) / (30 / wageDays)
        philHealthDeduction = int(employeeDic[str(i)][2]) / (30 / wageDays)
        pagIbigDeduction = int(employeeDic[str(i)][4]) / (30 / wageDays)

        netSalary = salaryAmount - sssDeduction - philHealthDeduction - pagIbigDeduction

        print('=' * 80)
        print(f'Salary amount: {salaryAmount}')
        print(f'Philhealth Deduction: {philHealthDeduction}')
        print(f'SSS Deduction: {sssDeduction}')
        print(f'PagIbig Deduction: {pagIbigDeduction}')
        print()
        print(f'Net Salary: {netSalary}')
        print('=' * 80)

        # Generate Pandas Dataframe with output
        allOutput = {inputName: [salaryAmount, philHealthDeduction, sssDeduction, pagIbigDeduction, netSalary]}
        allDict.append(allOutput)
        print(allDict)

        print('=' * 80)

        print('Please double check if information is accurate.')
else:
    # Making it easier to read by changing dictionary values to vars
    inputName = employeeDic[employeeSelect][0]
    inputWageperDay = employeeDic[employeeSelect][1]
    inputPhilhealth = employeeDic[employeeSelect][2]
    inputSSS = employeeDic[employeeSelect][3]
    inputPagibig = employeeDic[employeeSelect][4]

    print()
    print(f'Getting wage info...')
    print('=' * 80)
    print(f'''
        Name: {inputName}
        Wage per Day: {inputWageperDay}
        Phil-health: {inputPhilhealth}
        SSS: {inputSSS}
        Pag-Ibig: {inputPagibig}
    ''')
    print('=' * 80)

    print()
    wageDays = input('Input the number of days to compute for wage: ')
    wageDays = int(wageDays)

    salaryAmount = int(wageDays) * int(employeeDic[employeeSelect][1])

    # Computing benefit deductions
    sssDeduction = int(employeeDic[employeeSelect][3]) / (30 / wageDays)
    philHealthDeduction = int(employeeDic[employeeSelect][2]) / (30 / wageDays)
    pagIbigDeduction = int(employeeDic[employeeSelect][4]) / (30 / wageDays)

    netSalary = salaryAmount - sssDeduction - philHealthDeduction - pagIbigDeduction

    print('=' * 80)
    print(f'Salary amount: {salaryAmount}')
    print(f'Philhealth Deduction: {philHealthDeduction}')
    print(f'SSS Deduction: {sssDeduction}')
    print(f'PagIbig Deduction: {pagIbigDeduction}')
    print()
    print(f'Net Salary: {netSalary}')
    print('=' * 80)

    # Generate Pandas Dataframe with output
    outputDic = pd.DataFrame({'0': [inputName, salaryAmount, philHealthDeduction, sssDeduction, pagIbigDeduction, netSalary]})
    outputDic.index = ['Name', 'Gross Salary', 'PhilHealth Deduction', 'SSS Deduction', 'Pag-Ibig Deduction', 'Net Salary']
    print(outputDic)

    print('=' * 80)

    print('Please double check if information is accurate.')

if employeeSelect == '2':
    # Make DF for "All Output" Portion
    allDictTEST = pd.concat([pd.DataFrame(x) for x in allDict], axis=1)
    allDictTEST.index = ['Gross Salary', 'PhilHealth Deduction', 'SSS Deduction', 'Pag-Ibig Deduction', 'Net Salary']

    print(allDictTEST)

# allOutputDict.index = ['Gross Salary', 'PhilHealth Deduction', 'SSS Deduction', 'Pag-Ibig Deduction', 'Net Salary']
outputQuestion = input('Would you want to save this info? (y/n)')

# Output to excel file
if outputQuestion == 'y':
    fileName = f'BBSalary_{date.today()}.xlsx'
    if employeeSelect == '2':
        allDictTEST.to_excel(fileName)
    else:
        outputDic.to_excel(fileName)
else:
    print("Ending program.")

