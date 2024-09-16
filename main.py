import streamlit as st
import fitz  # PyMuPDF

def pdf_to_text(pdf_file):
    text = ""
    # Read the PDF file as a byte stream
    pdf_bytes = pdf_file.read()
    
    with fitz.open(stream=pdf_bytes, filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()
    return text

st.title("PDF to Text Converter")
st.write("Upload a PDF file to extract text.")

pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

if pdf_file is not None:
    with st.spinner("Processing..."):
        text = pdf_to_text(pdf_file)
        st.text_area("Extracted Text", text, height=600)
