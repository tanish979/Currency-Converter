# Currency Converter Project

This project is a **Currency Converter** built using Python and Tkinter. It allows users to convert amounts between different currencies in real time using the **forex-python** library to fetch live exchange rates.

---

## Features

- **Real-Time Conversion**: Converts currency amounts based on live exchange rates.
- **User-Friendly GUI**: Built using Tkinter for an intuitive graphical interface.
- **Clear Functionality**: Easily reset inputs and outputs with a clear button.
- Supports multiple currencies like **USD, INR, CAD, EUR, CNY, DKK**.

---

## Demo

1. Enter the amount to convert.
2. Select the **From Currency** and **To Currency** from the dropdown menus.
3. Click the **Convert** button to get the converted value.
4. Use the **Clear All** button to reset all fields.

---

## Installation

### Prerequisites
- Python 3.10 or above installed.
- Virtual environment (optional but recommended).

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Currency-Converter
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
   .venv\Scripts\activate    # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:
   ```bash
   python CurrencyConverter_SourceCode.py
   ```

---

## Requirements

Dependencies are listed in the `requirements.txt` file:

```plaintext
forex-python==1.8
requests==2.32.3
simplejson==3.19.3
```

**Note**: Tkinter is included in Python's standard library and does not require separate installation.

---

## Usage

1. Enter the amount in the **Amount** field.
2. Select the **From Currency** and **To Currency**.
3. Click on **Convert** to display the converted amount.
4. Use **Clear All** to reset the fields.

---

## Supported Currencies

The project currently supports the following currencies:
- INR (Indian Rupee)
- USD (United States Dollar)
- CAD (Canadian Dollar)
- EUR (Euro)
- CNY (Chinese Yuan)
- DKK (Danish Krone)

More currencies can be added by updating the `CurrenyCode_list` in the source code.

---

## Project Structure

```
Currency-Converter/
├── CurrencyConverter_SourceCode.py   # Main source code for the project
├── requirements.txt                  # Project dependencies
├── README.md                         # Project documentation
```

---

## Key Modules Used

1. **Tkinter**: For building the graphical user interface.
2. **forex-python**: For fetching real-time currency exchange rates.
3. **requests**: For handling HTTP requests in the forex-python module.

---

## Troubleshooting

### Common Errors:
1. **JSONDecodeError**:
   - Ensure you have a stable internet connection.
   - Verify the forex-python API is functioning.

2. **Tkinter Not Found**:
   - Tkinter is a part of Python's standard library. If it is missing, install the Tkinter package:
     ```bash
     sudo apt-get install python3-tk   # On Ubuntu/Debian
     ```

---

## Future Improvements

- Add support for more currencies.
- Implement error handling for API connection issues.
- Enhance UI design with modern frameworks.

---

## Acknowledgements

- **Python** for providing a versatile programming language.
- **forex-python** library for live currency exchange rates.
- **Tkinter** for GUI development.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest features!

