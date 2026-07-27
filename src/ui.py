import streamlit as st


def configurar_pagina():

    st.set_page_config(
        page_title="Agente de Consultas IA",
        page_icon="",
        layout="wide"
    )


def mostrar_sidebar():

    with st.sidebar:

        st.title(" Proyecto challenge Alura")

        st.markdown("---")

        st.write("### 📄 Documento")

        archivo = st.file_uploader(
            "Seleccione un documento sólo archivos PDF",
            type=["pdf"],
            help="Suba un documento para que el asistente pueda responder preguntas sobre su contenido."
        )

        st.markdown("---")

        limpiar = st.button("🗑 Limpiar historial")

        return archivo, limpiar