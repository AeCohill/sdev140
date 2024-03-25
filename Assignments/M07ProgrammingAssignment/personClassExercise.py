'''
Author:Adam Cohill
Date Written: 07/21/23
Assignment : Write a class named Person with data attributes
for a person’s name,address, and telephone number.
Next, write a class named Customer that is a subclass of the Person class.
The Customer class should have a data attribute for a customer number,
and a Boolean data attribute indicating whether the customer wishes to be on a mailing list.
Demonstrate an instance of the Customer class in a simple program.
'''

class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list=False):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

if __name__ == "__main__":
    name = input("Name: ")
    address = input("Address: ")
    telephone = input("Phone: ")
    customer_number = int(input("Customer Number: "))
    mailing_list = input("Would you like to be on the mailing list? (y/n): ").lower() == "y"

    customer = Customer(name, address, telephone, customer_number, mailing_list)

    print("\nCustomer Information:")
    print("Name:", customer.name)
    print("Address:", customer.address)
    print("Telephone:", customer.telephone)
    print("Customer Number:", customer.customer_number)
    print("Mailing List:", "Yes" if customer.mailing_list else "No")
