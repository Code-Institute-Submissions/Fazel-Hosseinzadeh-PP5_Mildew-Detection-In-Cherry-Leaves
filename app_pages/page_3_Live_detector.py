import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
import plotly.express as px
import base64
from datetime import datetime



def page_3_Live_detector_content():
    
    st.write(f"## **Live detector**")
    st.write("---")
    st.success(f"Easily obtain instant analysis by uploading a photo of a cherry leaf to our machine learning model. "
            f"The analysis yields a brief report showcasing the probability of the leaf being infected or healthy. "
            f"This report is conveniently available for download in CSV format, ensuring quick access and "
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
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            
            # Download the report
            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
            
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)


def resize_input_image(img, version):  
    """
    Reshape image to average image size
    """
    file_path = f"outputs/{version}/image_shape.pkl"
    image_shape = joblib.load(filename=file_path)
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"outputs/{version}/cherry-leaves-mildew-detector-model.h5")

    pred_proba = model.predict(my_image)[0,0]

    target_map = {v: k for k, v in {'helthy': 0, 'powdery_mildew': 1}.items()}
    pred_class =  target_map[pred_proba > 0.5]  
    if pred_class == target_map[0]: pred_proba = 1 - pred_proba


    st.write(
        f"The predictive analysis indicates the sample leave is "
        f"**{pred_class.lower()}**.")
    
    return pred_proba, pred_class


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class= pd.DataFrame(
            data=[0,0],
            index={'helthy': 0, 'powdery_mildew': 1}.keys(),
            columns=['Probability']
        )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    
    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y=[0,1],
            width=600, height=300,template='seaborn')
    st.plotly_chart(fig)


def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href