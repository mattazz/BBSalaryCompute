import pandas as pd
import openpyxl
from datetime import date
from os.path import exists

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
    '1': ['Janet Apostol', 533, 277.16, 600, 100],
    '2': ['Rizalyn Repalda', 533, 277.16, 600, 100]
}
print()
# Input getting data of girls
print('''Which employee:
    (1) Janet Apostol
    (2) Rizalyn Repalda
    ''')

# Input a valid response
while True:
    try:
        employeeSelect = input('Select (1/2): ')
        if int(employeeSelect) in range(1, 3):
            break
    except:
        pass
    print('Input a valid number')

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
outputDic = pd.DataFrame({inputName: [salaryAmount, philHealthDeduction, sssDeduction, pagIbigDeduction, netSalary]})
outputDic.index = ['Gross Salary', 'PhilHealth Deduction', 'SSS Deduction', 'Pag-Ibig Deduction', 'Net Salary']
print(outputDic)

print('=' * 80)

print('Please double check if information is accurate.')
outputQuestion = input('Would you want to save this info? (y/n)')

# Output to excel file
if outputQuestion == 'y':
    fileName = f'BBSalary_{date.today()}.xlsx'
    outputDic.to_excel(fileName)
else:
    print("Ending program, thank you!")

