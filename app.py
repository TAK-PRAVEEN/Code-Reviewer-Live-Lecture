import streamlit as st

from code_parser import parse_code
from style_checker import show_style_corrected

st.title("AI Code Reviewer")
code = st.text_area("Code: ")

if st.button("Analysis"):
    if code:
        result = parse_code(code)
        result1 = show_style_corrected(code)
        if result["success"]:
            st.success("Parsed!")
            st.code(result1, language="python")
        else:
            st.error(result["error"]["message"])
    else:
        st.warning("Please enter some code first!")