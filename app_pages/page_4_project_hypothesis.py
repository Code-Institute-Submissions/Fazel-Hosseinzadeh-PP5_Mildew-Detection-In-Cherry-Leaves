import streamlit as st


def page_4_project_hypothesis_content():
    st.write(f"## **Project Hypothese** ")
    st.info(f"### **Hypothesis 1: Visual Identification of Powdery Mildew**")
    st.success(
            f"We hypothesize that there are distinct visual markers on cherry leaves that can help differentiate between healthy leaves and those affected by powdery mildew.\n\n"
            f"Affected leaves typically exhibit white or gray powdery spots on their surfaces, which are not present on healthy leaves.\n\n"
            f"By carefully examining these visual cues, it is possible to identify the presence of the disease, enabling timely intervention and treatment.\n\n"
            
        )


    st.info(f"### **Hypothesis 2: Machine Learning for Automated Detection**")

    st.success(
        f"We hypothesize that machine learning, specifically Convolutional Neural Networks (CNNs), can be effectively used to automate the detection of powdery mildew on cherry leaves.\n\n"
        f"By training a CNN on a labeled dataset of healthy and affected leaf images, the model can learn to recognize patterns and features associated with the disease.\n\n"
        f"This approach can provide accurate and rapid diagnosis, assisting in the early detection and management of powdery mildew.\n\n"
        
    )
