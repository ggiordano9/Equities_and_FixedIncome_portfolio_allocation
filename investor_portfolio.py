################################################################################
# Step 1 - Financial tax information:
# Import personal tax information from 'financial_information.py' script into the file "investor_portfolio"
# which contains code for Investor Portfolio's customer interface in order to add wallet operations to the 
# application. We will provide the investors account information to the application.

# Step 2 - Crypto wallet:
# Within the Streamlit sidebar section of code, create a variable named `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the Investor Portfolio customer's account and will contain their wallet information. Additionally within 
# this section, there will be an `st.sidebar.write` function that will display the balance of the customer’s account.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List

# From `financial_information.py' import the functions generate_account, get_balance
from financial_information import generate_account, get_age

# From `crypto_wallet.py' import the functions generate_account, get_balance
from crypto_wallet import generate_crypto_account, get_balance


################################################################################
# Financial Services Information

# Database of Financial services including their service, name, sector, company, price, trending, esg risk rating

# Overall format: Example - AAPL (11/17/21 - 9:54 PM)

# Financial Service: Stocks
# Sector: Technology
# Company: AAPL
# Price: 153.49
# Trending: High (given from twitter keyword search code)
# ESG Risk Rating: 17   
# Market Summary: Line graph of (1D, 5D, 1M)

# Need to figure out how to import information from other .py files into the financial_database !!!!

financial_database = {
    "Stocks": ["Stocks", " ", " ", " ", " ", " ", "ESG #", "Market Summary"],
    "Options": ["Options", " ", " ", " ", " ", "ESG #", "M.S"],
    "Bonds": ["Bonds", " ", " ", " ", " ", "ESG #", "M.S"],
    "Cryptocurrency": ["Cryptocurrency", " ", " ", " ", " ", "ESG #", "M.S"]
}

# A list of the financial_services information
financial_services = ["Stocks", "Options", "Bonds", "Cryptocurrency"]

def get_financial_services():
    """Display the database of the current state of the financial services."""
    db_list = list(financial_database.values())
    for number in range(len(people)):
        st.write("Financial Service: ", db_list[number][0])
        st.write("Sector: ", db_list[number][1])
        st.write("Company: ", db_list[number][2])
        st.write("Price: ", db_list[number][3])
        st.write("Trending: ", db_list[number][4]) # Keywords from twitter whether a company/coin has a positive, negative or neutral trend
        st.write("ESG Risk Rating: ", db_list[number][5]) # Can be used for crypto mining? Perhaps?
        st.write("Market Summary: ", db_list[number][6]) # Display a plot of the (1D, 5D, 1M)
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Investor Portfolio")
st.markdown("## Financial areas recommended to invest in based on your financial background.")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

### FROM FINANCIAL_INFORMATION.py ###

# Write the client's personal information to the sidebar
st.sidebar.markdown("## Client Account Information")
account = generate_account()
st.sidebar.write(account.address)

### FROM CRYPTO_WALLET.py ###

# Write the investor's Ethereum account address to the sidebar
st.sidebar.markdown("")
crypto_account = generate_crypto_account('')
st.sidebar.write(crypto_account.address)

# Call `get_balance` function and pass it your account address
st.sidebar.write(get_balance(account.address))

##########################################

person = st.sidebar.selectbox('Select a Financial Area', financial_services)


hours = st.sidebar.number_input("")

st.sidebar.markdown("")


################################################################################
