#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
import random
import tkinter
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
# image = Image.open('assets/logo.jpg')
with title_container:
    # with col1:
       # st.image(image)
    with col2:
        st.title('Password Generator')
        st.markdown("""
Create strong Passwords to protect your accounts

""")
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*()#.,?0123456789'
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input

pass_len = st.number_input('Enter password Length', min_value=4, max_value=50)
st.write(pass_len)


#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function

def generate_password(len):
    password = ''
    for pwd in range(len):
        password += random.choice(chars)
    return password

gen = st.button('Generate')
st.subheader('Here is your password:')
if gen:
    st.write(generate_password(pass_len))
#----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer


footer="""<style>

#MainMenu {visibility: hidden;}
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit with ❤️ by <a href='https://github.com/mayursrt'>Mayur</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



############################################################################################################################# 
#############################################################################################################################
