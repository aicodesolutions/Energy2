import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "John Miller", "Jennifer Johnson"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose User Profile", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
request_1 = st.Page(
    "user1/dashboard1.py",
    title="Dashboard",
    icon=":material/help:",
    default=(role == "John Miller"),
)
request_2 = st.Page(
    "user1/user1chat.py", title="Chat", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "user2/dashboard2.py",
    title="Dashboard",
    icon=":material/healing:",
    default=(role == "Jennifer Johnson"),
)
respond_2 = st.Page(
    "user2/user2chat.py", title="Respond 2", icon=":material/handyman:"
)


account_pages = [logout_page]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]


st.title("Intelligent Energy")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["John Miller", "Admin"]:
    page_dict["John Miller"] = request_pages
if st.session_state.role in ["Jennifer Johnson", "Admin"]:
    page_dict["Jennifer Johnson"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation( page_dict | {"Account": account_pages})
else:
    pg = st.navigation([st.Page(login)])

pg.run()