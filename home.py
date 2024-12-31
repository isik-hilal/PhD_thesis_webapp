import streamlit as st
from PIL import Image
from analysis import add_footer

def show_home():
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 24px;">
        Benthic Foraminifera of the Sea of Marmara: Distribution, Ecology and Significance as Biotic Indices
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        Gamze TANIK
        </p>
        """, unsafe_allow_html=True
    )

    # Abstract
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 20px;">Abstract</h2>
        <div style="text-align: justify; font-size: 14px;">
        Sea of Marmara (SoM), connecting the Black Sea and Mediterranean, has a stratified water
column with a strong pycnocline at ~25-40 m depth with limited mixing. As a result, the top
layer is oxygenated, but in depth the dissolved oxygen values drop drastically and produce
suboxic or anoxic conditions in bottom waters. This layered structure of the water column
directly translates into the benthic foraminifera (BF) communities with <em>Ammonia</em> and <em>Elphidium</em>
dominated shallow assemblages (&lt;40 m), <em>Cassidulina laevigata</em> dominated deeper assemblages
(40-150 m) and <em>Bolivina spathulata</em>, <em>Bolivina vadescens</em> and <em>Paracassidulina minuta</em> dominated
deepest assemblages. This study quantitatively documented the BF assemblages from 18 stations
(short sediment cores) from the SoM, presenting a comprehensive systematic taxonomy and high
quality illustrations of deep sea benthic foraminifera. With integration of the previously
published quantitative BF data, this study generated the geographic distributions of BF
assemblages and the relationship of BF communities with environmental variables. The changes
in BF assemblages in the vertical dimension were investigated by the study of 15 sediment cores.
Depositional history of the core from the Karamürsel Basin was documented in this way, and the establishment of sulfidic bottom water in the basin was linked to the 1999 earthquake with the
abundance of <em>Virgulinella fragilis</em>. The quantitative data set was applied to assess the utility and
applicability of four quantitative foraminiferal biotic indices: %P*, morphotype classification,
BFOI and Foram-AMBI. In conclusion, this study forms a basis for future monitoring and
taxonomic studies by documenting the present configuration in the SoM.

<br><br>
<strong>Keywords:</strong> Benthic foraminifera, Sea of Marmara, quantitative analysis, biotic indices, Foram-
AMBI.
        </div>""", unsafe_allow_html=True
    )

     # About the project
    st.markdown(
        """ 
        <br><br>
        <h2 style="text-align: center; font-size: 20px;">Conclusions</h2>
        <div style="text-align: justify; font-size: 14px;">
        Benthic foraminifera (BF) is one of the major elements of meiobenthos, and due to their high
abundance, diversity and small size, both in recent sediments and as fossils in older strata, are
used for time keeping and as environmental proxies. To assign predictive power to BF
assemblages or individual BF taxa, their study in various different settings is necessary. The Sea
of Marmara (SoM) provides a special setting for such studies of BF due to its permanently
stratified water column and suboxic deep basins, limited circulation, high antropogenic stress
resulting from dense industrial and residential settlements on its coasts, and its position and
importance as a link between the Black Sea and the Mediterranean.

For this purpose, BF of the SoM were studied from 18 short sediment cores from 15 stations (82
samples in total), mainly from the eastern side of the SoM. Stations span a wide geographic area
and water depths, including the Izmit Bay, shelf around Prince Islands, Çınarcık Basin, Imralı
Basin, Southern shelf, Southern slope and Central Basin, from 53.5 m to 1214 m water depth.

172 BF taxa were identified, and a comprehensive systematic taxonomy was constructed. Taxa
was quantified from the samples, and relative abundances of taxa were used for their relationship
with environmental variables such as water depth, dissolved oxygen, and measured
concentrations of nitrite, nitrate, ammonium, phosphate in the bottom, interface and pore waters
of the stations. Total absolute abundances of benthic and planktonic foraminifera (PF) and
distributions of taxa were determined and differences and similarities of stations from the 18
core-top samples were documented.

Along selected 15 sediment cores the total absolute abundances of benthic and planktonic
foraminifera (PF), relative abundances of taxa, the ratio of PF (P%) and sand content were
analyized to distinguish changes in the vertical dimension. Most of the studied cores showed no
significant changes, however in several of them shifts in foraminiferal assemblages were detected. The shifts in the abundances of <em>Bulimina inflata</em>, <em>Melonis pompilioides</em> and
<em>Sigmoilopsis</em> sp.1 were interpreted in terms of change in quality and quantity of food reaching
the sea floor especially in the deep basins (Central and Çınarcık basins). The shift in the relative
abundance of <em>V. fragilis</em>, along with change in P% and total absolute abundance of benthic
foraminifera, evaluated with the radiocarbon dating of the core, was linked with the
establishment of sulfidic conditions in the Karamürsel Basin, after the 1999 earthquake.

The produced benthic foraminifera dataset was compared to the previous quantitative works, and
the data from 10 studies were incorporated to effectively and comprehensively evaluate the
distribution of taxa in the SoM. Cluster analysis was utilized to asses the differences and
similarities of stations, showing that different assemblages prevail in different bathymetric zones
and near stream mouths. Adjacent to stream mouths the assemblage is the poorest in terms of
diversity; the shallowest shelf is dominated by <em>Ammonia</em> and <em>Elphidium genera</em>, below, about 40
m to 150 m the assemblage is dominated by <em>Cassidulina laevigata</em>, and below that the
dominance of <em>Bolivina spathulata</em>, <em>Bolivina vadescens</em> and <em>Paracassidulina minuta</em> was
distinguished. Combining of the data from the literature showed the need of establishment of a
solid taxonomic framework for the benthic foraminifera of the SoM and encouragement of its
wide usage.

The data from the studied core-top samples were used in application of four quantitative
foraminiferal biotic indices: %P* (as depth proxy), morphotype classification (as total organic
carbon proxy), BFOI and (as bottom water oxygen proxy) and Foram-AMBI (as ecological
quality status proxy), and assessment of their utility. Analysis of these indices show wide
separation between the calculated and measured values for the former three, showing either the
inadequacy of the resolution the indices provide, or alteration of the assemblages analyzed due to
bottom processes such as dissolution, winnowing or resedimentation. Calculated Foram-AMBI
values show all stations to be slightly polluted with an unbalanced assemblage. Foram-AMBI is
very promising in terms of monitoring applications; however, further research is necessary until
it can be utilized.

In conclusion, this study presents a comprehensive systematic taxonomy with numerous high
quality illustrations of mainly deep sea benthic foraminiferal taxa which can be used as a
reference material in future studies, forms a basis for future monitoring studies by supplying quantitative foraminiferal data and calculated biotic indices from various settings in the SoM
showing the present configuration.</div> """, unsafe_allow_html=True
    )

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    # About Gamze Tanık
    
    st.markdown(
        """
        <h2 style=" font-size: 20px;">About Gamze Tanık</h2>
        <div style="text-align: justify; font-size: 14px;">
        <strong>Gamze Tanık</strong> is a geological engineer and paleontologist with a specialization in foraminifera. Her primary focus is on understanding changes in assemblages driven by climatic or depositional shifts. She has significant experience working with Paleocene-Eocene planktonic foraminifera and pteropoda. Currently, her research examines recent benthic foraminifera in the Sea of Marmara, particularly their response to anthropogenic impacts on assemblage composition.
        </div>
        """, unsafe_allow_html=True
    )

    #empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Contact Information with smaller text
    st.markdown(
        """
        <h3 style=" font-size: 18px;">Contact Information</h3>
        """, unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 5])  # Images column (left) is smaller, text column (right) is larger

    # In the first column (left), display images
    with col1:
        gamze_image = Image.open("images/gamze_tanik.jpg")  # Ensure the image is in the correct folder
        st.image(gamze_image, width=100)  # Set width to 100 pixels for a small image
        
        metu_logo = Image.open("images/metu_logo.jpeg")  # Ensure the logo image is in the images folder
        st.image(metu_logo, width=100)  # Set width to 100 pixels for the logo

    # In the second column (right), display contact info
    with col2:
        st.markdown(
            """
            <div style="font-size: 14px;">
            <strong>Email</strong>: <a href="mailto:gtanik@metu.edu.tr">gtanik@metu.edu.tr</a>
            <br><br>
            <strong>Institution</strong>: Faculty Of Engineering, Department Of Geological Engineering  
            <br><br>
            <strong>WoS Research Areas</strong>: Geology, Paleontology  
            <br><br>
            <strong>Avesis Research Areas</strong>: General Geology, Paleontology (paleobotany, invertebrate, vertebrate), Sedimentology, Stratigraphy, Geology 
            </div>
            """, unsafe_allow_html=True
        )

    # Adding a section about past work
    st.markdown(
        """
        <h3 style="font-size: 18px;">Past Research</h3>
        <div style="text-align: justify; font-size: 14px;">
        In her Master's thesis, Gamze studied planktonic foraminifera from the Paleocene-Eocene Thermal Maximum 
        (57-54 million years ago), a period marked by rapid global warming. She later expanded her research to 
        include the study of pteropoda in the same geological interval. 
        </div>
        """, unsafe_allow_html=True
    )
    #empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
    add_footer()