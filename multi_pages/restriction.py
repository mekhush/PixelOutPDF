import streamlit as st

st.set_page_config(page_title="Restriction", layout="centered")
st.markdown("""
    ## 🔓Remove PDF Restrictions

    Most PDFs and scanned documents often have **editing restrictions** that prevent proper image extraction.

    These restrictions can cause:
    - ❌ Images not appearing in the viewer
    - ❌ Selected images not being removed
    - ❌ No error, but nothing changes

    ### ✅ How to fix it:
    Use this **free online tool** to remove restrictions:

    🔗 [online2pdf.com](https://online2pdf.com/remove-pdf-restrictions)
            
    🔗 [ilovepdf.com](https://www.ilovepdf.com/unlock_pdf)

    **Steps:**
    1. Upload your restricted PDF.
    2. Wait for processing.
    3. Download the unrestricted version.
    4. Re-upload the cleaned file in this app.

    This will ensure all images can be extracted and removed successfully.""")