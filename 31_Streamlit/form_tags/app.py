# https://github.com/gagan3012/streamlit-tags/blob/master/examples/app.py

import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

st.write("# Code for streamlit tags")

st.code(body='''keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags = 4,
    key='1')''',
        language="python")

maxtags = st.slider('Number of tags allowed?', 1, 10, 3, key='jfnkerrnfvikwqejn')

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags,
    key="aljnf")

st.write("### Results:")
st.write(type(keywords))

st.sidebar.write("# Code for streamlit tags sidebar")

st.sidebar.code(body='''keyword = st_tags_sidebar(
label='# Enter Keywords:',
text='Press enter to add more',
value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 
'eight', 'nine', 'three', 
'eleven', 'ten', 'four'],
maxtags = 4)''',
                language="python")

maxtags_sidebar = st.sidebar.slider('Number of tags allowed?', 1, 10, 3, key='ehikwegrjifbwreuk')


keyword = st_tags_sidebar(label='# Enter Keywords:',
                          text='Press enter to add more',
                          value=['Zero', 'One', 'Two'],
                          suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
                          maxtags=maxtags_sidebar,
                          key="afrfae")

st.sidebar.write("### Results:")
st.sidebar.write((keyword))


# Forms can be declared using the 'with' syntax
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')

    # st.form_submit_button returns True upon form submit
    if submit_button:
        st.write(f'hello {text_input}')