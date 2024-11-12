import qrcode
import streamlit as st
import io

URLS = {
    "IDS - Ingenieria en desarrollo de software": {
        "1": {
            "Matutino": {"A": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-IDS-TM-A-1024x791.jpg',
                         "B": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-IDS-TM-B-1024x791.jpg'},
            "Vespertino": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-IDS-TV-1024x791.jpg'
        },
        "3": {
            "Matutino": {"A": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-IDS-TM-A-1024x791.jpg',
                         "B": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-IDS-TM-B-1024x791.jpg'},
            "Vespertino": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-IDS-TV-1024x791.jpg'
        },
        "5": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/5-IDS-1-1024x791.jpg',
        "7": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/7-IDS-1024x791.jpg',
        "9": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/9-IDS-1024x791.jpg'
    },
    "ITC - Ingenieria en Tecnologia Computacional": {
        "1": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-ITC-1024x791.jpg',
        "3": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-ITC-1024x791.jpg',
        "5": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/5-ITC-1024x791.jpg',
        "7": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/7-ITC-1024x791.jpg',
        "9": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/9-ITC-1024x791.jpg'
    },
    "LATI & TSUATI - Licenciatura en Administracion de Tecnologias de la informacion": {
        "1": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-LATI-TM-1024x791.jpg',
        "3": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-LATI-TM-1024x791.jpg',
        "5": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/5-LATI-TM-1024x791.jpg',
        "7": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/7-LATI-TM-1024x791.jpg'
    },
    "LITI - Licenciatura en Tecnologia de la Informacion": {
        "1": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-LITI-1024x791.jpg',
        "3": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/3-LITI-1024x791.jpg',
        "5": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/5-LITI-1024x791.jpg'
    },
    "IC - Ingenieria en Ciberseguridad": {
        "1": 'https://www.uabcs.mx/dasc/wp-content/uploads/2024/08/1-IC-TM-1-1024x791.jpg'
    }
}

def generate_qr_code(url, fill_color, bg_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=bg_color)

st.title("Encuentra tu horario")

carrera = st.selectbox("Selecciona tu carrera", list(URLS.keys()))
semestre = st.selectbox("Selecciona tu semestre", list(URLS[carrera].keys()))

turno = None
grupo = None
url = URLS[carrera][semestre]

if isinstance(url, dict):
    turno = st.selectbox("Selecciona tu turno", list(url.keys()))
    url = url[turno]
    if isinstance(url, dict):
        grupo = st.selectbox("Selecciona tu grupo", list(url.keys()))
        url = url[grupo]

if st.button("Generate QR Code") and url:
    try:
        qr_img = generate_qr_code(url, "#000000", "#FFFFFF")
        img_buffer = io.BytesIO()
        qr_img.save(img_buffer, format="PNG")
        img_bytes = img_buffer.getvalue()
        st.image(img_bytes)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
