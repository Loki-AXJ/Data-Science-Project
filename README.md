# "Attrition Analysis and Key Drivers in Green Destinations"

## Project Overview
This project analyzes employee attrition at Green Destinations using real HR data. The goal is to identify the overall attrition rate and understand which factors (age, tenure, income, overtime, etc.) most influence whether an employee stays or leaves.

## Table of Contents
- Project Overview
- Data Used
- Methodology
- Key Findings
- Visualizations
- How to Run
- Recommendations
- Contact

## Data Used
- `greendestination-1-1.csv`: Contains 1471 employee records and 35 HR features such as Age, Attrition Status, YearsAtCompany, MonthlyIncome, OverTime, JobRole, etc.

## Methodology
1. **Data Loading & Quality Check:** Explored columns, checked for missing values (none found), verified data types.
2. **Attrition Rate Calculation:** Calculated percentage of employees who left: **16.12%**.
3. **Key Averages:** Compared Age, YearsAtCompany, and MonthlyIncome for attrition groups.
4. **Visualizations:** Created boxplots for visual comparison.
5. **Statistical Testing:** Used t-tests to confirm significant differences.
6. **Further Analysis:** Assessed the impact of OverTime and other factors.

## Key Findings
- **Attrition Rate:** 16.12% employees have left.
- **Averages (No vs Yes Attrition):**
  - Age: 37.56 vs 33.61 years
  - YearsAtCompany: 7.37 vs 5.13
  - MonthlyIncome: 6832.74 vs 4787.09
- **Statistical Significance:**
  - Age, YearsAtCompany, and MonthlyIncome differences are statistically significant (p < 0.0001).
- **OverTime Impact:** Employees who work overtime have a 30.5% chance of leaving, compared to 10.4% for those who do not.

## Visualizations
- `Figure_1.jpg`: Boxplot - Age vs Attrition
- `Figure_2.jpg`: Boxplot - Years at Company vs Attrition
- `Figure_3.jpg`: Boxplot - Monthly Income vs Attrition

Each plot shows clear separation, with lower ages, tenure, and income associated with higher attrition.

## How to Run
1. Install dependencies:
pip install pandas matplotlib scipy
2. Place all files in one folder.
3. Run `Project.py` in your terminal or use the Jupyter notebook version.
4. Outputs:
- Numeric summary in terminal.
- Visualizations pop up and are saved.

## Recommendations
- Green Destinations should focus retention programs on younger, less-tenured, and overtime-working employees.
- Increase support, career development, and work-life balance for at-risk groups.

## Contact
For queries or collaboration, reach out to [Loki], [malothulokesh743@gmail.com].
