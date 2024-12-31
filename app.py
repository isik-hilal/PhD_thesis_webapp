import streamlit as st
from home import show_home
from maps import create_first_map, create_second_map
from analysis import show_analysis, show_depth_analysis, add_footer
from references import show_references
from cluster import show_clustermap

# Main application entry point
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": show_home,
        "Maps": show_maps_section,
        "Single View": show_analysis_section,
        "Similarity of Sites": show_cluster_section,
        "References": show_references,
    }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Render the selected page
    pages[selected_page]()



# Maps section handler
def show_maps_section():
    
    st.subheader("General Map Showing All Data Points")
    create_first_map()

    st.subheader("Filtered Map by Reference")
    create_second_map()

    # Add footer to the Maps section
    add_footer()

# Analysis section handler (includes multiple analyses)
def show_analysis_section():

    show_analysis()
    
    show_depth_analysis()

    # Add footer to the Maps section
    #empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
    add_footer()

# clustering
def show_cluster_section():
    #show the

    show_clustermap()



if __name__ == "__main__":
    main()
