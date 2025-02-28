# streamlit for nice easy UI 

import streamlit as st

if "todos" not in st.session_state:
    st.session_state.todos = []

def selectA(StartInput, todos):
    newtodo = st.text_input("Enter new To Do:")
    if st.button("Add To Do"):
        todos.append(newtodo)
        st.write("To Dos:", todos)

st.write("====================================")
st.write("Select an option: ")
st.write("A for new To Do")
st.write("B for view current To Dos")
st.write("Q for Quit")
st.write("====================================")

StartInput = st.radio("Enter option:", ["A", "B", "Q"])

if StartInput == "A":
    selectA(StartInput, st.session_state.todos)
elif StartInput == "B":
    st.write("Current To Dos:", st.session_state.todos)
elif StartInput == "Q":
    st.write("Goodbye!")
    st.stop()
else:
    st.write("Invalid input, try again")

# streamlit run file
