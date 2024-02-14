# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 8/3/2023
# Description:

class Employee:
    """Represents Employees at an organization with a name, id_number, salary, and an email_address"""

    def __init__(self, name, id_number, salary, email_address):
        """
        inititializes data members with argument values
        :param name: string
        :param id_number: int
        :param salary: int
        :param email_address: string
        """
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        '''
        returns name
        '''
        return self._name

    def get_id_number(self):
        '''
        returns id_number
        '''
        return self._id_number

    def get_salary(self):
        '''
        returns salary
        '''
        return self._salary

    def get_email_address(self):
        '''
        returns email_address
        '''
        return self._email_address


def make_employee_dict(list_names, list_id_number, list_salary, list_email_address):
    """
    takes as parameters a list of names, a list of ID numbers, a list of salaries and a list of email addresses
     to create a dictionary where the key is the ID number and the value for that key is the Employee object
    :param list_names: list of strings
    :param list_id_number: list of ints
    :param list_salary: list of ints
    :param list_email_address: list of strings
    :return: dictionary with id_number keys and Employee object values
    """
    employee_dict = {}  # Creates empty dictionary
    for x in range(0, len(list_id_number)):  # iterates for each id_number
        # Creates employee objects and keys for dictionary
        employee_dict[list_id_number[x]] = Employee(list_names[x], list_id_number[x], list_salary[x], list_email_address[x])
    return employee_dict
