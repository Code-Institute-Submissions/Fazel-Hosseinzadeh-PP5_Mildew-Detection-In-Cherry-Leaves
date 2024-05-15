import streamlit as st


def page_1_project_summary_content():

    st.write("## **Quick Project Summary**")
    st.write(f"---")
    st.info(f"### **About The Project**")
    
    st.success(  
        f"Powdery mildew is a fungal disease that affects cherry trees, causing significant yield loss.\n\n"
        f"This quick project aims to develop a user-friendly app to detect powdery mildew in cherry leaves using image recognition.\n\n"
        f"By uploading an image, you can potentially identify the health of your cherry leaves and take early action to protect your trees."
        )
    st.write(f"---")
    st.info(f"### **Project Dataset**")
    st.success(
        f"The dataset contains 4208 cherry leaf images from Kaggle: 2104 healthy and 2104 with powdery mildew.\n\n"
        f"Leaves individually photographed."
        )
    st.write(f"---")
    st.info(f"### **Bussiness Requirements**")
    st.success(
        
        f"The project has 2 business requirements:\n\n"

        f" - 1 - The client is interested in having a study to differentiate a powdery-mildew cheary leaf and a healthy cherry leaf visually.\n\n"
        f" - 2 - The client is interested in telling whether a given cherry leaf picture is a powdery-mildew cheary leaf and a healthy cherry leaf.\n\n"

        )
    st.write(f"* More information available [hear](https://github.com/Fazel-Hosseinzadeh/PP5_Mildew-Detection-In-Cherry-Leaves/blob/main/README.md) ")
    