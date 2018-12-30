# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

loan_status.plot(kind = 'bar')


# --------------
#Code starts here
property_and_loan = data.groupby(by = ["Property_Area","Loan_Status"])

property_and_loan = property_and_loan.size().unstack()

property_and_loan.plot(kind = 'bar', stacked = False,rot = 45)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")


# --------------
#Code starts here

education_and_loan = data.groupby(by= ['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()

education_and_loan.plot(kind = 'bar',stacked = True, rot = 45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.show()


# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

graduate.plot(kind = 'density',label ='Graduate')
not_graduate.plot(kind = 'density',label ='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3,1)

# Applicant Income
ai = data[['ApplicantIncome','LoanAmount']]
ai.plot(kind = 'scatter',x= 'ApplicantIncome',y='LoanAmount', ax = ax_1)
ax_1.set_title('Applicant Income')

# Co-applicant Income
ci = data[['CoapplicantIncome','LoanAmount']]
ci.plot(kind = 'scatter',x= 'CoapplicantIncome',y='LoanAmount', ax = ax_2)
ax_2.set_title('Coapplicant Income')

# Total Income
data['TotalIncome']= data['ApplicantIncome']+data['CoapplicantIncome']
ti = data[['TotalIncome','LoanAmount']]
ti.plot(kind = 'scatter',x= 'TotalIncome',y='LoanAmount', ax = ax_3)
ax_3.set_title('Total Income')





