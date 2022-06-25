import streamlit as st

st.set_page_config(page_title="Teeth check", initial_sidebar_state="collapsed")


from stlib import advice, analyze


with st.sidebar:
    st.markdown("")
    page = st.selectbox("Select:", ["Анализ", "Полезные советы"])


match page:
    case "Полезные советы":
        advice.run()
    case _:
        analyze.run()
