"""
File Upload with Streamlit

Ref:
https://blog.jcharistech.com/2021/01/21/how-to-save-uploaded-files-to-directory-in-streamlit-apps/
https://towardsdatascience.com/data-apps-with-pythons-streamlit-b14aaca7d083
https://github.com/Wirg/stqdm
https://discuss.streamlit.io/t/stqdm-a-tqdm-like-progress-bar-for-streamlit/10097
https://pythonwife.com/file-upload-download-with-streamlit/
"""
import os
import time
import streamlit as st #pip install streamlit
from stqdm import stqdm

st.title('File Uploader App')
st.write('A general purpose data exploration app')
file = st.file_uploader("Upload file", type=['xlsx'])
st.write(file)

if file is not None:
    with open(os.path.join(os.getcwd(),file.name),"wb") as f:
        f.write(file.getbuffer())
    
    for _ in stqdm(range(50)):
        for _ in stqdm(range(15)):
            time.sleep(0.5)