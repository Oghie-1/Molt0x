import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)


st.write("-------")
col1, col2, col3= st.columns(3)
with st. container():

    with col1:
        

    with col2:
        img = Image.open("./media/img/home.png") 
        n_img = img.resize ((300, 200))   
        st.image(n_img)          
st.write("-------")


with st.sidebar:
    st.write("MOLT0x - Better Than Your Usual Bank.")

    tab1, tab2, tab3 = st.tabs(["FAQs", "About", "Learn"])

    with tab1:
        st.header("FAQs")

    with tab2:
        st.header("About")
        st.write("-----")
        st.subheader("We provide access to a host of finanical Instrument")
        st.subheader("Save Transfer Loan Escrow")


    with tab3:
        st.header("Learn")

    st.sidebar.write("We are defining the Banking Experience")

    st.subheader("Subscribe to our newsletter")

    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Please enter your email address')
    submit_e_button = email_form.form_submit_button(label='Signup')

    if submit_e_button:
        st.write("Welcome")
        st.subheader("for the latest news on new features, financial tips, tidbits and for our wonderful community.")
        st.header("Visit Blog")




col4, col5 = st.columns(2)

with st.container():
    with col4:
        st.header("Accounts")
        img = Image.open("./media/img/on.png")
        n_img = img.resize((500, 200))
        st.image(n_img)
    with col5:
        with st.container():

            option = st.selectbox('Account Info',('Account Bal', 'Savings', 'Transfer', 'Withdraw'))
            st.write('Option Selected:', option)


st.write("________")
col6, col7, col8 = st.columns(3)
with st.container():

    with col6:
        st.write("123")

        
        
with st.container():

    img = Image.open("./media/img/earn.png")
    n_img = img.resize((500, 250))
    st.image(n_img)






       
    







            

 