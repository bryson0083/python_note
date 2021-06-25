"""



Ref:
1. How to Save Uploaded Files to Directory in Streamlit Apps
https://blog.jcharistech.com/2021/01/21/how-to-save-uploaded-files-to-directory-in-streamlit-apps/

2. 


"""


import os
import shutil
import streamlit as st
import streamlit.components.v1 as stc
from PyPDF2 import PdfFileReader
# import pdfplumber


def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()

    return all_page_text


def main():
    st.title("File Upload Tutorial")

    menu = ["Home"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        docx_file = st.file_uploader(
            "Upload File", type=['txt', 'docx', 'pdf'])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"Filename": docx_file.name,
                                "FileType": docx_file.type, "FileSize": docx_file.size}
                st.write(file_details)
                # Check File Type
                if docx_file.type == "application/pdf":
                    st.write("filename: ", docx_file.name)
                    st.write(docx_file)
                    with open(os.path.join("", docx_file.name), "wb") as f:
                        f.write(docx_file.getbuffer())
                    # print(os.path.dirname(os.path.realpath(docx_file)))
                    try:
                        shutil.move(docx_file.name, "O:\P32\@@@@報表暫存區@@@@")
                        st.write("搬移檔案完成")
                    except Exception as e:
                        st.write(e)
                    # raw_text = read_pdf(docx_file)
                    # st.write(raw_text)

                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         page = pdf.pages[0]
                    #         st.write(page.extract_text())
                    # except:
                    #     st.write("None")

    else:
        st.subheader("About")
        st.info("Built with Streamlit")
        st.info("Jesus Saves @JCharisTech")
        st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
    main()
