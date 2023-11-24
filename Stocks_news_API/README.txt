# Stock News Notifier

This script fetches stock data and related news, calculates the percentage difference, and sends an email notification with breaking news if certain conditions are met.

## Prerequisites
Before running the script, make sure you have the required Python libraries installed:
```bash
pip install requests

Configuration
Create a file named config.py with the following content:
python
Copy code
# config.py

API_KEY_STOCKS = "your_alpha_vantage_api_key"
API_KEY_NEWS = "your_newsapi_org_api_key"
smtp_server = "smtp.your_email_provider.com"
my_email = "your_email@gmail.com"
password = "your_email_password"
smtp_port = 587
Replace the placeholder values with your actual API keys and email configuration.

Create a .env file in the root directory of your project:

API_KEY_STOCKS=your_alpha_vantage_api_key
API_KEY_NEWS=your_newsapi_org_api_key
Replace the placeholder values with your actual API keys.

Usage
Run the script by executing the following command:


python stock_news_notifier.py
The script will fetch stock and news data, analyze the percentage difference, and send an email with breaking news if conditions are met.

License
This project is licensed under the MIT License - see the LICENSE file for details.



Make sure to replace the placeholder values with your actual API keys and email configuration. 
This README provides a brief overview of the script, how to set it up, and how to run it. 
You may want to customize it further based on your project's specific requirements.

