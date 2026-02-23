import json
import streamlit as st
from test_data_visualization import test_json_to_dataframe


def main():
    st.title("ZumbaStats")
    st.header("Work in progress 🛠️")

    st.header("This is just a test")
    with open("data/zumba4/test_report.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    st.dataframe(test_json_to_dataframe(data))


if __name__ == "__main__":
    main()