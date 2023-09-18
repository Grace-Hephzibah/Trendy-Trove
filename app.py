import streamlit as st
import langchain_helper
start = False
st.sidebar.title("Create Fashion Stores")

st.sidebar.multiselect("Wear Types", ("Ethnic Wear", "Western Wear", "Traditional Wear", 
                                               "Casual Wear", "Formal Wear", "Sportswear", 
                                               "Business Casual", "Bohemian Style", "Vintage Style", 
                                               "Streetwear", "Gothic Style", "Preppy Style", 
                                               "Punk Style", "Retro Style", "Festival Wear"), 
                                key = "wear_state")


if st.session_state["wear_state"]:
    st.sidebar.write(st.session_state["wear_state"])


if st.session_state["wear_state"]:

    wear_list = st.session_state["wear_state"]
    wear = " ,".join(wear_list)

    response = langchain_helper.generate_name_and_items(wear)
    st.header(response['name'].strip())
    st.divider()
    menu_items = response['items'].strip().split(",")
    
    st.write("<h3 style='text-align: center;'> Our Top In-store Dresses </h3> ", unsafe_allow_html=True)
    a, b = st.columns(2)
    for item in menu_items[:5]:
        with a:
            st.write("-", item)

    for item in menu_items[5:]:
        with b:
            st.write("-", item)