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