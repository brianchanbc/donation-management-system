import unittest
from donation import Donation  
            
class TestRegisterDonation(unittest.TestCase):
    """Tests for the register_donation method in the Donation class"""

    def setUp(self):
        """Initializes the Donation class with empty inventory, donation log, and distribution log"""
        self.donation = Donation()

    def test_invalid_input_type(self):
        """Test for invalid input type for the register_donation method in the Donation class"""
        with self.assertRaises(TypeError):
            self.donation.register_donation('doner', 'food', '5', '2024-04-01')

    def test_missing_input_parameter(self):
        """Test for missing input parameter for the register_donation method in the Donation class"""
        with self.assertRaises(TypeError):
            self.donation.register_donation('doner', 'food', 5)

    def test_invalid_date_format(self):
        """Test for invalid date format for the register_donation method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.register_donation('doner', 'food', 5, '202-04-01')

    def test_date_pass_todays_date(self):
        """Test for date passed is today's date for the register_donation method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.register_donation('doner', 'food', 5, '2024-09-20')

    def test_quantity_less_than_0(self):
        """Test for quantity less than 0 for the register_donation method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.register_donation('doner', 'food', -10, '2024-04-01')


class TestLogDistribution(unittest.TestCase):
    """Tests for the log_distribution method in the Donation class"""

    def setUp(self):
        """Initializes the Donation class with empty inventory, donation log, and distribution log"""
        self.donation = Donation()

    def test_invalid_input_type(self):
        """Test for invalid input type for the log_distribution method in the Donation class"""
        with self.assertRaises(TypeError):
            self.donation.log_distribution('clothes', '10', '2024-04-01')

    def test_missing_input_parameter(self):
        """Test for missing input parameter for the log_distribution method in the Donation class"""
        with self.assertRaises(TypeError):
            self.donation.log_distribution('clothes', 10)

    def test_invalid_date_format(self):
        """Test for invalid date format for the log_distribution method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.log_distribution('clothes', 10, '2024-0-01')

    def test_date_pass_todays_date(self):
        """Test for date passed is today's date for the log_distribution method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.log_distribution('clothes', 10, '2024-08-12')

    def test_quantity_less_than_0(self):
        """Test for quantity less than 0 for the log_distribution method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.log_distribution('clothes', -5, '2024-04-01')

    def test_type_not_in_inventory(self):
        """Test for type not in inventory for the log_distribution method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.register_donation('doner', 'food', 5, '2024-04-01')
            self.donation.log_distribution('non-existing type', 5, '2024-04-01')

    def test_quantity_more_than_inventory_quantity(self):
        """Test for quantity more than inventory quantity for the log_distribution method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.register_donation('doner', 'food', 5, '2024-04-01')
            self.donation.log_distribution('food', -30, '2024-04-01')


class TestGenerateReport(unittest.TestCase):
    """Tests for the generate_report method in the Donation class"""

    def setUp(self):
        """Initializes the Donation class with empty inventory, donation log, and distribution log"""
        self.donation = Donation()

    def test_invalid_input_type(self):
        """Test for invalid input type for the generate_report method in the Donation class"""
        with self.assertRaises(TypeError):
            self.donation.generate_report(123)

    def test_invalid_report_type(self):
        """Test for invalid report type for the generate_report method in the Donation class"""
        with self.assertRaises(ValueError):
            self.donation.generate_report('analytics')

if __name__ == '__main__':
    unittest.main()