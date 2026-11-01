
import streamlit as st

st.title("🎓 Student Task Manager")

st.write("Manage your daily college tasks!")

# Get task from user
task = st.text_input("Enter a task")

# Add task button
if st.button("Add Task"):
    if task:
        st.success("Task added: " + task)
    else:
        st.warning("Please enter a task!")

# Display some tasks
st.header("My Tasks")

st.checkbox("Complete Python assignment")
st.checkbox("Study Mathematics")
st.checkbox("Revise Cybersecurity")
st.checkbox("Prepare for Hackathon")
