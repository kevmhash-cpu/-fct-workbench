import streamlit as st
import json
from fct_engine import analyze_graph

st.title("FCT Workbench (Prototype)")

st.write("Upload a JSON graph with nodes and edges.")

uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

if uploaded_file is not None:
    try:
        graph = json.load(uploaded_file)
        result = analyze_graph(graph)

        st.subheader("Analysis Result")
        st.json(result)

    except Exception as e:
        st.error(f"Error reading file: {e}")
