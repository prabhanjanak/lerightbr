import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set page config
st.set_page_config(page_title="Right Brothers - AI For Legal Documentation and Assistance", layout="wide")

# Function to load an image from a URL
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")
        return None
    except UnidentifiedImageError as e:
        st.error(f"Error identifying image: {e}")
        return None

# Example image URLs
main_image_url = "https://st2.depositphotos.com/3837271/9109/i/450/depositphotos_91090624-stock-photo-wooden-blocks-with-the-text.jpg"
main_image_url1="https://img.freepik.com/free-photo/still-life-with-scales-justice_23-2149776024.jpg"
profile_image_url = "https://t3.ftcdn.net/jpg/05/75/22/58/360_F_575225818_PQ2ZPHFw51yCcmieutB5bT843nPAPzo3.jpg"
profile_image_url1="https://www.shutterstock.com/image-illustration/illustration-operator-600nw-110348867.jpg"
profile_image_url2="https://img.freepik.com/premium-photo/3d-call-center-operator-working-with-laptop-thumb-up_168450-70.jpg"
profile_image_url3="https://img.freepik.com/premium-photo/3d-illustration-young-girl-with-glasses-white-coat_856795-21399.jpg"
profile_image_url4="https://img.freepik.com/premium-photo/young-caucasian-tv-presenter-woman-isolated-white-background-showing-lifting_540381-3409.jpg"
# Load images
main_image = load_image(main_image_url)
main_image1=load_image(main_image_url1)
profile_image = load_image(profile_image_url)
profile_image1 = load_image(profile_image_url1)
profile_image2 = load_image(profile_image_url2)
profile_image3 = load_image(profile_image_url3)
profile_image4 = load_image(profile_image_url4)

st.write("---")
st.header("About Us!")
st.write("##")

# About Us Section
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Revolutionizing Legal Documentation. Simplifying legal complexities.")
        st.write("""
            At RightBrothers, our journey began with the vision of simplifying legal documentation for individuals and businesses alike. 
            We're dedicated to transforming the way legal documents are created, making the process intuitive, efficient, and accessible to all.
            Whether you're drafting contracts, agreements, or other legal documents, LegaEase is here to streamline the process and empower you with confidence.
        """)
    with col2:
        if main_image1:
            st.image(main_image1, use_column_width=True)

st.write("")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        if main_image:
            st.image(main_image, caption="Our Team", use_column_width=True)
    with col2:
        st.header("Empowering Legal Solutions at Your Fingertips. Bringing clarity to legal complexities.")
        st.write("""
            Discover a new era of legal documentation with LegaEase. Our user-friendly platform harnesses the power of AI to generate accurate and easy-to-understand legal documents tailored to your needs.
            Say goodbye to cumbersome processes and hello to streamlined solutions with LegaEase.
        """)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Navigating the Legal Landscape Made Simple. Your trusted ally in legal matters.")
        st.write("""
            LegaEase is your partner in simplifying the complexities of the legal world. With our innovative approach,
            we're revolutionizing the way individuals and businesses handle legal documentation. 
            Let us guide you through the legal maze, providing clarity and confidence every step of the way.
        """)
    with col2:
        if profile_image:
            st.image(profile_image, caption="Our Team", use_column_width=True)

st.write("-------------------------------------------------------")
with st.container():
    st.header("Meet Our team!")
    with st.container():
        left, mid1, mid2, right = st.columns(4)
        
        with left:
            if profile_image:
                st.image(profile_image1, use_column_width=True)
            st.write("Name: Eeshan V C")
            st.write("Usn: 4PM21AI013")
            st.write("Email: eeshanvc@gmail.com")
        with mid1:
            if profile_image:
                st.image(profile_image2, use_column_width=True)
            st.write("Name: Harsha T R")
            st.write("Usn: 4PM21AI017")
            st.write("Email: htr1172@gmail.com")
        with mid2:
            if profile_image:
                st.image(profile_image3, use_column_width=True)
            st.write("Name: Prabhanjana K")
            st.write("Usn: 4PM21AI026")
            st.write("Email: prabh.bhat12@gmail.com")
        with right:
            if profile_image:
                st.image(profile_image4, use_column_width=True)
            st.write("Name: Prathibha P")
            st.write("Usn: 4PM21AI028")
            st.write("Email: prathibhapsagar@gmail.com")

# Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #000000;
            padding: 5px 0;
            text-align: center;
            font-size: 12px;
            color: #f0f0f0;
        }
    </style>
    <div class="footer">
        <p>© 2023-2024 LegaEase, Inc. · <a href="#">Privacy</a> · <a href="#">Terms</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
