import streamlit as st
import sqlite3
import datetime
import pandas as pd

# --- Database setup ---
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS attendance(
                                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        name TEXT,
                                                        date TEXT,
                                                        status TEXT
               )
               """)
conn.commit()

# --- App UI ---
st.title("🏫 School Attendance System")
st.image("logo.png", caption="Smart Attendance Dashboard")

# Sidebar
st.sidebar.header("Menu")
menu = st.sidebar.radio("Select Action", ["Mark Attendance", "View Records", "Prompt Mode"])

# Student List
students = ["Alice", "Bob", "Charlie", "David", "Emma"]

# --- Mark Attendance ---
if menu == "Mark Attendance":
    st.subheader("Mark Attendance for Today")
    date = datetime.date.today()
    attendance_data = {}

    for student in students:
        status = st.radio(f"{student}", ["Present", "Absent"], key=student)
        attendance_data[student] = status

    if st.button("Save Attendance"):
        for student, status in attendance_data.items():
            cursor.execute("INSERT INTO attendance (name, date, status) VALUES (?, ?, ?)",
                           (student, date, status))
        conn.commit()
        st.success("✅ Attendance saved successfully!")

# --- View Records ---
elif menu == "View Records":
    st.subheader("Attendance Records")
    df = pd.read_sql("SELECT * FROM attendance", conn)
    st.dataframe(df)

    # Chart
    if not df.empty:
        chart_data = df.groupby("status").size().reset_index(name="count")
        st.bar_chart(chart_data.set_index("status"))

# --- Prompt Mode ---
elif menu == "Prompt Mode":
    st.subheader("💬 AI-Style Prompt Interface")
    user_prompt = st.text_input("Enter your command (e.g. 'Show me absentees today')")

    if st.button("Run Prompt"):
        today = datetime.date.today().isoformat()

        if "absentees" in user_prompt.lower():
            df = pd.read_sql(f"SELECT name FROM attendance WHERE date='{today}' AND status='Absent'", conn)
            st.write("🚫 Absentees Today:")
            st.table(df)
        elif "present" in user_prompt.lower():
            df = pd.read_sql(f"SELECT name FROM attendance WHERE date='{today}' AND status='Present'", conn)
            st.write("✅ Present Students:")
            st.table(df)
        else:
            st.warning("Prompt not recognized. Try: 'Show me absentees today' or 'Show me present students'")

st.sidebar.write("Developed by Prompt Engineer 👩‍💻")
