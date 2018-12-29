# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis =1)

null_values = banks.isnull().sum()
print(null_values)

bank_mode = banks.mode()

for col in banks.columns:
    mode_val = banks[col].mode()[0]
    banks[col].fillna(mode_val,inplace =True)

null_values = banks.isnull().sum()
print(null_values)
#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(data = banks, index = ['Gender','Married','Self_Employed'], values = ['LoanAmount'], aggfunc = 'mean')


# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]
#print(loan_approved_se.shape)
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]
#print(loan_approved_nse.shape)
loan_status_count = 614

percentage_se = (len(loan_approved_se)/loan_status_count)*100
#print(percentage_se)
percentage_nse = (len(loan_approved_nse)/loan_status_count)*100
#print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = sum(loan_term>=25)


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(by = 'Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


