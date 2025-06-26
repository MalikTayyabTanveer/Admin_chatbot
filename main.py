import streamlit as st
from dbintial import init_db
from LLM import parse_with_llm
import sqlite3

st.title("Admin Chatbot with LLM")

conn = init_db()
c = conn.cursor()

# Chat input
msg = st.text_input("Type your command:")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Send") and msg:
    parsed = parse_with_llm(msg)
    intent = parsed.get("intent")
    email = parsed.get("email")
    name = parsed.get("name")
    phone = parsed.get("phone")
    city = parsed.get("city")

    if intent == "add" and email:
        try:
            c.execute("INSERT INTO users (email, name, phone, city) VALUES (?, ?, ?, ?)",
                      (email, name or "", phone or "", city or ""))
            conn.commit()
            response = f"User {email} added successfully."
        except sqlite3.IntegrityError:
            response = f"User {email} already exists."

    elif intent == "remove" and email:
        c.execute("DELETE FROM users WHERE email = ?", (email,))
        conn.commit()
        if c.rowcount:
            response = f"User {email} removed."
        else:
            response = f"User {email} not found."

    elif intent == "update" and email:
        updates = []
        params = []
        if name:
            updates.append("name = ?")
            params.append(name)
        if phone:
            updates.append("phone = ?")
            params.append(phone)
        if city:
            updates.append("city = ?")
            params.append(city)

        if updates:
            query = f"UPDATE users SET {','.join(updates)} WHERE email = ?"
            params.append(email)
            c.execute(query, params)
            conn.commit()
            if c.rowcount:
                response = f"User {email} updated successfully."
            else:
                response = f"User {email} not found."
        else:
            response = "No valid fields to update."

    else:
        response = "Sorry, I couldn't understand or process that command."

    st.session_state.history.append(("You", msg))
    st.session_state.history.append(("Bot", response))

for who, text in st.session_state.history:
    st.markdown(f"**{who}:** {text}")
