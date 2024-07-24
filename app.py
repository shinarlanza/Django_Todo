import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import requests

st.set_page_config(page_title="My Todo List", page_icon=":tada", layout="wide")

st.title("Todo List")
st.write("v.0.0.1")

api_url = "http://127.0.0.1:8000/api/todo/"


def fetch_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data


def sent_data(title, details):
    try:
        data = {"title": title, "details": details}
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Something went wrong: {e}")
        return None


st.write("---")
right_column, left_column = st.columns(2)

with left_column:

    with st.container():
        st.subheader("List")
        data = fetch_data(api_url)

    if data:
        df = pd.DataFrame(data)

        st.data_editor(df, num_rows="dynamic")


with right_column:
    with st.container():
        st.subheader("New ")
        title = st.text_input("Title")
        details = st.text_area("Details")

        if st.button("Add Todo"):
            response = sent_data(title, details)
            if response is not None and response.status_code == 201:
                st.success("Todo created.")
                st.experimental_rerun()  # Use st.experimental_rerun instead of st.rerun
            else:
                st.error("Something went wrong.")
