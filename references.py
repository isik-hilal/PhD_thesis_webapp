import streamlit as st
import pandas as pd
from analysis import add_footer

def show_references():
    # Title for the references section
    st.title("References")


    
    # give some empty spaces in between
    st.markdown("<br>", unsafe_allow_html=True)

    # Load the references from the CSV file
    try:
        # Path to your references CSV file
        references_df = pd.read_csv('data/references.csv')

        # Check if the CSV loaded correctly
        if references_df.empty:
            st.write("No references found.")
        else:
            # Display the references in a readable format
            st.subheader("Key References:")
            
            for index, row in references_df.iterrows():
                # Displaying each reference in a structured way
                #st.markdown(f"<p style='font-size: 14px;'>{row['Code']}, **{row['Authors']}**, {row['Title']}, {row['Year']}, {row['Link']}.</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 14px;'>{row['Code']}, <strong>{row['Authors']}</strong>, {row['Title']}, {row['Year']}, <a href='{row['Link']}' target='_blank'>{row['Link']}</a>.</p>", unsafe_allow_html=True)
   
                st.write("------")

    except Exception as e:
        # If there is an error reading the CSV, show a message
        st.error(f"Error loading references: {e}")

#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
    add_footer()
