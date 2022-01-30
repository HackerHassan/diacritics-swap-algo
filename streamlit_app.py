# imports
# import plotly.express as px
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import ast
import functions

import docx
import unicodedata
import re
import pandas as pd
import re

st.set_page_config(
    page_title="Diacritics Insertion Algorithm",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)

# over here we are opening the 5p logo to personalize the Dash
image = Image.open('nur logo.png')
# st.image(image, caption='')

col1, col2 = st.columns(2)
with col1: st.image(image)
with col2:
    st.title('Diacritics')

company_name = 'Nur Publications'


st.markdown("""---""")
st.header('Inputs')

# |*****| text section |*****|

# st.subheader('Text')
short_story_string = "There was a very blessed man named Qasim Junayd. He was a very special person who was a member of the Hanafi madhab. He was a great lover of the 4 Imams and in particular loved Imam Abu Hanifa dearly. He was also someone who really focused on purifying his nafs by reading a portion of the quran daily and did not want to be like those from the qawm of lut AS."

# this is the place for input by user
input_text = st.text_input('Text Input', 'insert text here')
st.write('`Current Inputted Text:`', input_text)
# input_text = short_story_string

# this is the expander section with SAMPLE TEXT
expander = st.expander(
    "Copy this sample PASSAGE to see how the replacing function works")
expander.write(
    short_story_string)


# |*****| dictionary section |*****|

# this is the place for input by user
input_dict_str = st.text_input(
    'Dictionary/Diacritic Mapping Input', "{'insert':'insert', 'diacritics':'diacritics', 'here':'here'}")
st.write('`Current Inputted Diacritic Mapping:`', input_dict_str)
# st.subheader('Dictionary/Diacritic Input')

l1 = ['qasim', 'hanifa', 'imam', 'qawm', 'junayd', 'nafs', 'quran', 'lut']
l2 = ['qāsim', 'ḥanīfa', 'imām', 'qâwm', 'junaÿd', 'ńafs', 'qurān', 'lūt']
sample_dict = functions.to_dictionary(l1, l2)

expander = st.expander(
    "Copy this sample DICTIONARY to see how the replacing function works")
expander.write("`note:` these are not accurate and are only for reference")
expander.write(sample_dict)

if len(input_dict_str)==0:
    # st.write('`TRUE`')
    # st.write('input data into text box')
    st.write()
else:
    input_dict = ast.literal_eval(input_dict_str)
    # input_dict = sample_dict
    # the below two lines are useful for running the final script
    l3 = ["[[ " + w + " ]]" for w in list(input_dict.values())]
    curr_dict = functions.to_dictionary(input_dict.keys(), l3)

st.markdown("""---""")
# running full script section
st.subheader('Run the Diacritic Replacement Script')

if st.button('Run Script'):
    st.write("`OUTPUT:`")
    st.write(functions.paragraph_replace(input_text, curr_dict))
# else: st.write('Enter valid parameters')



# input_password = st.text_input('Password', 'Enter Password')
# st.write('The password you entered is incorrect, please try again')


# -----------------------------------------------
st.markdown("""---""")

# expander = st.expander("FAQ")
# expander.write(
#     "For any questions & suggestions, feel free to reach out to hassankhawaja@5ivepillars.com")
# st.write("For any question")
