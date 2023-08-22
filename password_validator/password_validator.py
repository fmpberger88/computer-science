import random
import string
import streamlit as st


def is_special_char(char):
    special_chars = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
    return ord(char) in special_chars


def password_validator(password):
    pass_length = len(password)
    contains_number = any(char.isdigit() for char in password)
    contains_sonderzeichen = any(is_special_char(char) for char in password)
    contains_uppercase = any(char.isupper() for char in password)
    contains_lowercase = any(char.islower() for char in password)

    if pass_length >= 8 and contains_number and contains_sonderzeichen and contains_uppercase and contains_lowercase:
        return "Strong"
    elif pass_length >= 8 and (contains_number or contains_sonderzeichen) and contains_uppercase and contains_lowercase:
        return "Good"
    else:
        return "weak"

def generate_password():
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(charset) for _ in range(8))

st.title("Check Password Strength")
password = st.text_input("Enter your password:", type="password")

if password:
    strength = password_validator(password)
    st.write(f'Password strength: {strength.title()}')

st.subheader("Password Hints:")
st.markdown("- The password should be at least 8 characters long.")
st.markdown("- The password should contain both uppercase and lowercase letters.")
st.markdown("- The password should have at least one number.")
st.markdown("- The password should have at least one special character (e.g., #, !, $, %, etc.).")

if st.button('Generate Random Password'):
    random_password = generate_password()
    st.write("Your generated password:", random_password)