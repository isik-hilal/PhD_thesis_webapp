import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots


# Read the data
def load_data():
    # Load the data from the Excel file (make sure it's in the 'data' folder)
    data = pd.read_excel("data/gamze2.xlsx", engine="openpyxl")
    
    return data

# First Map: General map showing all data points with different colors
def create_first_map():
    datatoc = load_data()

    # Display information above the map
    st.write(
        """
        **About this map**: This interactive map shows in total **144 stations** coming from **11 different quantitative benthic foraminifera studies** 
        (including this study).
        """
    )
    
    # Define custom colors for the references
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
    ]

    # Create the map with Plotly
    fig1 = px.scatter_mapbox(
        datatoc,
        lat='Lat',
        lon='Long',
        hover_name='Reference',
        hover_data={
            'Reference': False,
            'Lat':False,
            'Long':False,
            'Station':True,
            'Type': True,
            'Depth_in_core': True,
            'Water_depth': True,
            'TOC': True,
            'L/D/U': True,
            'S': True,
            'N': True
        },
        color='Reference',
        color_discrete_sequence=colors,  # Use the custom color palette
        zoom=5,
        height=600
    )

    fig1.update_traces(marker=dict(opacity=0.7, size=10))  # Set marker transparency and size

    fig1.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=40.8, lon=28.5),
            zoom=7
        ),
        title=dict(
            text="<b>Sea of Marmara Station Locations</b>",
            font=dict(family="Lora, Roboto, sans-serif", size=20),
            x=0.5,
            xanchor="center"
        ),
        margin={"r":0, "t":50, "l":0, "b":0}
    )

     # Display the map in Streamlit
    st.plotly_chart(fig1)

    # Add the note
    st.markdown(
    """
    <p style="font-size:10px; font-style:italic; color:gray;">
    The purple borders are administrative or jurisdictional boundaries included in the OpenStreetMap base layer. 
    These can represent country, state, or municipality borders, and they are part of the default map.
    </p>
    """,
    unsafe_allow_html=True)

    # Add info box explanation
    st.markdown(
        """
        <h3 style=" font-size: 10px;">Explanation of Info Box</h3>
        <p style="font-size:10px;">
        <strong>Type:</strong> Core (C) or Grab (G)<br>
        <strong>Station:</strong> Station name, original, as in publications.<br>
        <strong>Depth_in_core:</strong> (cm) for type =core (C) the bottom level of sampled interval (e.g. Depth_in_core = 4 for sampling between 2-4 cm); for type = grab (G) 0.5 cm unless otherwise specified in the reference.<br>
        <strong>Water depth:</strong> station water depth (m)<br>
        <strong>TOC:</strong> total organic carbon, as percentage."-" If data do not exists. TOC for SoM_2 taken from du Chatelet et al. 2013.<br>
        <strong>L/D/U:</strong> Studied type of assemblage, live/dead/undifferentiated<br>
        <strong>Size_fraction:</strong> Studied size fraction, micrometers<br>
        <strong>S:</strong> Number of identified taxa in the study<br>
        <strong>N:</strong> Counted number of foraminifera, as reported in publications, "-" if data do not exist<br></p>
    """, unsafe_allow_html=True)



# Second Map: Map with dropdown to filter by reference
def create_second_map():
    datatoc = load_data()
    
    # Dropdown for selecting reference
    unique_references = datatoc['Reference'].unique()
    selected_reference = st.selectbox("Select a Reference", unique_references)
    
    # Filter data based on the selected reference
    filtered_data = datatoc[datatoc['Reference'] == selected_reference]

    # Define custom colors for the references
    
    reference_color_map = {
        "Fontanier et al. 2018": "#1f77b4",  # Blue
        "Phipps et al. 2010": "#8c564b",  # Brown
        "Kırcı-Elmas 2006": "#d49a6a",  # Light Brown
        "Kırcı-Elmas 2018": "#b5634f",  # Burnt Orange
        "Kırcı-Elmas 2013": "#bcbd22",  # Yellow-green
        "Avşar 2010": "#e377c2",  # Pink
        "Kırcı-Elmas et al. 2008": "#7f7f7f",  # Gray
        "Kaminski et al. 2002": "#8e44ad",  # Purple
        "Avşar et al. 2006": "#f1c40f",  # Gold
        "Alavi 1988": "#ba55d3",  # Lavender
        "This study": "#ff7f0e",  # Bright Orange
    }
    
     # Ensure all `Reference` values in filtered_data exist in the color map
    filtered_data = filtered_data[filtered_data['Reference'].isin(reference_color_map.keys())]

    # Create the map with the filtered data
    fig2 = px.scatter_mapbox(
        filtered_data,
        lat='Lat',
        lon='Long',
        hover_name='Reference',
        hover_data={
            'Reference': False,
            'Type': True,
            'Depth_in_core': True,
            'Water_depth': True,
            'TOC': True,
            'L/D/U': True,
            'S': True,
            'N': True
        },
        color='Reference',
        color_discrete_map=reference_color_map,  # Highlight the selected reference in orange
        zoom=7,
        height=600
    )
    
    fig2.update_traces(marker=dict(opacity=0.7, size=10))  # Set marker transparency and size

    fig2.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(
            center=dict(lat=40.8, lon=28.5),
            zoom=7
        ),
        title=dict(
            text=f"<b>{selected_reference} Station Locations</b>",
            font=dict(family="Lora, Roboto, sans-serif", size=20),
            x=0.5,
            xanchor="center"
        ),
        margin={"r":0, "t":50, "l":0, "b":0}
    )

    # Display the map in Streamlit
    st.plotly_chart(fig2)

    # Prepare columns without null or zero values
    non_null_columns = [
        col for col in filtered_data.columns if filtered_data[col].notna().any() and (filtered_data[col] != 0).any()
]

    # Exclude unwanted columns explicitly
    unwanted_columns = {"Code","Reference", "Type", "Lat", "Long", "L/D/U", "Size_fraction", "S", "N", "Unnamed: 450"}
    filtered_columns = [col for col in non_null_columns if col not in unwanted_columns]


    final_data=filtered_data[filtered_columns]

    # Display the filtered table beneath the map
        
    st.markdown(f"### Filtered Data for {selected_reference}")
    st.markdown(
    """
    <p style="font-size:10px; font-style:italic; color:gray;">
    Use the interactive button on the right corner to download the table as a csv file. See supplementary material in References Section for full names of taxa.
    </p>
    """,
    unsafe_allow_html=True)

    st.dataframe(
    final_data.style
    .set_properties(**{
        'font-size': '7px',
        'width': '60px',
        'text-align': 'left'
    })
    .set_table_styles([
        {
            'selector': 'th',
            'props': [
                ('writing-mode', 'vertical-lr'),
                ('text-orientation', 'mixed'),
                ('transform', 'rotate(45deg)'),
                ('height', '100px')
            ]
        }
    ])
    .format(precision=2)  # Keep values formatted to 3 decimal places
)
#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")



