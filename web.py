import streamlit as st
import funcions

todos = funcions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    funcions.write_todos(todos)


st.title("My todo App")
st.subheader("this is my todo app.")
st.write("This app is to increase productivity.")


for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        funcions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a new to-do...", on_change=add_todo,
              key='new_todo')
