import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
def load_data():
    return pd.read_excel("data/gamze2.xlsx", engine="openpyxl")

def show_analysis():
    # Add the title and description for the Analysis section
    st.title("Single View")
    
    # Load the data
    data = load_data()

    # Remove any columns named 'Unnamed: 0' or similar
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

    st.markdown(
        """
        <h2 style=" font-size: 25px;">1-Relative Abundance of Taxa for Each Station/Sample</h2>
        """, unsafe_allow_html=True
    )
    
    # Dropdown for selecting Reference
    st.markdown(
        """
        <h3 style=" font-size: 22px;">Step 1</h3>
        """, unsafe_allow_html=True
    )
    unique_references = data['Reference'].dropna().unique()
    selected_reference = st.selectbox("Choose a Reference:", unique_references)

    if selected_reference:
        # Filter data for the selected reference
        filtered_reference_data = data[data['Reference'] == selected_reference]

        # Display map of stations
        st.markdown(
            """
            <h3 style=" font-size: 22px;">Station Map</h3>
            <p style="font-size: 14px;">The map below shows the stations for the selected reference. Use this to decide which station to select in Step 2.</p>
            """, unsafe_allow_html=True
        )

        # Ensure Latitude and Longitude columns exist
        if 'Lat' in filtered_reference_data.columns and 'Long' in filtered_reference_data.columns:
            # Generate map
            fig_map = px.scatter_mapbox(
                filtered_reference_data,
                lat='Lat',
                lon='Long',
                color='Station',
                hover_name='Station',
                hover_data={'Lat': False, 'Long': False},
                mapbox_style="open-street-map",
                zoom=8,  # Adjust zoom level for better visualization
                height=400
            )
            fig_map.update_layout(
                margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove margins for a clean map
            )
            st.plotly_chart(fig_map)

        # Dropdown for selecting Station
        st.markdown(
            """
            <h3 style=" font-size: 22px;">Step 2</h3>
            """, unsafe_allow_html=True
        )
        unique_stations = filtered_reference_data['Station'].dropna().unique()
        selected_station = st.selectbox("Choose a Station:", unique_stations)

        if selected_station:
            # Filter data for the selected station
            station_data = filtered_reference_data[filtered_reference_data['Station'] == selected_station]

            # Dropdown for selecting Depth_in_core
            st.markdown(
                """
                <h3 style=" font-size: 22px;">Step 3</h3>
                """, unsafe_allow_html=True
            )
            unique_depths = station_data['Depth_in_core'].dropna().unique()
            selected_depth = st.selectbox("Choose a Depth in Core (Sample):", unique_depths)

            if selected_depth:
                # Filter data for the selected depth
                depth_data = station_data[station_data['Depth_in_core'] == selected_depth]

                # Display station and depth details
                st.markdown(f"<h3 style='font-size: 22px;'>Details: </h3>", unsafe_allow_html=True)

                station_details = {
                    "Station": selected_station,
                    "Depth in Core": selected_depth,
                    "TOC": depth_data['TOC'].iloc[0] if 'TOC' in depth_data.columns else 'N/A',
                    "Water Depth": depth_data['Water_depth'].iloc[0] if 'Water_depth' in depth_data.columns else 'N/A',
                }
                for key, value in station_details.items():
                    st.write(f"**{key}:** {value}")

                # Prepare data for fossil analysis (use existing relative abundance values)
                fossil_columns = [
                    col for col in depth_data.columns
                    if col not in {'Code', 'Reference', 'Type', 'Lat', 'Long', 'L/D/U', 'Size_fraction', 'S', 'N',
                                   'Unnamed: 450', 'Station', 'TOC', 'Water_depth', 'Depth_in_core'}
                ]

                fossil_data = depth_data[fossil_columns].sum().reset_index()
                fossil_data.columns = ['Fossil', 'Relative Abundance']
                fossil_data = fossil_data[fossil_data['Relative Abundance'] > 0]  # Filter out fossils with zero relative abundance
                fossil_data = fossil_data.sort_values(by='Relative Abundance', ascending=False)  # Sort by Relative Abundance

                # Group fossils with relative abundance < 2 as 'Others'
                others_abundance = fossil_data[fossil_data['Relative Abundance'] < 2]['Relative Abundance'].sum()
                fossil_data = fossil_data[fossil_data['Relative Abundance'] >= 2]

                if others_abundance > 0:
                    # Add a row for "Others" containing the summed relative abundance of fossils < 2
                    fossil_data = pd.concat([
                        fossil_data,
                        pd.DataFrame([{'Fossil': 'Others', 'Relative Abundance': others_abundance}])
                    ], ignore_index=True)

                # Bar graph of fossils
                st.markdown(
                    """
                    <h3 style=" font-size: 22px;">Benthic Foraminifera Assemblage</h3>
                    """, unsafe_allow_html=True
                )
    
                st.markdown(f"<p style='font-size: 14px;'>The following bar graph shows the <strong>Relative Abundances</strong> of taxa (taxa with abundances <2% are summed in 'Others') found at Station: {selected_station}, Depth in core: {selected_depth} cm.</p>", unsafe_allow_html=True)

                fig = px.bar(
                    fossil_data,
                    y='Fossil',
                    x='Relative Abundance',
                    orientation='h',  # Horizontal bar chart
                    title=f"Relative Abundances of Taxa at Station: {selected_station}, Depth in core: {selected_depth} cm",
                    labels={'Relative Abundance': 'Relative Abundance (%)', 'Fossil': 'Taxa'},
                    color='Relative Abundance',
                    color_continuous_scale='Viridis',
                    height=700
                )
                st.plotly_chart(fig)
    
    # Empty spaces
    st.write("------")






#second part with area graphs
def show_depth_analysis():
    # Add the title and description for the analysis section
    st.markdown(
        """
        <h2 style=" font-size: 25px;">2-Relative Abundances Changing with Depth</h2>
        """ , unsafe_allow_html=True
    )

    # Load the data
    data = load_data()

    # Remove any columns with names containing 'Unnamed'
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

    # Dropdown for selecting Reference
    st.markdown(
        """
        <h3 style=" font-size: 22px;">Step 1</h3>
        """ , unsafe_allow_html=True
    )
    unique_references = data['Reference'].dropna().unique()
    selected_reference = st.selectbox("Choose a Reference:", unique_references, key="depth_analysis_reference")

    if selected_reference:
        # Filter data for the selected reference
        filtered_reference_data = data[data['Reference'] == selected_reference]

        # Dropdown for selecting Station
        st.markdown(
        """
        <h3 style=" font-size: 22px;">Step 2</h3>
        """ , unsafe_allow_html=True
    )
        unique_stations = filtered_reference_data['Station'].dropna().unique()
        selected_station = st.selectbox("Choose a Station:", unique_stations, key="depth_analysis_station")

        if selected_station:
            # Filter data for the selected station
            station_data = filtered_reference_data[filtered_reference_data['Station'] == selected_station]

            # Check if the station has only one unique Depth_in_core value
            if station_data['Depth_in_core'].nunique() == 1:
                # Show a message and do not display any graphs
                st.write("This station has only one sample, so no graphs can be shown due to lack of depth variation.")
                return  # Exit the function early to prevent further processing

            # Prepare data for fossil analysis
            fossil_columns = [
                col for col in station_data.columns
                if col not in {'Code', 'Reference', 'Type', 'Lat', 'Long', 'L/D/U', 'Size_fraction', 'S', 'N',
                               'Unnamed: 450', 'Station', 'TOC', 'Water_depth', 'Depth_in_core'}
            ]

            # Prepare line graphs for each fossil
            st.markdown(""" <div style="text-align: justify; font-size: 14px;">
        The following line graphs show the <strong>Relative Abundances</strong> of each taxa (>2%) changing with depth in the core.
        </div>""", unsafe_allow_html=True
    )

            # Create a container for the graphs
            graph_container = st.container()

            # Filter out fossils that have no data (empty fossil data)
            valid_fossils = []
            for fossil in fossil_columns:
                fossil_data = station_data[['Depth_in_core', fossil]].dropna()
                if not fossil_data.empty and fossil_data[fossil].sum() > 2:
                    valid_fossils.append(fossil)

            # Create the graphs only for valid fossils
            with graph_container:
                # Create rows of columns for displaying graphs
                num_graphs_per_row = 4
                rows = (len(valid_fossils) + num_graphs_per_row - 1) // num_graphs_per_row  # Calculate number of rows needed

                # Loop through rows and create columns for each
                for row_idx in range(rows):
                    # Create the columns for this row (up to 4 per row)
                    columns = st.columns(num_graphs_per_row)

                    # Loop through fossils and plot them
                    for i in range(num_graphs_per_row):
                        fossil_index = row_idx * num_graphs_per_row + i
                        if fossil_index < len(valid_fossils):
                            fossil = valid_fossils[fossil_index]
                            fossil_data = station_data[['Depth_in_core', fossil]].dropna()

                            # Normalize the fossil data to Relative Abundance
                            total_abundance = fossil_data[fossil].sum()
                            if total_abundance > 2:
                                fossil_data['Relative Abundance'] = (fossil_data[fossil] / total_abundance) * 100  # Normalize to percentage

                                # Sort the data by depth to ensure the line graph is continuous and ordered
                                fossil_data = fossil_data.sort_values(by='Depth_in_core')  # Sorting by depth to avoid irregular connections

                                # Create the line graph for the fossil
                                fig = px.line(
                                    fossil_data,
                                    x='Relative Abundance',  # Relative Abundance on the X-axis
                                    y='Depth_in_core',       # Depth_in_core on the Y-axis
                                    title=fossil,
                                    labels={'Relative Abundance': 'Relative Abundance (%)', 'Depth_in_core': 'Depth in Core'},
                                    line_shape='linear')  # Line graph 

                                # Set a fixed x-axis range from 0 to 100 (percentage scale)
                                fig.update_layout(
                                    title=dict(
                                    text=fossil,
                                    font=dict(size=10),  # Set a smaller font size for the title
                                    x=0.5,
                                    xanchor='center',
                                    yanchor='top',
                                ),
                                height=400,  # Make the graph narrow and tall
                                margin=dict(l=10, r=10, t=40, b=10),  # Reduce margins
                                showlegend=False,  # Don't show legend
                                yaxis=dict(
                                    autorange='reversed',  # Reverse the Y-axis to increase depth downward
                                    title=dict(
                                        font=dict(size=8)  # Set a smaller font size for the y-axis label
                                    )
                                ),
                                xaxis=dict(
                                    title=dict(
                                        font=dict(size=8)  # Set a smaller font size for the x-axis label
                                    ),
                                    range=[0, 100]  # Set the x-axis range to be from 0 to 100 (percentage)
                                )
                            )


                                # Display the graph in the respective column
                                with columns[i]:
                                    st.plotly_chart(fig, use_container_width=True)

     

def add_footer():
    st.markdown("""
    <div style="text-align: center; font-size: 10px; margin-top: 30px;">
        <a href="https://github.com/isik-hilal" target="_blank">GitHub</a> | 
        <a href="https://www.linkedin.com/in/hilal-isik/" target="_blank">LinkedIn</a><br>
        <span style="font-size: 8px;">Hilal Işık</span>
    </div>
    """, unsafe_allow_html=True)
