<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


---
<!-- readme-top -->
## 📄 About The Project

**PixelOutPDF** is a lightweight Streamlit app that allows users to remove specific images like watermarks, logos, stamps, or overlays from PDF documents. This is particularly useful when working with scanned or watermarked PDFs in regional languages such as Kannada.

### 🧱 Built With

This project uses the following core libraries:

* [![Streamlit][streamlit-logo]][streamlit-web]

* [![Python][python-logo]][python-web]

<p align="right"><a href="#readme-top">⬆️</a></p>


### 🧠 Features

- 📄 **PDF Upload** — Upload PDF documents (up to 200MB)
- 📅 **Page-by-Page Image Extraction** — Navigate pages and view all images on each
- 🖼️ **Image Preview with Checkboxes** — Easily select unwanted images
- 🧹 **Remove Selected Images** — Clean out overlays without disturbing text
- 🔍 **Preview** the cleaned file after processing
- ⬇️ **Download** the cleaned PDF
<p align="right"><a href="#readme-top">⬆️</a></p>

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
<p align="right"><a href="#readme-top">⬆️</a></p>
### 📚 Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/PixelOutPDF.git
cd PixelOutPDF
```

2. Create a virtual environment:

```bash
python -m venv pdf
```

3. Activate the virtual environment:

```bash
# Windows
pdf\Scripts\activate

# macOS/Linux
source pdf/bin/activate
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
streamlit run app.py
```
<p align="right"><a href="#readme-top">⬆️</a></p>

---

## ⚡ Usage

### 📄 Upload PDF

### 📝 Select Page and Images

### 🧹 Remove Selected Images

### 📅 Download Cleaned PDF

<p align="right"><a href="#readme-top">⬆️</a></p>

---

## 🚩 Roadmap
- [x] Add drag-and-drop file upload support
- [ ] Integrate OCR to extract and display text alongside images
- [ ] Add image size filter (remove only small logos or stamps)
- [ ] Add navigation buttons (next/previous page for better UX)
- [ ] Support for image preview zoom
- [ ] Allow batch processing of multiple PDFs
- [ ] Add multilingual UI (Kannada, Hindi, etc.)
- [ ] Add password-protected PDF support
- [ ] Option to export only selected pages
- [ ] Improve UI/UX using custom CSS/themes
- [ ] Deploy on Streamlit Cloud or HuggingFace Spaces


<p align="right"><a href="#readme-top">⬆️</a></p>

---

## ♻️ Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<p align="right"><a href="#readme-top">⬆️</a></p>

---

## 📆 License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right"><a href="#readme-top">⬆️</a></p>

---

## 📢 Contact

**Kushal B**\
Email: [kushalkush1804@gmail.com](mailto\:kushalkush1804@gmail.com)\
GitHub: [@mekhush](https://github.com/mekhush)\
LinkedIn: [me-khush](https://www.linkedin.com/in/me-khush)\
Project Link: [https://github.com/mekhush/PixelOutPDF](https://github.com/your_username/PixelOutPDF)

<p align="right"><a href="#readme-top">⬆️</a></p>

---

## 📈 Acknowledgments

- [Streamlit][streamlit-web]
- [PyMuPDF][pymupdf-lib]
- [Pillow][pillow-lib]
- [Font Awesome][font-awe]
- [GitHub Emoji Cheat Sheet][gitHub-emoji-cheat-sheet]

<p align="right"><a href="#readme-top">⬆️</a></p>



[streamlit-logo]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-web]: https://streamlit.io/
[python-logo]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-web]: https://www.python.org/

[pymupdf-lib]: https://pymupdf.readthedocs.io/en/latest/
[pillow-lib]: https://python-pillow.org/
[font-awe]: https://fontawesome.com
[gitHub-emoji-cheat-sheet]: https://www.webpagefx.com/tools/emoji-cheat-sheet
