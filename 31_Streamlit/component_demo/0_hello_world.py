import streamlit as st
import pandas as pd

st.title('Hello World - This is a title :tropical_fish:')

st.header(':snake: This is a header')

st.subheader(':hatched_chick: This is a subheader')

st.caption('This is a string that explains something above.')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

code = '''
select 
    abc, def, efg 
from zzz 
where 
    abc='123'
'''
st.code(code, language='sql')

st.text('This is some text.')

st.write("Hello **World**!")

st.markdown("""---""")

st.subheader(':hatched_chick: 讀取 DataFrame')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.write(df)
st.write(df.style.highlight_max(axis=0))

st.markdown("""---""")

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.markdown("""---""")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("""---""")

if st.button('請按按鈕'):
    st.write('已按按鈕')
else:
    st.write('尚未點擊')

st.markdown("""---""")

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

st.markdown("""---""")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.markdown("""---""")

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.markdown("""---""")

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

st.markdown("""---""")

import os

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    
    with open(os.path.join("", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())


