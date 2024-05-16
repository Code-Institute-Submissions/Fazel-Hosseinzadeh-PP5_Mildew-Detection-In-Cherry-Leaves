********************

# Mildew Detection In Cherry Leaves
********************

### [View the live project here](https://cherryleaf-mildew-detector-11309237d5ff.herokuapp.com/)
********************


## Table Of Contents
********************

1.  [Intrudoction](#intruduction)
2.  [Dataset Content](#dataset-content)
3.  [Business Requirements](#business-requirements)
4.  [Hypotheses and how to Validate](#hypotheses-and-how-to-validate)
5.  [Aligning Business Needs with Visualizations and ML](#aligning-business-needs-with-visualizations-and-ml)
6.  [Project Workflow CRISP-DM Approach](#project-workflow-crisp-dm-approach)
7.  [ML Business Case](#ml-business-case)
8.  [User Story](#user-story)
9.  [Dashboard Design Using Streamlit](#dashboard-design-using-streamlit)
10. [Unfixed Bugs](#unfixed-bugs)


********************

### Intrucudtion

This project employs a machine learning model to detect powdery mildew on cherry leaves, distinguishing between healthy and infected leaves. Utilizing a supervised binary classification model and convolutional neural networks (CNNs), the Powdery Mildew Detector analyzes leaf images to provide accurate health assessments. The application offers a user-friendly interface for growers to identify and manage disease in cherry trees efficiently.

[Table Of Contents](#table-of-contents)
********************


### Dataset Content

The dataset utilized in this project is sourced from Kaggle and contains 4208 images of cherry leaves, taken from the client's crop fields. This dataset features an equal number of healthy leaves and leaves affected by powdery mildew, a biotrophic fungus that poses a significant threat to cherry crops. The images, presented against a neutral background, provide a clear view of the leaf conditions, enabling precise analysis and model training. The cherry plantation crop is a flagship product for the client, making the detection of powdery mildew crucial for maintaining product quality and market reputation.

[Link to Kaggle dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

[Table Of Contents](#table-of-contents)
********************

### Business Requirements

**Client:** Farmy & Foods

**Challenge:**
Farmy & Foods are facing issues with powdery mildew on their cherry plantations. The current method involves manual inspection, where an employee takes about 30 minutes per tree to check for the fungus and an additional minute to apply a fungicide if powdery mildew is detected. This manual process is time-consuming and impractical due to the large number of cherry trees spread across multiple farms.

**Proposed Solution:**
The IT team has suggested implementing a Machine Learning (ML) system that can instantly detect powdery mildew using images of cherry leaves. If successful, this system could be extended to other crops facing similar issues.

**Summary of Business Requirements:**

1. Study to Visually Differentiate Leaves:
    * Conduct a study to differentiate healthy cherry leaves from those affected by powdery mildew through visual analysis.

    * This study should include creating average and variability images for each class (healthy vs. powdery mildew).

2. **Prediction of Leaf Health:**
    *   Develop an ML model capable of predicting whether a cherry leaf is healthy or infected with powdery mildew with at least 97% accuracy.

    *   The model should be able to process images quickly and accurately to facilitate immediate action.

3.  **Dashboard Requirements:**

    *   Develop a responsive dashboard that displays predictions on the health of cherry leaves.

    *   The dashboard should be user-friendly and accessible on various devices.

    *   It should also provide detailed prediction reports for the examined leaves.

4.  **Scalability and Replicability:**

    *   Ensure that the solution is scalable to handle thousands of cherry trees.

    *   If successful, the system should be replicable for other crops and pest detection scenarios.

5.  **Prediction Report:**

    *   Generate a detailed prediction report for each leaf analyzed, indicating whether it is healthy or infected.

    *   Include explanations of possible outcomes to assist users in understanding the predictions.

6.  **Accuracy Requirements:**

    *   The ML system must achieve a minimum prediction accuracy of 97% to be considered successful.

7.  **Technical Considerations:**
    *   Use a dataset of cherry leaf images provided by Farmy & Foods.

    *   Implement a neural network model to map the relationship between image features and labels (healthy vs. powdery mildew).

[Table Of Contents](#table-of-contents)
********************

###  Hypotheses and how to Validate

**Hypothesis 1: Differentiation of Infected Leaves**

**Hypothesis:** Infected leaves exhibit distinct marks that differentiate them from healthy leaves.

**Validation Approach:**

1.  **Image Dataset Collection:** Gather images of both healthy and powdery mildew-affected cherry leaves.

**Healthy Leaf Sample**

![Healthy Leaf Sample](/readme-images/healthy.jpg)

**Powdery-Mildew Leaf Sample**

![Pwdery-Mildew Leaf Sample](/readme-images/mildew.jpg)

2.  **Image Montage Creation:** Create image montages to visually compare healthy and infected leaves.

![montage](/readme-images/montage.jpg)


3. **Average Image Analysis:** Generate average images for healthy and infected leaves to identify common visual patterns.

![montage](/readme-images/ave-difference.jpg)

4.  **Statistical Analysis:** Analyze the difference between average images of healthy and infected leaves.

![montage](/readme-images/difference.jpg)

**Observations:**
-   Powdery mildew manifests as white, dusty patches on leaves.

-   Healthy leaves have a rich, dark green color.

-   Infected leaves show light, roughly-circular, powdery patches.

-   Average images for infected leaves reveal more white stripes, but variability images did not show a definitive pattern.

**Hypothesis 2: Machine Learning Model Performance**

**Hypothesis:** A machine learning model can accurately differentiate between healthy and powdery mildew-affected cherry leaves with a precision of at least 97%.

**Validation Approach:**
1.  **Model Development:** Build and train a Convolutional Neural Network (CNN) on the collected dataset.

2.  **Model Evaluation:** Validate the model's performance using metrics like accuracy, model learning curve,generalized model and overfitting underfitting.

3. **Cross-Validation:** Apply cross-validation techniques to ensure generalizability.

*   **Observations:**
    -   The model achieved a high degree of accuracy (up to 99%) in distinguishing between healthy and infected leaves.

    -   Performance metrics indicated reliable predictions with a recall of 99% for powdery mildew detection.

[Table Of Contents](#table-of-contents)
********************

### Aligning Business Needs with Visualizations and ML

**Business Requirements and Mapping:**

1.    **Visually differentiate cherry leaves:**
*   **Client Need:** 
Farmy & Foods aims to visually differentiate between healthy cherry leaves and those affected by powdery mildew. This is crucial for quality control and disease management in their cherry farming operations.

*   **Mapped Tasks:**

    *   **Image Montage:** Utilizing the Cherry Leaves Visualizer page, **"LEAVES STUDY"**, the application will compile visual montages showcasing healthy and infected leaves, allowing easy visual comparison.

    *   **Average vs. Variability Imagery:** Through visualizations, users can discern differences in color consistency and patterns between healthy and infected leaves.
    
    *   **Difference in Average Imagery:** Providing comparisons of average images highlights visual disparities between healthy and infected leaves.

2.  **Predict leaf health:** 
    *   **Client Need:** Farmy & Foods requires a robust machine learning model to accurately predict whether a cherry leaf is healthy or infected with powdery mildew. This predictive capability streamlines disease detection and enables proactive management strategies.

    *   **Mapped Tasks:** 
        *   **Real-time Prediction:** The Powdery Mildew Detector page offers a user-friendly interface for uploading cherry leaf images and receiving instant predictions on their health status.

        *   **Model Performance Metrics:** The Machine Learning Performance Indicators page provides insights into the model's accuracy, losses, and overall performance, ensuring stakeholders are informed about the model's reliability.

        *   **Model Validation:** Rigorous validation procedures ensure the model's robustness and generalization capabilities, crucial for real-world applications.

        *   **Additional Insights (Future Consideration):** Potential expansion to include economic implications of undetected infections, highlighting revenue loss due to compromised leaf quality.


[Table Of Contents](#table-of-contents)
********************

### Project Workflow CRISP-DM Approach

1.  **Introduction to CRISP-DM:**
    CRISP-DM, or the Cross-Industry Standard Process for Data Mining, serves as a structured methodology for guiding data mining projects. It encompasses six distinct stages, each crucial for the successful execution of a data-driven project.

2.  **Utilizing CRISP-DM:**
    In our cherry leaf disease detection project, CRISP-DM provides the framework through which we organize and execute our tasks. By aligning our project phases with CRISP-DM stages, we ensure a systematic and thorough approach to achieving our objectives.

3.  **CRISP-DM Process Overview:**
    The CRISP-DM methodology includes the following stages:
    *   **Business Understanding:**
        Identifying project objectives and requirements, as well as assessing the current business situation.
    
    *   **Data Understanding:**
        Collecting, exploring, and assessing the quality of the data available for analysis.

    *   **Data Preparation:**
        Preprocessing, cleaning, and transforming the data into a suitable format for modeling.
    *   **Modeling:**
        Selecting appropriate modeling techniques and building predictive models based on the prepared data.
    *   **Evaluation:**
        Assessing the performance of the models generated and validating their effectiveness in meeting the project objectives.
    *   **Deployment:**
        Integrating the developed models into operational systems for real-world use and ensuring their continued performance and maintenance.

        ![CRISP-DM](/readme-images/crisp-dm.png)


4.  **Project Implementation:**
    *   **Business Understanding:**
        Our primary goal is to develop an AI model capable of accurately distinguishing between healthy cherry leaves and those infected with powdery mildew. This addresses the need for an automated solution to replace the time-consuming and error-prone manual inspection process.

    *   **Data Understanding:** We collect and explore a dataset comprising images of cherry leaves, both healthy and infected, to gain insights into the characteristics of each class.

    *   **Data Preparation:**
        We preprocess and clean the collected data, ensuring its readiness for model training. This involves tasks such as removing noise, handling anomalies, and splitting the data into appropriate sets for training, validation, and testing.
    
    *   **Modeling:**
        We select a convolutional neural network (CNN) as the appropriate model for our image classification task. Using TensorFlow and Keras, we configure and train the model, leveraging techniques such as data augmentation to enhance its robustness.
    
    *   **Evaluation:**
        We evaluate the trained model's performance using various metrics such as accuracy and monitor the learning curve to avoid overfitting and underfitting. Additionally, we test the model on a separate hold-out dataset to assess its generalization capability.

    *   **Deployment:**
        The final model is integrated into a Streamlit dashboard, providing users with a user-friendly interface for uploading cherry leaf images and obtaining predictions. Visualizations of the dataset and model performance are also included in the dashboard for enhanced insights.

5.  **Benefits of CRISP-DM:**
    By adhering to the CRISP-DM methodology, we ensure a structured and disciplined approach to our project. This not only facilitates collaboration and communication among team members but also enhances the likelihood of achieving our objectives in a timely and efficient manner. Furthermore, the clear delineation of project phases and tasks provided by CRISP-DM enables effective project management and risk mitigation, ultimately leading to successful project outcomes aligned with business requirements.


[Table Of Contents](#table-of-contents)
********************

### ML Business Case

*   We are developing a supervised machine learning model tailored specifically for classifying cherry leaves as either healthy or infected with powdery mildew. Utilizing a dataset of 4208 images sourced from the client's crop fields via Kaggle, our primary goal is to equip farmers with a swifter and more dependable diagnostic tool.

*   Currently, the detection process relies heavily on manual verification, with workers dedicating around 30 minutes per tree to visually inspect leaves for signs of powdery mildew. This method, however, is both time-consuming and susceptible to human errors, emphasizing the urgent need for an automated solution.

*   Our model will produce a flag indicating leaf health alongside its associated probability, empowering farmers to swiftly identify infected trees and take necessary actions. With a stringent accuracy target of at least 97% on the test set, our aim is to significantly enhance the efficiency and accuracy of the diagnostic process.

*   Through the utilization of machine learning techniques, we anticipate a notable reduction in both the time required and potential inaccuracies associated with manual verification. Ultimately, this initiative will provide farmers with a more reliable means of diagnosing powdery mildew in cherry trees, thereby improving overall crop management practices.

[Table Of Contents](#table-of-contents)
********************
### User Story

1.  As a client, I want an easy-to-use dashboard to view and understand the data, model, and outcomes.
2.  As a client, I want to visually differentiate between healthy cherry leaves and those infected with powdery mildew by viewing average and variability images for each classification.
3.  As a client, I want to understand the visual differences between an average healthy cherry leaf and one infected with powdery mildew.
4.  As a client, I want to view an image montage displaying both healthy cherry leaves and those infected with powdery mildew for visual differentiation.
5.  As a client, I want to upload cherry leaf images and receive predictions with over 97% accuracy, enabling quick assessment of cherry tree health.
6.  As a client, I want a downloadable report summarizing the predictions made by the machine learning model.

*   **Implementation:**
To address these user stories, we developed an interactive Streamlit dashboard and a Data Visualization notebook. The dashboard offers clients the following functionalities:

    *   Seamless upload of cherry leaf images in .jpeg format, supporting multiple uploads up to 200MB total size.
    *   Display of uploaded images alongside prediction statements indicating infection status (healthy or infected with powdery mildew) and associated probabilities.
    *   Provision of a downloadable report summarizing the machine learning predictions on new leaves, facilitating documentation and analysis for future reference.

[Table Of Contents](#table-of-contents)
********************

### Dashboard Design Using Streamlit
**Page 1: Quick Project Summary**

**About The Project:**
Summary of the project's goal to develop an app for detecting powdery mildew in cherry leaves using image recognition.

**Project Dataset:**
Overview of the dataset containing cherry leaf images.

**Business Requirements:**
Outline of the two main business requirements for the project.

![Quick Project Summary](/readme-images/page1.jpg)

**Page 2: Leaves Study**

**Study Introduction:**
Overview of the client's interest in visually differentiating powdery-mildew leaves from healthy ones.

**Analysis Options:**
Selection of options for customizing the study, including differences in average and variability, between average powdery-mildew and healthy leaves, and image montage.

![Leaves Study](/readme-images/page2.jpg)

**Page 3: Live Test**

**Test Introduction:**
Explanation of the live test feature allowing users to upload cherry leaf photos for instant analysis.

**Upload Widget:**
User interface for uploading leaf images.
Prediction Display: Display of the uploaded image with a prediction statement indicating infection status and probability.

**Report Generation:**
Information on downloading a report containing image names and prediction results.

![Live Test](/readme-images/page3.jpg)

**Page 4: Project Hypotheses and Validation**

**Hypothesis 1:**
Detailing the hypothesis of visual identification of powdery mildew on cherry leaves.

**Hypothesis 2:**
Detailing the hypothesis of using machine learning for automated detection.

**Validation:**
Explanation of how each hypothesis was tested and the resulting conclusions.

![Project Hypotheses](/readme-images/page4.jpg)

**Page 5: ML Metrics**

**Label Distribution:**
Table displaying label frequencies for each dataset bin.

**Model Learning Curve:**
Graph illustrating the model's performance trends during training and validation.

**Performance Evaluation:**
Details of the model's loss and accuracy scores after training.

![Machine Learning Metrics](/readme-images/page5-1.jpg)

![Machine Learning Metrics](/readme-images/page5-2.jpg)

[Table Of Contents](#table-of-contents)
********************

####    Unfixed Bugs

*   There are no known unfixed bugs.



[Table Of Contents](#table-of-contents)
********************