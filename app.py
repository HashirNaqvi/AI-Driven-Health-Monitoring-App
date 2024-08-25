import streamlit as st
import pandas as pd
from datetime import datetime

# Mock data for demonstration purposes
mood_data = {
    'Date': pd.date_range(start='2023-08-01', periods=30),
    'Mood': [3, 4, 5, 2, 3, 4, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 4, 3, 5, 4]
}
mood_df = pd.DataFrame(mood_data)

# Sample data to simulate user profiles and reminders
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "reminders": []
}

# Function to display the mental health dashboard
def mental_health_dashboard():
    st.title("Mental Health Monitoring Dashboard")

    # Dashboard Overview
    st.header("Overview")
    st.write("Welcome to your Mental Health Dashboard. Here you can track your mood, write daily journals, and receive personalized insights.")

    # Mood Tracking
    st.subheader("Daily Mood Tracker")
    mood = st.slider("How are you feeling today?", min_value=1, max_value=5, value=3)
    st.write("Mood Value: ", mood)

    # Journal Entry
    st.subheader("Daily Journal")
    journal_entry = st.text_area("How was your day? Share your thoughts and feelings.")
    if st.button("Analyze Journal"):
        st.write("Analyzing your journal...")
        # Mock response for AI analysis
        emotion_analysis = "Positive"
        st.write(f"Detected Emotion: {emotion_analysis}")

    # Insights and Recommendations
    st.subheader("Insights & Recommendations")
    st.write("Based on your recent activities, we recommend taking a short walk and practicing mindfulness meditation.")

    # Progress Visualization
    st.subheader("Mood Trend Over Time")
    st.line_chart(mood_df.set_index('Date')['Mood'])

    # Real-Time Alerts
    st.subheader("Real-Time Alerts")
    st.warning("You have been feeling low for the past 3 days. Consider talking to a friend or a professional.")

    # Display Journal History
    st.subheader("Journal History")
    st.write("Here’s what you’ve written in the past week:")
    journal_history = ["Day 1: Feeling good!", "Day 2: A bit stressed.", "Day 3: Today was a tough day."]
    for entry in journal_history:
        st.write(entry)

# Function to display user profile
def display_profile():
    st.subheader("Profile Management")
    name = st.text_input("Name", user_data["name"])
    email = st.text_input("Email", user_data["email"])
    
    if st.button("Update Profile"):
        user_data["name"] = name
        user_data["email"] = email
        st.success("Profile updated successfully!")

# Function to set reminders
def set_reminder():
    st.subheader("Set a Reminder")
    reminder_text = st.text_input("Reminder Text")
    reminder_date = st.date_input("Reminder Date", datetime.now())
    reminder_time = st.time_input("Reminder Time", datetime.now().time())

    if st.button("Add Reminder"):
        reminder_datetime = datetime.combine(reminder_date, reminder_time)
        user_data["reminders"].append({"text": reminder_text, "time": reminder_datetime})
        st.success("Reminder added!")

# Function to display reminders
def display_reminders():
    st.subheader("Your Reminders")
    if user_data["reminders"]:
        reminders_df = pd.DataFrame(user_data["reminders"])
        st.table(reminders_df)
    else:
        st.write("No reminders set.")

# Main application
def main():
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Profile", "Set Reminders", "View Reminders"])

    if page == "Dashboard":
        mental_health_dashboard()
    elif page == "Profile":
        display_profile()
    elif page == "Set Reminders":
        set_reminder()
    elif page == "View Reminders":
        display_reminders()

if __name__ == "__main__":
    main()
