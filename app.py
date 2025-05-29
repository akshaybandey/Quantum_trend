import streamlit as st
import pandas as pd
import os

# Load clustering results
df = pd.read_csv("clustered_papers.csv")
input_folder = "abstract_intro"

# Sidebar filter
st.sidebar.title("Cluster Filter")
cluster_ids = sorted(df["cluster"].unique())
selected = st.sidebar.multiselect("Select Cluster(s)", cluster_ids, default=cluster_ids)

# Main content
st.title(" Quantum Papers Cluster Viewer")
st.write(f"Showing files from {len(selected)} clusters.")

filtered = df[df["cluster"].isin(selected)]
for _, row in filtered.iterrows():
    st.markdown(f"###  {row['filename']}")
    with open(os.path.join(input_folder, row["filename"]), "r", encoding="utf-8") as f:
        st.write(f.read())
    st.caption(f"Cluster: {row['cluster']}")
    st.markdown("---")
