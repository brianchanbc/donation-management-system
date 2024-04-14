from datetime import datetime
import pandas as pd

class Donation:
    """A class to manage donations and distributions of items"""
    def __init__(self) -> None:
        """Initializes the Donation class with empty inventory, donation log, and distribution log"""
        self._inventory = {}
        self._donation_log = []
        self._distribution_log = []
    
    def register_donation(self, donor: str, type: str, quantity: int, date_str: str) -> None:
        """Registers a donation of items to the inventory and logs the donation
        Args:
            donor (str): The name of the donor
            type (str): The type of items donated
            quantity (int): The quantity of items donated
            date_str (str): The date of the donation in the format 'YYYY-MM-DD'
        """
        # Check if the input is provided
        self._check_input_provided(donor)
        self._check_input_provided(type)
        self._check_input_provided(quantity)
        self._check_input_provided(date_str)
        # Check if the input is of the correct type
        self._check_input_types(donor, str)
        self._check_input_types(type, str)
        self._check_input_types(quantity, int)
        self._check_input_types(date_str, str)
        # Check if the date is valid and not in the future
        self._check_date_valid(date_str)
        # Check if the quantity is larger than 0
        self._check_quantity_larger_than_zero(quantity)
        # Update the inventory and donation log
        self._inventory[type] = self._inventory.get(type, 0) + quantity
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        self._donation_log.append((donor, type, quantity, date))
    
    def log_distribution(self, type: str, quantity: int, distribution_time_str: str) -> None:
        """Logs the distribution of items from the inventory and updates the inventory
        Args:
            type (str): The type of items to be distributed
            quantity (int): The quantity of items to be distributed
            distribution_time_str (str): The date of the distribution in the format 'YYYY-MM-DD'
        """
        # Check if the input is provided
        self._check_input_provided(type)
        self._check_input_provided(quantity)
        self._check_input_provided(distribution_time_str)
        # Check if the input is of the correct type
        self._check_input_types(type, str)
        self._check_input_types(quantity, int)
        self._check_input_types(distribution_time_str, str)
        # Check if the date is valid and not in the future
        self._check_date_valid(distribution_time_str)
        self._check_quantity_larger_than_zero(quantity)
        self._check_inventory_available(type, quantity)
        # Update the inventory and distribution log
        self._inventory[type] -= quantity
        distribution_time = datetime.strptime(distribution_time_str, '%Y-%m-%d').date()
        self._distribution_log.append((type, quantity, distribution_time))
    
    def generate_report(self, report_type: str) -> None:
        """Generates a report of the inventory or donations
        Args:
            report_type (str): The type of report to generate ('inventory' or 'donation')
        """
        # Check if the input is provided
        self._check_input_types(report_type, str)
        # Check if the report type is valid
        self._check_report_type(report_type)
        # Generate the inventory report
        if report_type == 'inventory':
            # Convert the inventory dictionary to a DataFrame and save it to a CSV file
            df = pd.DataFrame(self._inventory.items(), columns=['Type', 'Quantity'])
            # Make the index start from 1
            df.index += 1
            df.to_csv('inventory_report.csv')
        # Generate the donation report
        elif report_type == 'donation':
            # Convert the donation log to a DataFrame, group by donor and type, sum the quantities, and save it to a CSV file
            df = pd.DataFrame(self._donation_log, columns=['Donor', 'Type', 'Quantity', 'Date'])
            df = df.groupby(['Donor', 'Type'])['Quantity'].sum().reset_index()
            # Make the index start from 1
            df.index += 1
            df.to_csv('donation_report.csv')
    
    @staticmethod
    def _check_input_types(input, expected_type):
        """Checks if the input is of the expected type
        Args:
            input: The input to check
            expected_type: The expected type of the input
        raises:
            TypeError: If the input is not of the expected type
        """
        if not isinstance(input, expected_type):
            raise TypeError(f"error: {input} must be provided as type {expected_type.__name__}")       
    
    @staticmethod
    def _check_input_provided(input):
        """Checks if the input is provided
        Args:
            input: The input to check
        raises:
            TypeError: If the input is not provided
        """
        if not input:
            raise TypeError(f"error: {input} must be provided")
    
    @staticmethod
    def _check_date_valid(date_str):
        """Checks if the date provided is valid and not in the future
        Args:
            date_str (str): The date string to check
        raises:
            ValueError: If the date is not in the correct format or is in the future
        """
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("error: date must be provided in the format 'YYYY-MM-DD'")
        if date > datetime.today().date():
            raise ValueError("error: date cannot be in the future")
    
    @staticmethod
    def _check_quantity_larger_than_zero(quantity):
        """Checks if the quantity is larger than 0
        Args:
            quantity (int): The quantity to check
        raises:
            ValueError: If the quantity is less than or equal to 0
        """
        if quantity <= 0:
            raise ValueError("error: quantity must be larger than 0")
    
    def _check_inventory_available(self, type, quantity):
        """Checks if the inventory has enough items of the specified type to be distributed
        Args:
            type (str): The type of items to be distributed
            quantity (int): The quantity of items to be distributed
        raises:
            ValueError: If the type is not in the inventory or the quantity is larger than the inventory quantity
        """
        if type not in self._inventory:
            raise ValueError(f"error: {type} not found in inventory")
        elif self._inventory.get(type, 0) < quantity:
            raise ValueError(f"error: insufficient {type} in inventory to be distributed")
    
    @staticmethod
    def _check_report_type(report_type):
        """Checks if the report type is valid
        Args:
            report_type (str): The type of report to generate
        raises:
            ValueError: If the report type is not 'inventory' or 'donation'
        """
        if report_type not in ['inventory', 'donation']:
            raise ValueError('Invalid report type: must be either "inventory" or "donation"')