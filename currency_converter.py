import streamlit as st

# Conversion rates dictionary
CURRENCY_RATES = {
    "Australian Dollar": 49.10,
    "Brazilian Real": 17.30,
    "British Pound": 90.92,
    "Bulgarian Lev": 39.80,
    "Chinese Yuan": 10.29,
    "Euro": 77.85,
    "HongKong Dollar": 8.83,
    "Indonesian Rupiah": 0.004864,
    "Japanese Yen": 0.628,
    "Pakistani Rupee": 0.49,
    "SriLankan Rupee": 0.39,
    "Swiss Franc": 69.62,
    "US Dollar": 69.32
}

# App title and subtitle
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")
st.markdown("<h1 style='text-align: center; color: darkred;'>💱 Currency Converter 💱</h1>", unsafe_allow_html=True)
st.markdown("---")

# Select conversion type
conversion_type = st.radio("Select Conversion Type", ["INR to Other", "Other to INR"], horizontal=True)

# Input amount
amount = st.text_input("Enter Amount", value="", help="Enter the amount you want to convert")

# Currency selection
currency = st.selectbox("Select Currency", options=["Select"] + list(CURRENCY_RATES.keys()))

# Convert button
if st.button("Convert"):
    if amount.strip() == "" or currency == "Select":
        st.error("❌ Please enter a valid amount and select a currency.")
    else:
        try:
            value = float(amount)
            rate = CURRENCY_RATES[currency]

            if conversion_type == "INR to Other":
                converted = round(value / rate, 2)
                st.success(f"💰 {value} INR = {converted} {currency}")
            else:
                converted = round(value * rate, 2)
                st.success(f"💰 {value} {currency} = {converted} INR")

        except ValueError:
            st.error("❌ Amount must be a number.")

# Footer
st.markdown("---")
st.markdown("<center>Developed with ❤️ using Streamlit</center>", unsafe_allow_html=True)
