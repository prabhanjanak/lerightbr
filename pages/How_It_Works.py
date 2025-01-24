import streamlit as st
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Page title
st.title("How LegaEase Works")

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# Define CSS styles
style = """
<style>

.card {
    width: 300px; /* Set the width of the card */
    height: 200px;
    border: 1px solid black;
    border-radius: .25rem;
    background-color: #f8f9fa;
    transition: box-shadow .3s ease;
}

.card:hover {
    box-shadow: 0 0 11px rgba(33,33,33,.2);
}

.card-body {
    flex: 1 1 auto;
    padding: 1.25rem;
}

.card-title {
    margin-bottom: .75rem;
    font-size: 1.25rem;
    font-weight: 500;
    line-height: 1.2;
}

.card-text {
    margin-top: .5rem;
    margin-bottom: 1.25rem;
}
</style>
"""

# Add CSS styles
st.markdown(style, unsafe_allow_html=True)

# Steps Section
st.header("Steps Section")

col1, col2, col3 = st.columns(3)

# Step 1: Sign Up
with col1:
    st.markdown("""
    <div class="card h-100">
        <div class="card-body">
            <div class="mb-3"><i class="fas fa-user-plus fa-3x"></i></div>
            <h5 class="card-title">Step 1: Sign Up</h5>
            <p class="card-text">Create your free account in minutes and gain access to all features.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Step 2: Upload Your Documents
with col2:
    st.markdown("""
    <div class="card h-100">
        <div class="card-body">
            <div class="mb-3"><i class="fas fa-upload fa-3x"></i></div>
            <h5 class="card-title">Step 2: Upload Your Documents</h5>
            <p class="card-text">Easily upload your legal documents securely.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <div class="mb-3"><i class="fas fa-edit fa-3x"></i></div>
                        <h5 class="card-title">Step 3: Customize Your Documents</h5>
                        <p class="card-text">Use our tools to tailor documents to your specific needs.</p>
                    </div>
                </div>
            </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='margin-top: 20px'></p>", unsafe_allow_html=True)

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    st.markdown("""
    <div class="col-md-4 mb-4">
        <div class="card h-100">
            <div class="card-body">
                <div class="mb-3"><i class="fas fa-robot fa-3x"></i></div>
                <h5 class="card-title">Step 4: Consult with Our AI Legal Assistant</h5>
                <p class="card-text">Get instant legal advice and answers to your questions.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Step 5: Get Professional Legal Help
with row2_col2:
    st.markdown("""
    <div class="col-md-4 mb-4">
        <div class="card h-100">
            <div class="card-body">
                <div class="mb-3"><i class="fas fa-gavel fa-3x"></i></div>
                <h5 class="card-title">Step 5: Get Professional Legal Help</h5>
                <p class="card-text">Schedule consultations with our top-notch lawyers for further assistance.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Step 6: Go For Premium Version
with row2_col3:
    st.markdown("""
    <div class="col-md-4 mb-4">
        <div class="card h-100">
            <div class="card-body">
                <div class="mb-3"><i class="fa-solid fa-dollar-sign"></i></div>
                <h5 class="card-title">Step 6: Go For Premium Version</h5>
                <p class="card-text">For More Features and Special consultancy go for premium version!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Testimonials Section
# Testimonials Section
st.write("<h2 style='text-align: center; margin-top: 50px;'>Testimonials</h2>", unsafe_allow_html=True)

# Testimonial 1
st.write("""
<div style='text-align: center; margin-bottom: 30px;'>
    <img src='https://via.placeholder.com/150' alt='Testimonial Image' style='border-radius: 50%; width: 150px; height: 150px;'>
    <p>"Streamlit made it incredibly easy for us to build interactive web apps for our clients. The simplicity and flexibility of the framework are unmatched!"</p>
    <p><strong>John Doe</strong><br> CEO, ABC Company</p>
</div>
""", unsafe_allow_html=True)

# Testimonial 2
st.write("""
<div style='text-align: center; margin-bottom: 30px;'>
    <img src='https://via.placeholder.com/150' alt='Testimonial Image' style='border-radius: 50%; width: 150px; height: 150px;'>
    <p>"We've been using Streamlit for our data visualization needs, and it has exceeded our expectations. The intuitive interface and fast development cycle are perfect for our team!"</p>
    <p><strong>Jane Smith</strong><br> Data Scientist, XYZ Corp</p>
</div>
""", unsafe_allow_html=True)

# Testimonial 3
st.write("""
<div style='text-align: center; margin-bottom: 30px;'>
    <img src='https://via.placeholder.com/150' alt='Testimonial Image' style='border-radius: 50%; width: 150px; height: 150px;'>
    <p>"Thanks to Streamlit, we were able to quickly prototype and deploy a machine learning model for our project. The ease of use and customization options are exceptional!"</p>
    <p><strong>Michael Johnson</strong><br> AI Engineer, Acme Inc</p>
</div>
""", unsafe_allow_html=True)

def faq_section():
    st.title("FAQs")
    with st.expander("What is LegaEase?"):
        st.write("LegaEase is an online platform that simplifies legal processes by offering secure document storage, "
                 "AI-powered legal assistance, and access to expert lawyers.")

    with st.expander("How do I upload documents?"):
        st.write("You can upload documents by signing into your account and selecting the 'Upload Document' option. "
                 "Follow the prompts to securely upload your files.")

    with st.expander("How does the AI Legal Assistant work?"):
        st.write("Our AI Legal Assistant uses advanced algorithms to provide you with instant answers to common legal "
                 "questions. Simply type in your query, and the AI will deliver accurate and helpful information.")

    with st.expander("Are my documents secure?"):
        st.write("Yes, your documents are stored securely using encryption and other advanced security measures. Only "
                 "you and authorized parties can access your documents.")

    with st.expander("How can I contact a lawyer?"):
        st.write("You can contact a lawyer through our platform by selecting a lawyer from our directory and "
                 "scheduling a consultation. You can communicate via messaging, phone, or video call.")

    with st.expander("What types of legal documents can I customize?"):
        st.write("LegaEase allows you to customize a wide range of legal documents, including contracts, wills, "
                 "leases, and more. Simply select a template and follow the prompts to tailor it to your needs.")

    with st.expander("Is there a cost to use LegaEase?"):
        st.write("LegaEase offers various subscription plans, including a free tier with basic features. Premium "
                 "plans with additional benefits are available for a monthly or annual fee.")

    with st.expander("Can I access LegaEase on my mobile device?"):
        st.write("Yes, LegaEase is fully responsive and can be accessed on any mobile device or tablet, allowing you "
                 "to manage your legal needs on the go.")

def main():
    st.markdown("<h1 style='text-align: center;'>LegaEase FAQs</h1>", unsafe_allow_html=True)
    faq_section()

if __name__ == "__main__":
    main()

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
        <p>© 2024-25 RightBrothers - AI For Legal Documentation and Assistance· <a href="#">Privacy</a> · <a href="#">Terms</a></p>
    </div>
    """,
    unsafe_allow_html=True
)