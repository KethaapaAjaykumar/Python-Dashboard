# MAIN EXECUTION
#
import objective
import EDA-analysis
def main():
    print("========== Bank Customer Churn Analysis ==========")
    print("Choose a Module to Run:\n1 - EDA Analysis\n2 - Churn Insights & Objectives")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        eda_module(df)
    elif choice == '2':
        objective_insights_module(df)
    else:
        print("Invalid input. Please enter 1 or 2.")
if __name__ == "__main__":
    main()
