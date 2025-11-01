import streamlit as st
import math

# -------------------------------
# Streamlit Scientific Calculator (Casio fx-991 Style)
# -------------------------------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Scientific Calculator (Casio fx-991 Style)")

st.markdown("""
This is a **Streamlit-based scientific calculator** inspired by Casio fx-991.
You can perform trigonometric, logarithmic, power, factorial, and basic arithmetic operations.
""")

# Input area for expression
expression = st.text_input("Enter Expression (e.g., sin(45) + log(10) * 3):", "")

# Mapping for Casio-style shortcuts
allowed_funcs = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "factorial": math.factorial,
    "pow": math.pow,
    "abs": abs,
    "exp": math.exp,
    "deg": math.degrees,
    "rad": math.radians
}

# Helper function to safely evaluate the expression
def evaluate_expression(expr):
    try:
        # Replace common Casio-like notation
        expr = expr.replace("^", "**")
        # Evaluate using only safe functions
        result = eval(expr, {"__builtins__": None}, allowed_funcs)
        return result
    except Exception as e:
        return f"❌ Error: {e}"

# Button to evaluate
if st.button("Calculate"):
    if expression.strip() == "":
        st.warning("Please enter an expression first.")
    else:
        result = evaluate_expression(expression)
        st.success(f"**Result:** {result}")

st.divider()
st.caption("Casio-style scientific calculator built with ❤️ using Streamlit and Python.")
