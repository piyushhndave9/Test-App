import streamlit as st

# -------------------------------
# Streamlit Calculator App
# -------------------------------
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, format="%.6f")
num2 = st.number_input("Enter second number", value=0.0, format="%.6f")

# Operation selection
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("Division by zero is not allowed!")
                st.stop()
            result = num1 / num2
        st.success(f"Result = {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.caption("Built with ❤️ using Streamlit")
