import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread

def page_5_ML_metrics_content():
    st.write(f"## **Machine Learning Metrics**")
    st.write("---")
    
    st.info(f"### **Table of Labels Distribution per each dataset bin**")
    
    #Load saved image of lables distribution
    version = 'v1'
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")
    
    