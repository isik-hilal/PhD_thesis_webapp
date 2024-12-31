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

    
    # Header for supplementary material
    st.markdown(
        "<h2 style='font-size: 18px;'>Supplementary Material</h2>",
        unsafe_allow_html=True
    )
    # Filepath to the Excel file
    file_path = "./data/taxa.xlsx"

    # Offer the file as a downloadable button
    with open(file_path, "rb") as file:
        st.download_button(
            label="📥 Download Taxa Excel File",
            data=file,
            file_name="taxa.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Add an explanation
    st.markdown(
        """
        <p style='font-size: 14px;'>
        Here you can download <b>Synonyms and presence table</b> for taxa identified in the analyzed studies. 
        </p>
        <ul style='font-size: 14px;'>
            <li><b>Y</b> stands for presence of a taxon under the name given in "Taxon name".</li>
            <li>Other names are explained in the same row.</li>
            <li>Codes are the same as in References.</li>
        </ul>
        """,
        unsafe_allow_html=True
        )

#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
    add_footer()
