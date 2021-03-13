#Kylie Gregory
#1/24/19
#Programming Assignment 2
#SEC290

print('Automobile Fuel Cost Calculator')
print(' ')
print('This program may help you decide which car makes sense for you based on your')
print('budget. You will be asked to enter the MPG for the car you have in mind, the')
print('average number of miles you expect to drive each month and the cost per gallon')
print('for fuel.')
print(' ')
print('The program will then calculate the monthly fuel cost.')
print(' ')
car_mpg = input("Please enter the car's MPG (miles per gallon): ")
car_mpg = float(car_mpg)
print(' ')
avg_miles = input('Please enter the average number of miles driven per month: ')
avg_miles = int(avg_miles)
print(' ')
fuel_cost = input('Please enter the cost of fuel per gallon: $')
fuel_cost = float(fuel_cost)
print(' ')
print('Given price of fuel at ${}/gallon and {} miles/month traveled:'.format(fuel_cost, avg_miles))
print(' ')

gallons_per_month = avg_miles / car_mpg
monthly_fuel_cost = gallons_per_month * fuel_cost

print('Gallons used each month: {:.1f}'.format(gallons_per_month))
print('Monthly cost of fuel: ${:.2f}'.format(monthly_fuel_cost))
