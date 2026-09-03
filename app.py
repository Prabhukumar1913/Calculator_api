import streamlit as st
st.title("Calculator Application")
number1=st.number_input("Insert a number",placeholder="Enter your first number")
number2=st.number_input("Insert a number",placeholder="Enter your second number")

operation=st.selectbox("Select the operation",("add","sub","mul","div"))
ret=st.button("Calculate")
if ret:
    if operation=="add":
        st.write(number1+number2)
    elif operation=="sub":
        st.write(number1-number2)
    elif operation=="mul":
        st.write(number1*number2)
    elif operation=="div":
        st.write(number1/number2)
    st.write("button is clicked")
    # st.balloons()