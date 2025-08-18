# IBM_HR_analysis

**IBM HR Employee Attrition Analysis**

This repository contains a Python-based exploratory data analysis (EDA) project on the IBM HR Employee Attrition dataset. The analysis aims to uncover patterns and insights related to employee attrition, including key numerical and categorical features, correlations, and visual trends.

**🗂 Project Structure:**

IBM_HR_Attrition_Analysis/
│
├── WA_Fn-UseC_-HR-Employee-Attrition.csv   # Dataset
├── analysis.py                             # Jupyter Notebook with EDA
├── README.md                               # Project overview
└── requirements.txt                        # Python dependencies

**📋 Dataset:**

*Source*: IBM HR Analytics Employee Attrition & Performance dataset

*Description*: Contains demographic, job-related, and performance-related information about employees.

*Target Variable*: Attrition (Yes/No)

*Key Features:*

--Numerical: Age, MonthlyIncome, YearsAtCompany, TotalWorkingYears, etc.

--Categorical: Department, JobRole, MaritalStatus, Gender, OverTime, BusinessTravel, EducationField, etc.

**🛠 Tools & Libraries:**

--*Python 3.12*

--*Pandas – Data manipulation*

--*NumPy – Numerical computations*

--*Matplotlib – Data visualization*

--*Seaborn – Statistical data visualization*

*Install required libraries:*

--pip install pandas numpy matplotlib seaborn

**🚀 Analysis Steps**

--Load Dataset

--Read the CSV file into a Pandas DataFrame.

--Inspect shape, missing values, and basic statistics.

--Target Variable Distribution

--Visualize Attrition counts.

--Show percentages on bars for clarity.

--Numerical Feature Distributions

--Histograms for key numerical columns.

--Examine spread and skewness of data.

*Boxplots: Numerical Features vs Attrition*

--Compare distributions of numerical features grouped by attrition status.

--Categorical Feature Analysis

--Countplots for each categorical variable with Attrition hue.

--Helps to identify categories with higher attrition risk.

--Correlation Analysis

--Correlation heatmap for numerical features.

--Identify top features correlated with Attrition after binary encoding.

--Special Insights

--YearsAtCompany vs Attrition.

--YearsSinceLastPromotion vs Attrition.

--Helps uncover patterns in employee tenure and promotion history.

**📊 Visualizations:**

*The notebook produces a variety of visualizations including:*

Countplots for Attrition and categorical features

Histograms for numerical features

Boxplots comparing numerical features across attrition groups

Correlation heatmap

Special stacked histograms to show attrition trends over YearsAtCompany and YearsSinceLastPromotion

**🔑 Key Insights:**

The distribution of employees who leave vs. stay can be visually assessed.

Certain numerical and categorical features have stronger correlation with attrition.

Trends in tenure, promotions, and overtime may indicate higher attrition risk.

(Exact insights can be derived by running the notebook and analyzing outputs.)

**💻 How to Run:**

*Clone the repository:*

git clone https://github.com/Snehasish5/IBM_HR_analysis.git
cd IBM_HR_analysis


*Install dependencies:*

pip install -r requirements.txt

**📌 Notes:**

The Attrition column is binary (Yes = 1, No = 0) for correlation analysis.

All visualizations use Seaborn’s Set2 or coolwarm color palettes.

This analysis is purely exploratory and does not include predictive modeling.

**📂 License:**

This project is licensed under the MIT License – see the LICENSE file for details.