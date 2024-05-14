import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_2_Leaves_Study_content():
    st.write("### Leaves study")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a powdery-mildew leaf from an healthy leaf.")
    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.warning(
        f"* We notice the average and variability images did not show "
        f"patterns where we could intuitively differentiate one from another. " 
        f"However, a small difference in the colour pigment of the average images is seen for both labels.")

      st.image(avg_powdery_mildew, caption='Powdery-mildew Leaf - Average and Variability')
      st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average powdery-mildew and average healthy leaves"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* We notice this study didn't show "
            f"patterns where we could intuitively differentiate one from another.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/cherry-leaves-dataset/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):
        pass
      st.write("---")

