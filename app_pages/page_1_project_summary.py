import streamlit as st


def page_1_project_summary_content():

    st.write("### Quick Project Summary")
    st.info(
        f"**About The Project**\n\n"
        f"Powdery mildew is a fungal disease that affects cherry trees, causing significant yield loss.\n\n"
        f"This quick project aims to develop a user-friendly app to detect powdery mildew in cherry leaves using image recognition.\n\n"
        f"By uploading an image, you can potentially identify the health of your cherry leaves and take early action to protect your trees.\n\n"
        )

    st.warning(
        f"\n\n"
        f"**Project Dataset**\n\n"
        f"The dataset contains 4208 cherry leaf images from Kaggle: 2104 healthy and 2104 with powdery mildew.\n\n"
        f"Leaves individually photographed.\n\n"


        f"\n\n"
        )

    st.success(
        f"**Bussiness Requirements**\n\n"
        f"The project has 2 business requirements:\n\n"

        f" - 1 - The client is interested in having a study to differentiate a powdery-mildew cheary leaf and a healthy cherry leaf visually.\n\n"
        f" - 2 - The client is interested in telling whether a given cherry leaf picture is a powdery-mildew cheary leaf and a healthy cherry leaf.\n\n"

        )
     
