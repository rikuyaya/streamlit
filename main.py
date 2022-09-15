from tkinter.messagebox import QUESTION
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')
st.header('This is a header')
st.subheader('This is a subheader')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress (0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.001)

'Done!!'



#st.write('Display Image')
#if st.checkbox('Show imgae'):
#    img = Image.open('one piece.jpeg')
#    st.image(img, caption = 'question', use_column_width = True)