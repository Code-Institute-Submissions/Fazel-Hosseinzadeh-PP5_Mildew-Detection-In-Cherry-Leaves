import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
import joblib

def page_5_ML_metrics_content():
    st.write(f"## **Machine Learning Metrics**")
    st.write("---")
    
    st.info(f"### **Table of Labels Distribution per each dataset bin**")
    
    #Load saved image of lables distribution
    version = 'v1'
    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")
    
    st.info(f"### **Model Learning Curve **")
    st.warning(f"The learning curve graph illustrates the model's performance on "
               f"both training and validation datasets over successive epochs, "
               f"highlighting trends such as underfitting, overfitting, and "
               f"optimal learning.\n\n This helps in evaluating how well the model "
               f"generalizes to unseen data.")
    
    # Load model learning curve Accuracy and Loss
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
    st.write("---")
    
    st.info(f"### **Model Performance with Restored Loss And Accuracy**")
    st.warning(f"Evaluating Loss and Accuracy Scores after Training.")
    
    evaluation = joblib.load(filename=f'outputs/{version}/evaluation.pkl')
    st.dataframe(pd.DataFrame(evaluation, index=['Loss', 'Accuracy']))