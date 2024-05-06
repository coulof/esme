import streamlit as st

def main():
    # Create a form to collect user input
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Create a button to submit the form
    if st.button("Submit"):
        # if password is shorter than 12 character error
        if len(password) < 12:
            st.error("Password must be at least 12 characters long.")
            return
        # Write the data to a file
        with open("user_data.txt", "a") as file:
            file.write(f"Full Name: {full_name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Password: {password}\n\n")

        st.success("Data saved successfully!")

if __name__ == "__main__":
    main()
