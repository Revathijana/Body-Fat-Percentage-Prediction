Body Fat Percentage Prediction using Machine Learning
Overview
This project aims to predict body fat percentage using machine learning techniques, specifically linear regression. The prediction model utilizes various physiological parameters such as age, weight, height, and body circumference measurements.

Problem Statement
Accurately measuring body fat percentage is often inconvenient and costly. This project seeks to provide a convenient and accessible method to estimate body fat percentage using readily available anthropometric measurements.

Dataset
The dataset used includes the following features:

Age (years)
Weight (lbs)
Height (inches)
Neck circumference (cm)
Chest circumference (cm)
Abdomen 2 circumference (cm)
Hip circumference (cm)
Thigh circumference (cm)
Knee circumference (cm)
Ankle circumference (cm)
Biceps (extended) circumference (cm)
Forearm circumference (cm)
Wrist circumference (cm)
Methodology
Data Preprocessing: The dataset undergoes preprocessing steps such as converting weight and height from lbs/in to kg/m, calculating BMI, and deriving ratios like the AC ratio (Abdomen Chest Ratio) and HTratio (Hip Thigh Ratio).
Model Building: Several regression models are trained and evaluated to predict body fat percentage, including Linear Regression, ElasticNet, Lasso, Ridge Regression, Support Vector Regression (SVR), Gradient Boosting, Bayesian Ridge, Random Forest, and Kernel Ridge Regression.
Model Evaluation: Models are evaluated based on metrics such as R-squared score (R2) and Root Mean Squared Error (RMSE) to assess prediction accuracy.
Installation
To run the code locally, ensure you have Python installed along with the necessary libraries specified in requirements.txt.

bash
Copy code
pip install -r requirements.txt
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the main script or notebooks to train models and predict body fat percentage.
Files Included
data/: Contains the dataset (bodyfat.csv) used for training and testing.
models/: Contains trained models saved as joblib files.
notebooks/: Jupyter notebooks for data exploration, preprocessing, model training, and evaluation.
scripts/: Python scripts for specific tasks like model training and prediction.
requirements.txt: List of Python dependencies required to run the project.
Contributors
Your Name
Co-contributor Name (if applicable)
References
Gallagher, D., et al. "Healthy percentage body fat ranges: an approach for developing guidelines based on body mass index." The American journal of clinical nutrition 72.3 (2000): 694-701.
Siri, W. E. (1956). Body composition from fluid spaces and density: analysis of methods. Techniques for Measuring Body Composition, 61-80.
Include any additional references as needed.
License
This project is licensed under the MIT License - see the LICENSE file for details.