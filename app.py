import streamlit as st

st.set_page_config(layout="centered") 
# Define the pages for the Streamlit app
about_page = st.Page(
    page = "multi_pages/about.py",
    title = "About",
    icon = ":material/info:",
    default = True
)
restriction_page = st.Page(
    page = "multi_pages/restriction.py",
    title = "Restriction",
    icon = ":material/lock:"
)

main_page = st.Page(
    page = "multi_pages/main.py",
    title = "Main",
    icon = ":material/picture_as_pdf:"
)



pg = st.navigation(
    pages = [main_page, restriction_page, about_page])

st.logo("assests/Background.png",)
#st.sidebar.image("assests/Logo1.png", use_container_width=True)
st.sidebar.text("Made with ❤️ by Kushal")

pg.run()
