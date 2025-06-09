# 🧹 Data Sanitization & Validation Tool

This project is a simple Python-based utility for cleaning and validating Aadhaar-related user data. It processes a CSV file (`input_data.csv`), sanitizes common fields like Aadhaar Number, Email, Phone, and Date of Birth, and saves a clean version as `sanitized_data.csv`.

## 🚀 Features

- Strips unnecessary whitespace and invalid characters
- Validates Aadhaar numbers (12 digits)
- Validates phone numbers (10 digits)
- Validates email format
- Ensures DOB format (YYYY-MM-DD)
- Outputs a cleaned CSV with only valid records

## 🛠️ Technologies Used

- Python
- `pandas` for data handling
- Regular expressions (`re`) for field validation

## 📂 How to Run

1. Place your raw data file as `input_data.csv` in the same directory.
2. Run the script:

```bash
python data_sanitization.py

3. Output will be saved as sanitized_data.csv.

📄 Sample Input (input_data.csv)
| Aadhaar        | Email                                       | Phone      | DOB        |
| -------------- | ------------------------------------------- | ---------- | ---------- |
| 1234 5678 9123 | [user@example.com](mailto:user@example.com) | 9876543210 | 2000-01-01 |
| 1111-2222-3333 | invalid-email                               | 12345      | 01/01/2000 |

✅ Sample Output (sanitized_data.csv)
| Aadhaar      | Email                                       | Phone      | DOB        |
| ------------ | ------------------------------------------- | ---------- | ---------- |
| 123456789123 | [user@example.com](mailto:user@example.com) | 9876543210 | 2000-01-01 |


