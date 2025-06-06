import streamlit as st
from textblob import TextBlob

# Styling the page with Streamlit's markdown and HTML injection for modern UI
st.set_page_config(
    page_title="Simple SpellChecker",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for the design based on the given inspiration guidelines
st.markdown(
    """
    <style>
    /* General body */
    .main {
        background-color: #ffffff;
        color: #6b7280;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
            Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        padding-top: 4rem;
        padding-bottom: 4rem;
        max-width: 800px;
        margin: 0 auto;
    }
    /* Headings */
    h1 {
        color: #111827;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    h2 {
        font-weight: 600;
        font-size: 1.25rem;
        color: #6b7280;
        margin-top: 0;
        margin-bottom: 2.5rem;
    }
    /* Text areas styling */
    textarea {
      border-radius: 0.75rem;
      border: 1px solid #d1d5db;
      padding: 1rem;
      font-size: 1rem;
      color: #374151;
      resize: vertical;
      box-shadow: 0 1px 2px rgb(0 0 0 / 0.05);
      transition: border-color 0.2s ease;
      width: 100% !important;
      min-height: 160px;
      font-family: inherit;
    }
    textarea:focus {
      outline: none;
      border-color: #111827;
      box-shadow: 0 0 0 3px rgb(17 24 39 / 0.2);
    }

    /* Button styling */
    .stButton > button {
      background-color: #111827;
      color: white;
      font-weight: 600;
      font-size: 1rem;
      padding: 0.75rem 1.75rem;
      border-radius: 0.75rem;
      border: none;
      width: 100%;
      transition: background-color 0.3s ease, transform 0.2s ease;
      cursor: pointer;
      box-shadow: 0 4px 8px rgb(17 24 39 / 0.1);
    }
    .stButton > button:hover {
      background-color: #374151;
      transform: scale(1.02);
    }
    .stButton > button:focus {
      outline: 2px solid #2563eb;
      outline-offset: 2px;
    }

    /* Output container styling */
    .output-container {
      margin-top: 2rem;
      background-color: #f9fafb;
      border-radius: 0.75rem;
      padding: 1.25rem 1.5rem;
      box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
      font-size: 1rem;
      color: #374151;
      white-space: pre-wrap;
      min-height: 160px;
      font-family: inherit;
    }

    /* Warning messages */
    .stAlert {
      border-radius: 0.75rem;
      font-weight: 600;
      box-shadow: none;
      margin-top: 1rem;
      max-width: 800px;
      margin-left: auto;
      margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main container div to apply styling
st.markdown('<div class="main">', unsafe_allow_html=True)

# Title and subtitle
st.markdown("# 📝 Simple SpellChecker")
st.markdown("Periksa dan koreksi ejaan teks dengan cepat menggunakan **TextBlob**.")

# Text input area
input_text = st.text_area("Masukkan teks yang ingin diperiksa ejaannya:")

# When button clicked, validate input and show corrected text
if st.button("Periksa Ejaan"):
    if not input_text.strip():
        st.warning("⚠️ Silakan masukkan teks sebelum menekan tombol periksa.")
    else:
        corrected = str(TextBlob(input_text).correct())
        st.markdown('<div class="output-container">', unsafe_allow_html=True)
        st.write(corrected)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

