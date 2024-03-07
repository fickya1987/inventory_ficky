import time
import json
import streamlit as st

st.title("Gaman E-Commerce Inventory Database")

# Load inventory from JSON
with open('Records.json', 'r') as fd:
    record = json.load(fd)

# Display the menu
st.subheader("Menu")
st.write("Product ID | Product  \t| Price | Quantity")
for key in record.keys():
    st.write(f"{key}: {record[key]['Name']}\t| {record[key]['Price']}\t| {record[key]['Qty']}")

# Taking user input
ui_name = st.text_input("Enter your name:")
ui_mail = st.text_input("Enter your e-mail ID:")
ui_ph = st.text_input("Enter your phone number:")
ui_id = st.text_input("Enter the Product ID:")
ui_qty = st.number_input("Enter the Quantity:", min_value=1, step=1)

# Check if the entered product ID exists
if ui_id in record:
    total_amount = record[ui_id]['Price'] * ui_qty

    # Display purchase details
    st.subheader("Bill")
    st.write("Name       :", record[ui_id]['Name'])
    st.write("Price      :", record[ui_id]['Price'])
    st.write("Quantity   :", ui_qty)
    st.write("Total amt  :", total_amount)

    # Apply discount if applicable
    if total_amount >= 5000:
        discount = 10
        dis_amt = total_amount * (discount / 100)
        final_price = total_amount - dis_amt
        st.write("Original Price             :", total_amount)
        st.write("Discount Amount (10% off)  :", dis_amt)
        st.write("Final Price:", final_price)
    else:
        st.write("Customer does not qualify for a discount")

    # Update records
    record[ui_id]['Qty'] -= ui_qty

    # Save records in JSON file
    with open("Records.json", 'w') as fd:
        json.dump(record, fd)

    # Save records in Sales file
    sale = f"{ui_name},{ui_mail},{ui_ph},{ui_id},{record[ui_id]['Name']},{ui_qty},{record[ui_id]['Price']},{total_amount},{time.ctime()}\n"
    with open('Sales.txt', 'a') as fd:
        fd.write(sale)

    st.write("Thank You!!")
else:
    st.write(f"Product with ID {ui_id} not found in inventory.")
