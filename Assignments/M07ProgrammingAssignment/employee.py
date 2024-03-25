'''
Author:Adam Cohill
Date Written: 07/21/23
Assignment : Write an Employee class that keeps data attributes
for the following pieces of information:Employee nameEmployee number
Next, write a class named ProductionWorker that is
a subclass of the Employee class. The ProductionWorker class
should keep data attributes for the following information:Hourly pay rate
Shift number (an integer, such as 1, 2, or 3)
The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. The day shift is shift 1 and the night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
Once you have written the classes, write a program that:
creates an object of the ProductionWorker class and prompts the user
to enter data for each of the object’s data attributes;
store the data in the object; and then
use the object’s accessor methods to retrieve it and display it on the screen.
'''

class Employee:
    def __init__(self, name, emp_number):
        self.name = name
        self.emp_number = emp_number

    def get_name(self):
        return self.name

    def get_emp_number(self):
        return self.emp_number

class ProductionWorker(Employee):
    def __init__(self, name, emp_number, hourly_pay_rate, shift):
        super().__init__(name, emp_number)
        self.hourly_pay_rate = hourly_pay_rate
        self.shift = shift

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def get_shift(self):
        return self.shift

if __name__ == "__main__":
    # Prompt the user to enter data for the ProductionWorker object
    name = input("Enter employee name: ")
    emp_number = int(input("Enter employee number: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    shift = int(input("Enter shift number (1 for day shift, 2 for night shift): "))

    # Create an object of the ProductionWorker class and store the data
    production_worker = ProductionWorker(name, emp_number, hourly_pay_rate, shift)

    # Display the stored data using accessor methods
    print("\nEmployee Information:")
    print("Name:", production_worker.get_name())
    print("Employee Number:", production_worker.get_emp_number())
    print("Hourly Pay Rate:", production_worker.get_hourly_pay_rate())
    print("Shift:", "Day" if production_worker.get_shift() == 1 else "Night")
