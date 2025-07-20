import streamlit as st


st.set_page_config(page_title="About", layout="centered")
st.title("Welcome to PixelOutPDF🎴")
st.markdown("A application where you can remove specific images from PDFs easily.")
st.markdown("""
            
**PixelOutPDF** is a lightweight Streamlit app that allows users to remove specific images like watermarks, logos, stamps, or overlays from PDF documents. This is particularly useful when working with scanned or watermarked PDFs in regional languages such as Kannada.

    """)


st.subheader("📘 How to Use")
st.markdown("""
1. Click on **Start Using PixelOutPDF**.
2. Upload your PDF file (max 200MB).
3. Select the page and images you want to remove.
4. Click **Remove** and preview your cleaned file.
5. Download the final PDF.
""")


st.subheader("🧱 Built With")
st.markdown("""
- [Streamlit](https://streamlit.io/)
- [Python 3.8+](https://www.python.org/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
- [Pillow](https://python-pillow.org/)
""")


st.subheader("📬 Contact & Links")
st.markdown("""
- Email: [kushalkush1804@gmail.com](mailto:kushalkush1804@gmail.com)
- GitHub: [mekhush](https://github.com/mekhush)
- LinkedIn: [me-khush](https://www.linkedin.com/in/me-khush)
- Project Repo: [PixelOutPDF](https://github.com/mekhush/PixelOutPDF)
""")



col1, col2 = st.columns(2)

with col1:
    if st.button("✨ Start Using PixelOutPDF"):
        st.switch_page("multi_pages/main.py")

with col2:
    if st.button("❓ Can't see the image you want to remove?"):
        st.switch_page("multi_pages/restriction.py")



# if st.button("Start Using PixelOutPDF ✨"):
#     st.switch_page("multi_pages/main.py")

# if st.button("❓ Can't see the image you want to remove? Click here to know why"):
#     st.switch_page("multi_pages/restriction.py")
