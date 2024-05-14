import streamlit as st
from app_pages.multipage import MultiPage

# load functions from each page
from app_pages.page_1_project_summary import say_hi


app = MultiPage(app_name="Cherry Leaves Mildew Detector")  # Create an instance of the app

# Add pages to app using add_page method
app.add_page("Quick Project Summary", say_hi)


app.run()  # Run the app