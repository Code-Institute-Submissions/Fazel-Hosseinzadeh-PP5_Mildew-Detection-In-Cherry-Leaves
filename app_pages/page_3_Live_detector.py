import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import joblib



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

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")
            
            
            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)

        
        if not df_report.empty:
            pass

def resize_input_image(img, version):  
    """
    Reshape image to average image size
    """
    file_path = f"outputs/{version}/image_shape.pkl"
    image_shape = joblib.load(filename=file_path)
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image
