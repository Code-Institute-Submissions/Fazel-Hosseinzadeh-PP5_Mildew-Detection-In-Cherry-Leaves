import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


def page_3_Live_detector_content():
    
    st.write(f"## **Live detector**")
    st.write("---")
    st.warning(f"Easily obtain instant analysis by uploading a photo of a cherry leaf to our machine learning model."
            f"The analysis yields a brief report showcasing the probability of the leaf being infected or healthy."
            f"This report is conveniently available for download in CSV format, ensuring quick access and"
            f"integration into your workflow.")
    st.write("---")
    st.write(f"* [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) "
               f"you can access **sample pictures** to test our ML model's performance." )
    
    images_buffer = st.file_uploader('Upload cherry leaves samples. You may select more than one.',
                                        type='JPG',accept_multiple_files=True)
    
   
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            print(f"{image}")
