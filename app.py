import streamlit as st
import qrcode
from PIL import Image
import io


st.set_page_config(page_title="Branded QR Generator", page_icon="🎨")

st.title("QR Asset Generator")
st.markdown(f"**Developed by Rukshan Weerasekara** | Creative Technologist")
st.markdown("---")
st.markdown("Create high-quality QR codes that match your brand identity.")


st.sidebar.header("Asset Details")
url = st.sidebar.text_input("Target URL", value="https://www.youtube.com")

st.sidebar.header(" Brand Identity")
fill_color = st.sidebar.color_picker("QR Color", value="#FFFFFF")
back_color = st.sidebar.color_picker("Background Color", value="#03687E")

st.sidebar.header("Visual Settings")
box_size = st.sidebar.slider("Box Size", 5, 50, 23)
border = st.sidebar.slider("Border Size", 1, 10, 6)


if st.button("Generate Branded QR"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
   
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

  
    st.image(byte_im, caption=f"Generated for: {url}", use_column_width=True)
    
 
    st.download_button(
        label=" Download QR ",
        data=byte_im,
        file_name="branded_qr.png",
        mime="image/png"
    )

