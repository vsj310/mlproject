import streamlit as st
import pandas as pd

# Create a DataFrame to store gig data
gigs_df = pd.DataFrame(columns=["Title", "Description", "Price"])

# Sidebar for gig submission
st.sidebar.header("Submit Your Gig")
title = st.sidebar.text_input("Title")
description = st.sidebar.text_area("Description")
price = st.sidebar.number_input("Price", step=0.01, format="%.2f")

if st.sidebar.button("Submit"):
    gigs_df = gigs_df.append({"Title": title, "Description": description, "Price": price}, ignore_index=True)
    st.success("Gig submitted successfully!")

# Main content
st.title("Welcome to Fiverr Clone!")
st.subheader("Browse Gigs")

if gigs_df.empty:
    st.info("No gigs available yet. Be the first to submit!")
else:
    st.dataframe(gigs_df)

# Filter gigs by price
price_filter = st.slider("Filter by price", 0.0, 1000.0, (0.0, 1000.0))
filtered_gigs = gigs_df[(gigs_df["Price"] >= price_filter[0]) & (gigs_df["Price"] <= price_filter[1])]

if not filtered_gigs.empty:
    st.subheader("Filtered Gigs")
    st.dataframe(filtered_gigs)

  