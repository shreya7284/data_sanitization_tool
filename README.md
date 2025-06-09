# Data Sanitization & Validation Tool

## Overview
This Python project validates user data such as Aadhaar numbers, phone numbers, and email addresses from CSV files. It automates the process of data cleaning by identifying and flagging invalid entries, helping improve data accuracy and integrity.

## Features
- Validates Aadhaar numbers ensuring exactly 12 digits.  
- Checks Indian phone numbers starting with digits 6-9 and 10 digits long.  
- Validates email addresses with a regex pattern.  
- Outputs a new CSV file with additional columns indicating validity of each data field.

## How to Use
1. Place your input CSV file named `input_data.csv` in the project directory.  
2. Run the script:
   ```bash
   python data_sanitization.py

3. Check the output file cleaned_data.csv for validation results.

Technologies Used

1)Python

2)CSV file handling

3)Regular expressions (regex)

Sample Input
| Name   | Aadhaar      | Phone      | Email                                           |
| ------ | ------------ | ---------- | ----------------------------------------------- |
| Shreya | 123412341234 | 9876543210 | [shreya@example.com](mailto:shreya@example.com) |
| Rohan  | 111122223333 | 1234567890 | rohan@@example.com                              |

Sample Output
| Name   | Aadhaar      | Phone      | Email                                           | Aadhaar\_Valid | Phone\_Valid | Email\_Valid |
| ------ | ------------ | ---------- | ----------------------------------------------- | -------------- | ------------ | ------------ |
| Shreya | 123412341234 | 9876543210 | [shreya@example.com](mailto:shreya@example.com) | True           | True         | True         |
| Rohan  | 111122223333 | 1234567890 | rohan@@example.com                              | True           | False        | False        |

This project is open-source and free to use.
