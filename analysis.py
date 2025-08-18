import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# =========================
# 1. Load Data
# =========================
df = pd.read_csv(r"D:\Project\IBM_HR_ANALYSIS\WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Set theme
sns.set_theme(style="whitegrid", palette="Set2")

# =========================
# 2. Basic Exploration
# =========================
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum().sort_values(ascending=False).head(10))
print("\nAttrition Distribution:\n", df["Attrition"].value_counts(normalize=True))
print("\nSummary Statistics:\n", df.describe())

# =========================
# 3. Target Variable Distribution
# =========================
plt.figure(figsize=(7,5))
ax = sns.countplot(data=df, x="Attrition", palette="Set2")
plt.title("Attrition Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Attrition", fontsize=12)
plt.ylabel("Number of Employees", fontsize=12)

# Show percentages on bars
total = len(df)
for p in ax.patches:
    percentage = f'{100 * p.get_height() / total:.1f}%'
    x = p.get_x() + p.get_width() / 2
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# =========================
# 4. Numerical Distributions
# =========================
num_cols = ["Age", "MonthlyIncome", "YearsAtCompany", "TotalWorkingYears"]

df[num_cols].hist(figsize=(12,8), bins=20, color="skyblue", edgecolor="black")
plt.suptitle("Distribution of Key Numerical Features", size=16, fontweight="bold")
for ax in plt.gcf().axes:
    ax.set_xlabel(ax.get_title(), fontsize=11)
    ax.set_ylabel("Count", fontsize=11)
    ax.set_title("")
plt.tight_layout()
plt.show()

# =========================
# 5. Boxplots: Numerical Features vs Attrition
# =========================
fig, axes = plt.subplots(2, 2, figsize=(13,7))
for i, col in enumerate(num_cols):
    sns.boxplot(data=df, x="Attrition", y=col, ax=axes[i//2, i%2], palette="coolwarm")
    axes[i//2, i%2].set_title(f"{col} vs Attrition", fontsize=12, fontweight="bold")
    axes[i//2, i%2].set_xlabel("Attrition", fontsize=11)
    axes[i//2, i%2].set_ylabel(col, fontsize=11)
plt.tight_layout()
plt.show()

# =========================
# 6. Categorical Analysis with Attrition
# =========================
cat_cols = ["Department", "JobRole", "MaritalStatus", "Gender", "OverTime", "BusinessTravel", "EducationField"]

for col in cat_cols:
    plt.figure(figsize=(10,5))
    ax = sns.countplot(data=df, x=col, hue="Attrition", palette="Set2", order=df[col].value_counts().index)
    plt.title(f"Attrition by {col}", fontsize=13, fontweight="bold")
    plt.xlabel(col, fontsize=11)
    plt.ylabel("Number of Employees", fontsize=11)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

# =========================
# 7. Correlation Heatmap
# =========================
plt.figure(figsize=(12,8))
corr = df.corr(numeric_only=True)

# Plot mask for upper triangle
mask = np.triu(corr)
sns.heatmap(corr, cmap="coolwarm", center=0, mask=mask, annot=False, cbar=True)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# Show top correlated features with Attrition (if binary encoded)
if "Attrition" in df.columns:
    # Convert Attrition to numeric (Yes=1, No=0)
    df["Attrition_n"] = df["Attrition"].map({"Yes":1, "No":0})
    corr_target = df.corr(numeric_only=True)["Attrition_n"].sort_values(ascending=False)
    print("\nTop Features Correlated with Attrition:\n", corr_target.head(10))

# =========================
# 8. Special Insights
# =========================
plt.figure(figsize=(10,6))
sns.histplot(data=df, x="YearsAtCompany", hue="Attrition", multiple="stack", bins=20, palette="Set2")
plt.title("Attrition by Years at Company", fontsize=13, fontweight="bold")
plt.xlabel("Years at Company", fontsize=11)
plt.ylabel("Number of Employees", fontsize=11)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(data=df, x="YearsSinceLastPromotion", hue="Attrition", multiple="stack", bins=15, palette="Set1")
plt.title("Attrition by Years Since Last Promotion", fontsize=13, fontweight="bold")
plt.xlabel("Years Since Last Promotion", fontsize=11)
plt.ylabel("Number of Employees", fontsize=11)
plt.tight_layout()

plt.show()