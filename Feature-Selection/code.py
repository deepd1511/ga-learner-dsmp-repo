# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here


# read the dataset
dataset = pd.read_csv(path)



# look at the first five columns
print(dataset.head(5))


# Check if there's any column which is not useful and remove it like the column id
dataset =  dataset.drop(['Id'],axis=1)

# check the statistical description
dataset.info()


# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = dataset.columns

#number of attributes (exclude target)
size = len(cols)-1

#x-axis has target attribute to distinguish between classes
x = dataset['Cover_Type']

#y-axis shows values of an attribute
y = cols.drop('Cover_Type')

#Plot violin for all attributes
for i in range(size):
    y_col_data = dataset[y[i]]
    sns.violinplot(x,y_col_data)


# --------------
import numpy
threshold = 0.5

# no. of features considered after ignoring categorical variables

num_features = 10

# create a subset of dataframe with only 'num_features'
subset_train = dataset.iloc[:,0:10]
cols = subset_train.columns

#Calculate the pearson co-efficient for all possible combinations
data_corr = subset_train.corr()
sns.heatmap(data_corr)
plt.show()
# Set the threshold and search for pairs which are having correlation level above threshold

# Sort the list showing higher ones first 
corr_var_list = []
for i in range(data_corr.shape[0]):
    for j in range(i+1):
        if (abs(data_corr.iloc[i,j])>0.5 and data_corr.iloc[i,j]!=1):
            corr_var_list.append(data_corr.iloc[i,j])
corr_var_list = sorted(corr_var_list,key=abs)
print("Corr Var List")
print(corr_var_list)
#Print correlations and column names




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)



# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
X = dataset.drop(["Cover_Type"],axis=1)
y = dataset["Cover_Type"]
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2,random_state=0)

X_train_temp = X_train.iloc[:,0:10]
X_test_temp = X_test.iloc[:,0:10]
print(X_train_temp.head(5))

X_train_categorical = X_train.iloc[:,10:]
X_test_categorical = X_test.iloc[:,10:]
#Standardized
#Apply transform only for non-categorical data
scaler = StandardScaler()
X_train_temp = pd.DataFrame(scaler.fit_transform(X_train_temp))
X_test_temp = pd.DataFrame(scaler.transform(X_test_temp))

#Concatenate non-categorical data and categorical
X_train1 = pd.concat([X_train_temp,X_train_categorical],axis=1)
X_test1 = pd.concat([X_test_temp,X_test_categorical],axis=1)

scaled_features_train_df = X_train1
scaled_features_test_df = X_test1





# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:
skb = SelectPercentile(score_func = f_classif,percentile=20)
#print(X_train1.head(5))
predictors = skb.fit_transform(X_train1,Y_train)
scores = list(skb.scores_)

top_k_index = sorted(range(len(scores)), key = lambda i: scores[i],reverse = True)[:predictors.shape[1]]
top_k_predictors = [scaled_features_train_df.columns[i] for i in top_k_index]

print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf = OneVsRestClassifier(LogisticRegression())
clf1 = OneVsRestClassifier(LogisticRegression())
model_fit_all_features = clf1.fit(X_train,Y_train)
predictions_all_features = model_fit_all_features.predict(X_test)
score_all_features = accuracy_score(Y_test,predictions_all_features)
print(score_all_features)
model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors],Y_train)
predictions_top_features = model_fit_top_features.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test,predictions_top_features)
print(score_top_features)



