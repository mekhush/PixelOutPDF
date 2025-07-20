import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import tempfile
import os
import pathlib
from collections import defaultdict


st.set_page_config(page_title="PixelOutPDF", layout="centered")

# if st.button("❓ Can't see the image you want to remove? Click here to know why"):
#     st.switch_page("multi_pages/restriction.py")
# Step 1: Upload PDF
pdf_file = st.file_uploader("📤 Upload a PDF", type=["pdf"])

if pdf_file:
    # Save original filename
    original_filename = pathlib.Path(pdf_file.name).stem

    # Load PDF in memory
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    st.success(f"✅ Loaded PDF with {len(doc)} page(s)")

    image_info = []

    # Step 2: Extract all images and metadata
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            try:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                pil_img = Image.open(io.BytesIO(image_bytes))
                image_info.append({
                    "xref": xref,
                    "page": page_num + 1,
                    "image": pil_img,
                })
            except Exception as e:
                st.error(f"❌ Failed to extract image xref={xref} on page {page_num + 1}: {e}")

    # Step 3: Group images by page
    pagewise_images = defaultdict(list)
    for info in image_info:
        pagewise_images[info["page"]].append(info)

    # Step 4: Persist selected xrefs in session_state
    if "selected_xrefs" not in st.session_state:
        st.session_state.selected_xrefs = set()

    # Step 5: Page-wise viewing and selection
    st.subheader("📑 Page-wise Image Viewer")
    available_pages = sorted(pagewise_images.keys())

    if not available_pages:
        st.warning("No images found in the PDF.")
    else:
        selected_page = st.number_input("Go to page", min_value=min(available_pages), max_value=max(available_pages), step=1)

        # 📌 Summary Section
        if st.session_state.selected_xrefs:
            st.subheader("📌 Selected Images Summary")
            selected_images = [
                info for info in image_info if info["xref"] in st.session_state.selected_xrefs
            ]

            cols = st.columns([1, 2, 3])  # Page | xref | Image
            cols[0].markdown("**📄 Page**")
            cols[1].markdown("**🆔 xref**")
            cols[2].markdown("**🖼️ Image Preview**")

            for info in selected_images:
                cols = st.columns([1, 2, 3])
                cols[0].markdown(f"{info['page']}")
                cols[1].markdown(f"{info['xref']}")
                cols[2].image(info["image"], width=100)

        # Show selected page images with checkbox on right
        st.markdown(f"### 📄 Images on Page {selected_page}")
        for i, info in enumerate(pagewise_images[selected_page]):
            col1, col2 = st.columns([4, 1])  # image on left, checkbox on right
            key = f"pg{selected_page}_img_{i}_xref_{info['xref']}"
            is_checked = info['xref'] in st.session_state.selected_xrefs

            with col1:
                st.image(info["image"], use_container_width=True)

            with col2:
                checked = st.checkbox(f"xref={info['xref']}", key=key, value=is_checked)
                if checked:
                    st.session_state.selected_xrefs.add(info["xref"])
                else:
                    st.session_state.selected_xrefs.discard(info["xref"])

    # Optional: Clear all selections
    if st.button("🔄 Clear All Selections"):
        st.session_state.selected_xrefs.clear()
        st.success("Selections cleared!")

    # Step 6: Remove selected xrefs and export
    if st.session_state.selected_xrefs and st.button("🧹 Remove Selected Images"):
        fd, output_path = tempfile.mkstemp(suffix=".pdf")
        os.close(fd)

        new_doc = fitz.open(stream=pdf_file.getvalue(), filetype="pdf")  # reload original doc

        for page_num, page in enumerate(new_doc, start=1):
            for img in page.get_images(full=True):
                xref = img[0]
                if xref in st.session_state.selected_xrefs:
                    try:
                        page.delete_image(xref)
                        st.info(f"✅ Removed xref={xref} from page {page_num}")
                    except Exception as e:
                        st.error(f"❌ Error removing xref={xref} from page {page_num}: {e}")

        new_doc.save(output_path)
        new_doc.close()
        st.success("🎉 PDF cleaned successfully!")

        # Step 7: Download button
        cleaned_filename = f"{original_filename}_img_removed.pdf"
        with open(output_path, "rb") as f:
            st.download_button("⬇️ Download Cleaned PDF", f, file_name=cleaned_filename)

        # Step 8: Full-page Preview (Jupyter-like cells)
        st.subheader("📖 Cleaned PDF Preview (All Pages)")
        with fitz.open(output_path) as preview_doc:
            for page in preview_doc:
                with st.container():  # Jupyter-style cell
                    st.markdown(f"#### 📄 Page {page.number + 1}")
                    pix = page.get_pixmap()
                    preview_img = Image.open(io.BytesIO(pix.tobytes("png")))
                    st.image(preview_img, use_container_width=True)

        os.remove(output_path)
