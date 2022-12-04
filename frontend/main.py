import streamlit as st
from PIL import Image
#import web3py

# DB Management
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username, password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',
	          (username, password))
	conn.commit()



st.set_page_config(page_title="Home", page_icon="👋")
st.markdown("# Molt0x")
st.sidebar.header("Home")


def main():
    selected_box = st.sidebar.selectbox('Menu', ('Home', 'Login', 'Account', 'Support'))

    if selected_box == 'Home':
        home()
    if selected_box == 'Login':
        login()
    if selected_box == 'Account':
        account()
    if selected_box == 'Support':
        support()


st.sidebar.subheader("We provide access to a host of finanical Instrument")



def home():
    st.title("Molt0x")

    st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
     + ' from the left. I have implemented only a few to show how it works on Streamlit. ' +
                 'You are free to add stuff to this app.')
    
    img = Image.open("./media/img/home.png")
    n_img = img.resize((300, 200))
    st.image(n_img, use_column_width=True)



def login():

    st.title('Bank of The Truely Free')

    # Create an empty container
    placeholder = st.empty()

    actual_email = "email"
    actual_password = "password"

    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        col1, col2, col3, col4= st.columns(4)

        with col1:
            st.form_submit_button("Login")

        with col3:
            st.form_submit_button('Forgot password')
            if st.form_submit_button == 'Forgot password':
                return forgot_password()
        with col4:
            submitted = st.form_submit_button('Sign Up')
            if submitted:
                signup()

    if st.form_submit_button and email == actual_email and password == actual_password:
        # If the form is submitted and the email and password are correct,
        # clear the form/container and display a success message
        placeholder.empty()
        st.success("Login successful")
    elif st.form_submit_button and email != actual_email and password != actual_password:
        st.error("Login failed")



def signup():

    st.subheader("Create an Account")
    new_user = st.text_input('Username')
    email = st.text_input(label='Please enter your email address')
    passwrrd = st.text_input(label='Password', type='password')
    new_passwd = st.text_input('Confirm  Password')
    st.button('SignUp', on_click=callable)

    if st.button('SignUp') and passwrrd == new_passwd:
        create_usertable()
        add_userdata(new_user, email, make_hashes(new_passwd))
        st.success("You have successfully created an account.Go to the Login Menu to login")


    
def account():
    st.subheader("Save " + "Tranfer " + "Loan ")
    st.subheader("All these are some of our services")

    with st.container():
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Statement", "Send", "Transfer", "Balance", "Deposit", "Withdraw"])

        
        with tab1:
            with st.form("my_form"):
                st.write("Statement")
                submitted = st.form_submit_button("Check Statement")
                if submitted:
                    st.write("Statement: ")
                    


        with tab2:
            st.header("Send")
            with st.form("send"):
                st.write("Send Token")
                submitted = st.form_submit_button("Send")
                if submitted:
                    st.write("Sent: ")

            st.write("-----")
        
        with tab3:
            st.header("Transfer")
            with st.form("Trf"):
                st.write("Transfer")
                submitted = st.form_submit_button("Transfer")
                if submitted:
                    st.write("Transferred ")
            st.write("-----")
        
        with tab4:
            st.header("Balance")
            with st.form("bal"):
                st.write("Balance")
                submitted = st.form_submit_button("Check Balance")
                if submitted:
                    st.write("Balance: ")
            st.write("-----")
        
        with tab5:
            with st.form("dep"):
                st.write("Deposit")
                submitted = st.form_submit_button("Deposit")
                if submitted:
                    st.write("Deposit: ")
            img = Image.open("./media/img/sv.png")
            n_img = img.resize((300, 200))
            st.image(n_img, use_column_width=True)
            st.write("-----")
        
        with tab6:
            st.header(" Withdraw")
            with st.form("withdrwn"):
                withdrawn_amt = st.text_input("Amount")
                submitted = st.form_submit_button("Withdraw")
                if submitted:
                    st.write("Withdrawn To: ")
            st.write("-----")
            

    st.title("MOLT0x - Better Than Your Usual Bank.")
    img = Image.open("./media/img/on.png")
    n_img = img.resize((300, 200))
    st.image(n_img, use_column_width=True)



def support():

    st.title('check out our materials below')
    st.write("Hello", src=("./Molt0x.py"))

def forgot_password():
    st.write("Get New Pass")



  
if __name__ == "__main__":
    main()
