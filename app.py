import streamlit as st
from app_pages.multipage import MultiPage

# load functions from each page
from app_pages.page_1_project_summary import page_1_project_summary_content
from app_pages.page_2_Leaves_Study import page_2_Leaves_Study_content
from app_pages.page_3_Live_detector import page_3_Live_detector_content
from app_pages.page_4_project_hypothesis import page_4_project_hypothesis_content
from app_pages.page_5_ML_metrics import page_5_ML_metrics_content



app = MultiPage(app_name="Cherry Leaves Powdery Mildew Detector")  # Create an instance of the app

# Add pages to app using add_page method
app.add_page("Quick Project Summary", page_1_project_summary_content)
app.add_page("Leaves Study", page_2_Leaves_Study_content)
app.add_page("Live Test", page_3_Live_detector_content)
app.add_page("Project Hypotheses", page_4_project_hypothesis_content)
app.add_page("Machine Learning Metrics", page_5_ML_metrics_content)



app.run()  # Run the app