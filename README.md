
# Diabetes Predictive Analysis

## Introduction

This repository contains a comprehensive analysis aimed at predicting diabetes outcomes using various machine learning models. The analysis involves data preprocessing, exploratory data analysis, and the application of multiple classification models to determine the most accurate predictor for diabetes.

Hugging Face Link: https://huggingface.co/spaces/utomon/PredictionDiabetes

## Libraries Used

The following Python libraries were used in this project:

- **pandas**: For data manipulation and analysis.
- **seaborn**: For data visualization.
- **numpy**: For numerical computations.
- **matplotlib.pyplot**: For creating static, animated, and interactive visualizations.

### Statistical Analysis Libraries
- **scipy.stats**:
  - `kendalltau`, `spearmanr`, `chi2_contingency`: For statistical tests to evaluate correlations and associations between variables.

### Scikit-Learn Libraries
- **Model Selection**:
  - `train_test_split`, `StratifiedKFold`, `cross_val_score`, `RandomizedSearchCV`: For splitting the data, performing cross-validation, and tuning hyperparameters.
- **Preprocessing**:
  - `MinMaxScaler`, `OrdinalEncoder`, `OneHotEncoder`: For scaling and encoding features.
  - `ColumnTransformer`: For applying different preprocessing steps to different subsets of the features.
- **Pipeline**:
  - `Pipeline`, `make_pipeline`: For automating the workflow from data preprocessing to model training.

### Machine Learning Models
- **KNeighborsClassifier**: A simple, instance-based learning algorithm.
- **SVC (Support Vector Classifier)**: A powerful model for classification, which was determined to be the best in this analysis.
- **DecisionTreeClassifier**: A tree-based model for classification.
- **AdaBoostClassifier**: An ensemble model that combines multiple weak learners.
- **RandomForestClassifier**: An ensemble of decision trees.

### Evaluation Metrics
- **classification_report**, `recall_score`, `f1_score`, `precision_score`, `accuracy_score`: Metrics to evaluate the performance of the models.
- **ConfusionMatrixDisplay**: For visualizing the confusion matrix.

### Additional Libraries
- **feature_engine.outliers**:
  - `Winsorizer`: For handling outliers in the dataset.
- **pickle**: For saving and loading trained models.

## Analysis and Results

### Data Preprocessing
- The dataset was first explored and cleaned to handle missing values and outliers. 
- Various feature scaling and encoding techniques were applied to ensure the data was in the best format for model training.

### Model Training and Evaluation
Multiple machine learning models were trained and evaluated on the dataset:

1. **K-Nearest Neighbors (KNN)**
2. **Support Vector Machine (SVM)**
3. **Decision Tree**
4. **AdaBoost**
5. **Random Forest**

### Conclusion
After extensive testing and cross-validation, it was determined that the **Support Vector Machine (SVM)** model outperformed the others in terms of accuracy, precision, recall, and F1-score, making it the best model for predicting diabetes outcomes in this dataset.
