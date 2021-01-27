# https://officeguide.cc/python-streamlit-build-web-data-analysis-app-tutorial-examples/
import streamlit as st
import pandas as pd
import time
import datetime
from datetime import datetime, date, time


# 設定網頁標題
st.title('My App')

# 加入網頁文字內容
st.write("My first app")

st.header("清分算日期")
st.date_input('start date')
st.date_input('end date')

# 加入 pandas 資料表格
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

multi_index = pd.MultiIndex.from_product([
    ['city_1', 'city_2'],
    ['store_1', 'store_2', 'store_3'],
])

df = pd.DataFrame(columns=['apples', 'oranges'], index=multi_index)
df.index.set_names(['city', 'store'], inplace=True)

# Now let's make some selectboxes for drilling up/down
levels = [
    st.selectbox('Level 1', ['All'] +
                 [i for i in df.index.get_level_values(0).unique()]),
    st.selectbox('Level 2', ['All'] +
                 [i for i in df.index.get_level_values(1).unique()])
]

# We need to use slice(None) if the user selects 'All'.
# The specified level with 'All' will take all values in that level.
for idx, level in enumerate(levels):
    if level == 'All':
        levels[idx] = slice(None)

# Make a cross section with the level values and pass in the index names.
st.dataframe(
    df.xs(
        (levels[0], levels[1]),
        level=['city', 'store']
    )
)
