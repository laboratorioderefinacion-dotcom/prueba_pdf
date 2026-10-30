#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import tempfile
import subprocess
import os

st.title("Prueba DOCX → PDF")

docx_file = st.file_uploader(
    "Subir DOCX",
    type=["docx"]
)

if docx_file:

    if st.button("Convertir"):

        with tempfile.TemporaryDirectory() as tmpdir:

            docx_path = os.path.join(
                tmpdir,
                docx_file.name
            )

            with open(docx_path, "wb") as f:
                f.write(docx_file.getbuffer())

            try:

                subprocess.run(
                    [
                        "soffice",
                        "--headless",
                        "--convert-to",
                        "pdf",
                        docx_path,
                        "--outdir",
                        tmpdir
                    ],
                    check=True
                )

                pdf_path = os.path.join(
                    tmpdir,
                    docx_file.name.replace(
                        ".docx",
                        ".pdf"
                    )
                )

                with open(pdf_path, "rb") as pdf:

                    st.download_button(
                        "Descargar PDF",
                        pdf,
                        file_name=os.path.basename(
                            pdf_path
                        ),
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(str(e))

