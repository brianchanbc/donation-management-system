# Donation Management System

## Overview

Donation Management System is a Python program to manage donations and run analytics on records. 

## How to Use The Program

**run.py**: The program interface to use the Donation class to register donations, log distributions and generate reports. Amend the inputs to try it out!

**donation.py**: Donation class with instance initializer, register_donation, log_distribution and generate_report class methods. 

**test_donation.py**: Unit tests for register_donation, log_distribution and generate_report class methods.

**requirements.txt**: Dependencies 

**donation_report.csv**: Output of generate_report("donation") class method as CSV file

**inventory_report.csv**: Output of generate_report("inventory") class method as CSV file

## Getting Started

1. **Clone Repository** 
```bash
git clone git@github.com:brianchanbc/donation-management-system.git
cd donation-management-system
```

2. **Install Dependencies** 
```bash
python -m venv donation-system
activate donation-system
pip install -r requirements.txt 
```

3. **Run Program**
```bash
python run.py
```

## Author

Brian Chan

## License

This project is licensed under the [MIT License](LICENSE).