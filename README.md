# BBSalaryCompute
Automated Computation for Philippines Salaries with contributions (SSS, Philhealth, Pag-Ibig) based on monthly wage

## Menu Details
1. Compute for Half Month Payroll
- Computes the payroll while taking into consideration the deductions for the first half or the second half of the month.

2. Compute for Monthly Payroll
- Computes for the monthly payroll while considering ALL deductions for the whole month 

3. Find SSS Contribution
- Find the total employer and employee contributions based on the most recent SSS contributions Table

4. Non Employee Wage Computation
- Simple wage computation for part-time employees that don't have contributions

5. Import Wages from Excel
- Wage computation taken from inputting salary values in the excel file ('Input' folder)



09-09-2022
- Improved on the import function not needed the '15th or 30th' input from the user anymore and just reads the date
- Added comments to the code for readability 

09-01-2022
- Added a 5th selection for importing wage data from excel file

Main2.0
- Updated salary and benefits computation to match real-world process (Pag-Ibig is deducted 1st half, SSS and PH is deducted 2nd half)
- Included output for half-month payroll
- Included salary computation (menu 4) for employees without benefits (part-time and contractual)

Notes: 
- Salary benefit deductions are computed based on a per day basis. For the half-month payroll, deductions are made depending on which half of the month is selected. 
- Output for half-month payroll is saved in the 'Output' folder
