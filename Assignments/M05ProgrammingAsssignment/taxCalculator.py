'''
Author:Adam Cohill
Date Written: 06/15/23
Assignment : A retail company must file a monthly sales tax report
listing the total sales for the month,
and the amount of state and county sales tax collected.
The state sales tax rate is 5 percent and the county
sales tax rate is 2.5 percent.
Write a function that asks the user
to enter the total sales for the month.
From this figure, the application
should calculate and display the following
'''

cTax = 0.025
sTax = 0.05
stateTax = 0.0
countyTax = 0.0

totalSales = input('Please enter your total sales: ')
totalSales = float(totalSales)

def calTaxes ():
    countyTax = totalSales * cTax
    countyTax = float(countyTax)
    print ('Your county tax is: ','$',"{:.2f}".format(countyTax))

    stateTax = totalSales * sTax
    stateTax = float(stateTax)
    print('Your state tax is: ','$',"{:.2f}".format(stateTax))

    totalIncTax = totalSales + stateTax + countyTax

    print('Your total including taxes is: ','$', "{:.2f}".format(totalIncTax))    

calTaxes()
