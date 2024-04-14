from donation import Donation

def main():
    # Create an instance of the Donation class
    donation = Donation()
    # Register some donation records
    donation.register_donation('Andrew', 'food', 10, '2024-04-01')
    donation.register_donation('Brian', 'food', 20, '2024-04-01')
    donation.register_donation('Brian', 'clothes', 5, '2024-04-02')
    donation.register_donation('Andrew', 'money', 15, '2024-04-03')
    donation.register_donation('Brian', 'food', 10, '2024-04-04')
    # Log some distribution records
    donation.log_distribution('food', 5, '2024-04-05')
    donation.log_distribution('clothes', 3, '2024-04-06')
    # Generate reports
    donation.generate_report('inventory')
    donation.generate_report('donation')
    
if __name__ == '__main__':
    main()