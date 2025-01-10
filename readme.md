# Debt Tracker

Debt Tracker is a simple Flask web application that allows users to track their credit card debts by entering card details such as card name, APR, and balance.
This program is currently being developed as a personal project to practice web development with Flask, Python, and deploying to Azure Web Applications.

## Features

- Add credit card details including card name, APR, and balance.
- Display a list of all entered credit cards with their details.

## Requirements

- Python 3.x
- Flask
- Gunicorn (for deployment)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/iwindon/debt-tracker.git
    cd debt-tracker
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask development server:
    ```
    python3 DebtTracker.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Deployment

To deploy the application using Gunicorn, use the following command:
    ```
    gunicorn --bind 0.0.0.0:$PORT Debt_Tracker:app
    ```

## License

This project is licensed under the MIT License.






    
    