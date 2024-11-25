import streamlit as st
#st.set_page_config(page_title="Invento Logo Existo🐑", page_icon="🐑", layout="wide")

forms = st.Page("pages/forms.py", title="Queremos te conhecer!", icon=":material/confirmation_number:", default=True)

pg = st.navigation(
    {
    "Conhecendo nosso cliente": [forms, ],
    }
)
pg.run()
