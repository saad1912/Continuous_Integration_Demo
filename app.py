import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its Square, Cube and Fifth power")

n = st.number_input("Enter a  number ", value=1, step=1)

#Calculate Results

square = n**2
cube = n**3
fifth_power = n**5

st.write(f"The Square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth power of {n} is {fifth_power}")

