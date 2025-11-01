import streamlit as st
import math

# -----------------------------
# STREAMLIT SCIENTIFIC CALCULATOR (CASIO FX-991 STYLE)
# -----------------------------
st.set_page_config(page_title="Casio fx-991 Calculator", page_icon="🧮", layout="centered")

# --- Custom CSS for better visuals ---
st.markdown("""
    <style>
    body {
        background-color: #111;
        color: #f5f5f5;
    }
    .stButton>button {
        background-color: #222;
        color: #fff;
        border: 1px solid #444;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px 15px;
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #00b4d8;
        color: white;
        border: none;
    }
    .stTextInput>div>div>input {
        background-color: #000;
        color: #00ff00;
        font-size: 22px;
        text-align: right;
        border: 2px solid #00b4d8;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Casio fx-991 Scientific Calculator")

# --- Calculator display ---
display = st.text_input("Display", value="", placeholder="0", label_visibility="collapsed", key="display")

# --- Button layout grid ---
buttons = [
    ["sin", "cos", "tan", "log", "ln"],
    ["(", ")", "^", "sqrt", "factorial"],
    ["7", "8", "9", "/", "pi"],
    ["4", "5", "6", "*", "e"],
    ["1", "2", "3", "-", "exp"],
    ["0", ".", "C", "+", "="]
]

# --- Define allowed safe functions ---
allowed_funcs = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sqrt": math.sqrt, "log": math.log10, "ln": math.log,
    "pi": math.pi, "e": math.e, "factorial": math.factorial,
    "exp": math.exp, "pow": math.pow
}

# --- Function to safely evaluate ---
def evaluate_expression(expr):
    try:
        expr = expr.replace("^", "**")
        result = eval(expr, {"__builtins__": None}, allowed_funcs)
        return result
    except Exception:
        return "Error"

# --- Layout in columns (like a real calculator) ---
for row in buttons:
    cols = st.columns(5, gap="small")
    for i, label in enumerate(row):
        if cols[i].button(label):
            if label == "C":
                st.session_state.display = ""
            elif label == "=":
                result = evaluate_expression(st.session_state.display)
                st.session_state.display = str(result)
            else:
                st.session_state.display += label

# --- Result display ---
if "display" in st.session_state:
    st.text_input("Output", value=st.session_state.display, label_visibility="collapsed", key="output")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("💻 Built with Streamlit | Inspired by Casio fx-991 | Created with ❤️ in Python")
