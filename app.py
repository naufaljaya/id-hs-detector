import streamlit as st
from helper import predict
from lang import change_lang

# Default lang (indo)
if 'words' not in st.session_state:
    st.session_state['words'] = {
        "title": "Pendeteksi Ujaran Kebencian",
        "desc": "Dalam Bahasa Indonesia",
        "text_input_placeholder": "Masukkan kalimat disini",
        "option": "Pilih bahasa antarmuka",
        "button": "Deteksi",
        "error": ":warning: Ujaran kebencian terdeteksi! harap lakukan hal berikut:",
        "write": "**1. Jangan Terlibat dalam Perdebatan atau Provokasi** <br> **2. Laporkan Ujaran Kebencian**",
        "success": ":heavy_check_mark: Tidak terdeteksi ujaran kebencian"
    }
option = st.selectbox(
    "",
    ('Indonesia', 'English', '한국'))

st.session_state['words'] = change_lang(option)

st.title(st.session_state['words']["title"])

st.write(st.session_state['words']["desc"])

detect = st.text_input(
    '', '', placeholder=st.session_state['words']["text_input_placeholder"])

if st.button(st.session_state['words']["button"], type="primary"):
    decision = predict(detect)
    if decision:
        st.error(st.session_state['words']["error"])
        st.write(st.session_state['words']["write"], unsafe_allow_html=True)

    else:
        st.success(st.session_state['words']["success"])
