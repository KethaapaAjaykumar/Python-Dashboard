import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Load data file (I have taken the data in  csv formt)
df = pd.read_csv("C:\\Users\\ajayk\\Desktop\\Bank_Churn.csv")

# MODULE 1: EDA ANALYSIS (Visualizing + Cleaning of data )
def eda_module(df):
    print("\nEDA ANALYSIS0")
    print("\nStep 1: Checking for Null Values")
    print(df.isnull().sum())
    print("\nStep 2: Removing Duplicate Records")
    df.drop_duplicates(inplace=True)
    print("Duplicates removed successfully.")
    print("\nStep 3: Correlation Matrix (All Numeric Features present in the file)")
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
    print("\nStep 4: Covariance Matrix for CreditScore', 'Age', 'Balance', 'EstimatedSalary")
    cov_columns = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary']
    print("Selected columns for covariance matrix:", cov_columns)
    print(df[cov_columns].cov())
    print("\nStep 5: Outlier Detection using Boxplot")
    num_cols = ['CreditScore', 'Age', 'Balance']
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[num_cols], orient='h')
    plt.title("Outlier Detection: Credit Score, Age, Balance")
    plt.xlabel("Values")
    plt.tight_layout()
    plt.show()
    print("\nStep 6: Pairplot for Key Numerical Features")
    pairplot_columns = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Exited']
    print("Pairplot columns:", pairplot_columns)
    sampled_df = df.sample(500, random_state=1)
    sns.pairplot(sampled_df[pairplot_columns], hue='Exited')
    plt.suptitle("Pairplot of Selected Features (Sample of 500 Records)", y=1.02)
    plt.show()
#PRESS 1 for eda analysis

