import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import numpy as np


# Ensure the correct path to the Tesseract executable (Windows users)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to perform OCR on an uploaded image
def ocr_image_with_tesseract(image):
    try:
        # Perform OCR using pytesseract with both English and Hindi languages
        custom_config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(image, lang='eng+hin', config=custom_config)

        if not extracted_text.strip():
            extracted_text = "No text will be extracted. Please try a different image."

        return extracted_text
    except Exception as e:
        return f"Error during OCR processing: {str(e)}"

# Function to highlight searched keywords
def highlight_text(extracted_text, keyword):
    if not keyword:
        return extracted_text

    highlighted_text = extracted_text.replace(keyword, f'**{keyword}**')
    return highlighted_text


# Streamlit App Layout
def main():
    st.title("OCR Web App (Supports Hindi and English Text)")
    st.write("Upload an image containing Hindi and/or English text, and see the extracted text.")

    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:

        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("Extracting text...")
        extracted_text = ocr_image_with_tesseract(image)

        st.subheader("Extracted Text:")
        st.text_area("Extracted Text", value=extracted_text, height=200)

        # Add a search feature
        st.subheader("Search for a Keyword:")
        keyword = st.text_input("Enter a keyword to search")

        if keyword:
            # Highlight and display the search results
            st.write("Search Results:")
            highlighted_text = highlight_text(extracted_text, keyword)
            st.markdown(highlighted_text)


    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align:center; font-size:20px; margin-top:50px;">
             <span style="font-size:22px; font-weight:bold; color:#FF5733;">© Made by Pratham Bajpai</span>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
