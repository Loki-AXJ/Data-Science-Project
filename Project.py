# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load the data
df = pd.read_csv(r'c:\Users\malot\Downloads\greendestination (1) (1).csv')


# 3. Explore initial data
print(df.head())
print(df.columns.tolist())

# 4. Data quality check
print(df.info())
print(df.isnull().sum())
print(df['Attrition'].unique())

# 5. Attrition rate calculation
num_left = df[df['Attrition'] == 'Yes'].shape[0]
total = df.shape[0]
attrition_rate = (num_left / total) * 100
print("Attrition Rate (%):", attrition_rate)

# 6. Compare key averages by attrition status
means = df.groupby('Attrition')[['Age', 'YearsAtCompany', 'MonthlyIncome']].mean()
print("Average values by Attrition status:\n", means)

# 7. Boxplots for visualization
df.boxplot(column='Age', by='Attrition')
plt.title('Age vs Attrition')
plt.show()

df.boxplot(column='YearsAtCompany', by='Attrition')
plt.title('Years at Company vs Attrition')
plt.show()

df.boxplot(column='MonthlyIncome', by='Attrition')
plt.title('Monthly Income vs Attrition')
plt.show()

# 8. T-tests for statistical significance
from scipy.stats import ttest_ind
age_yes = df[df['Attrition']=='Yes']['Age']
age_no = df[df['Attrition']=='No']['Age']
t_stat_age, p_val_age = ttest_ind(age_yes, age_no)
print("T-test Age p-value:", p_val_age)

years_yes = df[df['Attrition']=='Yes']['YearsAtCompany']
years_no = df[df['Attrition']=='No']['YearsAtCompany']
t_stat_years, p_val_years = ttest_ind(years_yes, years_no)
print("T-test YearsAtCompany p-value:", p_val_years)

income_yes = df[df['Attrition']=='Yes']['MonthlyIncome']
income_no = df[df['Attrition']=='No']['MonthlyIncome']
t_stat_income, p_val_income = ttest_ind(income_yes, income_no)
print("T-test MonthlyIncome p-value:", p_val_income)

# 9. Examine effect of OverTime
print(df.groupby('OverTime')['Attrition'].value_counts(normalize=True).rename("proportion"))


