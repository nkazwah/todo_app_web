import streamlit as st


import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)



st.title('My todo app')
st.subheader('This is my todo list')
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo , key=todo )
    if checkbox:
        print("selected box: " + str(checkbox))
        print("checked: " + todo)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Type something', placeholder='Add new todo...', on_change=add_todo , key='new_todo')
