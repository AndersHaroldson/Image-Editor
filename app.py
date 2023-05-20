import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

def main():
    # Title
    st.markdown("<h1 style='text-align: center;'> 📸 Image Editor 📸 </h1>", unsafe_allow_html=True)

    # Getting rid of presets
    hideSt = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hideSt, unsafe_allow_html=True)

    # Get an image file
    imgFile = st.file_uploader("Upload an image to process", type=['jpg', 'png', 'jpeg'], accept_multiple_files=False)
    
    # Open image file
    if imgFile:
        st.sidebar.title("Editing Panel")
        img = Image.open(imgFile)
    else:
        return None

    # Brightness Adjustment
    brightnessSetting = st.sidebar.slider('Brightness', 0, 100, 50, step=1)
    newImage = ImageEnhance.Brightness(img).enhance(brightnessSetting/50)
    # Contrast Adjustment
    contrastSetting = st.sidebar.slider('Contrast', 0, 100, 50, step=1)
    newImage = ImageEnhance.Contrast(newImage).enhance(contrastSetting/50)
    # Color Adjustment
    colorSetting = st.sidebar.slider('Color', 0, 100, 50, step=1)
    newImage = ImageEnhance.Color(newImage).enhance(colorSetting/50)
    # Sharpness Adjustment
    sharpnessSetting = st.sidebar.slider('Sharpness', 0, 100, 50, step=1)
    newImage = ImageEnhance.Sharpness(newImage).enhance(sharpnessSetting/50)
    # Blur Adjustment
    blurSetting = st.sidebar.slider('Blur', 0, 100, 0, step=1)
    newImage = newImage.filter(ImageFilter.BoxBlur(blurSetting/10))

    # Output new image
    st.text("Edited Image")
    st.image(newImage)
    # Expander to see original image
    with st.expander("See original"):
        st.text("Original Image")
        st.image(img)

    # Preparing edited image for download
    buffer = BytesIO()
    newImage.save(buffer, format="PNG")
    byte_im = buffer.getvalue()

    # Download button
    btn = st.download_button(
        label="Download New Image",
        data=byte_im,
        file_name="editedImage.png",
        mime="image/png",
        )

if __name__ == '__main__':
    main()
