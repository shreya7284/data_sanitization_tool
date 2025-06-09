import csv
import re

def validate_aadhaar(aadhaar):
    # Check if Aadhaar is exactly 12 digits
    return bool(re.fullmatch(r'\d{12}', aadhaar))

def validate_phone(phone):
    # Check if phone number is 10 digits starting with 6-9 (Indian number format)
    return bool(re.fullmatch(r'[6-9]\d{9}', phone))

def validate_email(email):
    # Basic email validation regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.fullmatch(pattern, email))

def sanitize_data(input_file, output_file):
    with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Aadhaar_Valid', 'Phone_Valid', 'Email_Valid']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row['Aadhaar_Valid'] = validate_aadhaar(row['Aadhaar'])
            row['Phone_Valid'] = validate_phone(row['Phone'])
            row['Email_Valid'] = validate_email(row['Email'])
            writer.writerow(row)

if __name__ == '__main__':
    sanitize_data('input_data.csv', 'cleaned_data.csv')
    print("Data sanitization complete. Output saved to cleaned_data.csv")
