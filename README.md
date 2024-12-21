# Iron Condor Calculator

This is a Python application with a graphical user interface (GUI) built using **Tkinter**. It allows you to calculate the maximum profit, maximum loss, and risk percentage of your account for an Iron Condor options trading strategy.

---

## Features

- **User-Friendly GUI**: Simple and intuitive interface for entering trade details.
- **Key Calculations**:
  - Maximum Profit: Net premium received from the trade.
  - Maximum Loss: The highest potential loss from the trade (either put or call side).
  - Risk (% of Account): Maximum loss as a percentage of your total account size.
- **Customizable Input Fields**:
  - Account size
  - Strike prices (short and long) for puts and calls
  - Credits and debits for each leg
  - Number of contracts

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/iron-condor-calculator.git
   cd iron-condor-calculator
   ```

2. **Install Dependencies**:
   This project requires Python 3.x. Tkinter is included in most Python installations. If not, install it using:
   ```bash
   sudo apt-get install python3-tk   # For Ubuntu/Debian
   ```

3. **Run the Application**:
   ```bash
   python iron_condor_calculator.py
   ```

---

## How to Use

1. **Input Fields**:
   - **Account Size (£)**: Enter your total trading account size in GBP.
   - **Strike Prices**: Enter the short and long strike prices for both puts and calls.
   - **Credits and Debits**: Enter the premium received or paid for each leg of the Iron Condor.
   - **Number of Contracts**: Specify how many contracts you are trading.

2. **Calculate**:
   - Click the **Calculate** button.
   - The results will display:
     - Maximum Profit
     - Maximum Loss
     - Risk as a percentage of your account size.

3. **Example Inputs**:
   - **Account Size**: £3000
   - **Short Put Strike**: 3900
   - **Long Put Strike**: 3850
   - **Short Call Strike**: 4100
   - **Long Call Strike**: 4150
   - **Credits and Debits**: Enter the premiums received/paid for each leg.
   - **Contracts**: 2

   **Output Example**:
   ```
   Max Profit: £150.00
   Max Loss: £350.00
   Risk (% of Account): 11.67%
   ```
![image](https://github.com/user-attachments/assets/23d4bb21-6e65-4cda-922b-8b72348fa8f2)


