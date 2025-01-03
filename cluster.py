import streamlit as st
import pandas as pd
import plotly.express as px
from analysis import add_footer


# Load the data
def load_data():
    data = pd.read_csv("data/cluster.csv")  # Loading CSV data
    data.columns = data.columns.str.strip() 
    data = data.sort_values(by='Cluster/Subcluster', ascending=True)
    data['Cluster/Subcluster'] = data['Cluster/Subcluster'].astype('object') # Strip any leading/trailing spaces
    return data

# Function to show the map
def show_clustermap():
    # Load the data
    data = load_data()
    # Title for the references section
    st.title("Similarity of Sites")
    st.image("images/cluster.png", caption="Cluster Image", use_container_width=True)

    st.markdown("""
                <p style="text-align:justify; font-size:14px;">
                Dendrogram produced from the cluster analysis (hierarchical clustering, 
                UPGMA, Bray-Curtis, PAST, Hammer et al., 2001) of surface data set (384 taxa (<em>See Supplementary Material in References Section</em>), 144 stations). 
                A: Station numbers (shortened as "study code (see References)_station number", 
                without using SoM prefix, and MAR prefix in SoM-11, MRS06: MRS-DV05-PC-06, 
                MRS04: MRS-DV01-PC-04, TS_IzDeep: SoM_TS_Izmit-deep, 
                other stations of this study shortened to first few characters only) in clusters,
                colored according to location (see legend A); 
                B: water depths the stations belong to (see legend B); 
                C: dendrogram cut from about 32% similarity resulting in 15 separate clusters of stations,
                clusters and subclusters enumerated (as C#) starting from the root of the tree; 
                station numbers colored according to studied size fraction (see legend C).
                <br><br>
                Locations of the stations belonging to 18 clusters/subclusters (15 separate clusters and 
                2 and 3 subclusters of Cluster 12 and 13 respectively) can be visualized in the map below.
                <br><br>
                "Details" in the info-box stand for distinguishing feature of the cluster/sublcluster in terms of dominant assemblage, studied assemblage or pollution.
</p>""",
    unsafe_allow_html=True)


    # Check if 'Cluster' column exists
    if 'Cluster/Subcluster' not in data.columns:
        st.error("The 'Cluster' column is missing in the data.")
        return

    # Add the title and description for the Map section
    st.markdown(
        """
        <h2 style=" font-size: 25px;">Interactive Map of Clusters</h2>
        """ , unsafe_allow_html=True
    )

    # Dropdown for selecting clusters
    st.markdown(
        """
        <h3 style=" font-size: 22px;">Select Clusters</h3>
        """ , unsafe_allow_html=True
    )
    
    # Get unique cluster values from the 'Cluster' column
    unique_clusters = data['Cluster/Subcluster'].dropna().unique()
    
    # User can select multiple clusters
    selected_clusters = st.multiselect("Choose Clusters to display:", unique_clusters, default=unique_clusters[0]) #default=unique_clusters)

    if selected_clusters:
        # Filter data based on selected clusters
        filtered_data = data[data['Cluster/Subcluster'].isin(selected_clusters)]

        # Ensure that the latitude and longitude columns exist in the data
        if 'Latitude' not in filtered_data.columns or 'Longitude' not in filtered_data.columns:
            st.error("Latitude and Longitude columns are missing in the data.")
            return

        # Get bounding box for dynamic zoom
        lat_min, lat_max = filtered_data['Latitude'].min(), filtered_data['Latitude'].max()
        lon_min, lon_max = filtered_data['Longitude'].min(), filtered_data['Longitude'].max()

        # Calculate center of the map for better zooming (mean of latitudes and longitudes)
        lat_center = (lat_min + lat_max) / 2
        lon_center = (lon_min + lon_max) / 2

        # Create a list of colors (15 colors for 15 clusters)
        colors = [
    "#1f77b4",  # Blue
    "#8c564b",  # Brown
    "#d49a6a",  # Light Brown
    "#b5634f",  # Burnt Orange
    "#bcbd22",  # Yellow-green
    "#e377c2",  # Pink
    "#7f7f7f",  # Gray
    "#8e44ad",  # Purple
    "#f1c40f",  # Gold
    "#ba55d3",  # Lavender
    "#ff7f0e",  # Bright Orange
    "#2ca02c",  # Green
    "#ffbb78",  # Peach
    "#17becf",  # Cyan
    "#9b59b6",  # Amethyst
    "#ff6347",  # Tomato Red
    "#4682b4",  # Steel Blue
    "#32cd32",  # Lime Green
]

        # Ensure that clusters have unique colors by using color_discrete_map
        color_map = {cluster: colors[i] for i, cluster in enumerate(unique_clusters)}

        # Create a map with points for the selected clusters
        fig = px.scatter_mapbox(
            filtered_data,
            lat='Latitude',  # Latitude column
            lon='Longitude',  # Longitude column
            color='Cluster/Subcluster',  # Cluster column for different colors
            hover_name='Reference',  # Hover name (can show more info in hover)
            hover_data={
                'Reference': False,
                'Station': True,
                'Details':True,
                'Latitude': False,
                'Longitude': False
            },
            color_discrete_map=color_map,  # Use the custom color map
            mapbox_style="open-street-map",  # Map style
            zoom=7,  # Zoom level (will be overwritten dynamically)
            center={"lat": lat_center, "lon": lon_center},  # Center the map dynamically
            height=600
        )

        fig.update_traces(marker=dict(opacity=0.7, size=10))

        # Update the map zoom to ensure the points are visible
        fig.update_layout(
            mapbox=dict(
                bearing=0,
                pitch=0,
                zoom=7,  # Can adjust this further depending on the spread of the points
                center={"lat": lat_center, "lon": lon_center}
            )
        )

        # Show the map
        st.plotly_chart(fig)

    # Empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
    add_footer()
