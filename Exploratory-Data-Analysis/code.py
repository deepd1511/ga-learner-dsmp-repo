# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




#Code starts here
data = pd.read_csv(path)
plt.plot(data['Rating'])

data = data[data['Rating']<=5]
plt.plot(data['Rating'])
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())
missing_data = pd.concat([pd.Series(total_null),pd.Series(percent_null)],axis=1)
missing_data.columns = ['Total','Percent']
#print(missing_data)

data.dropna(inplace = True)


total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1 = pd.concat([pd.Series(total_null_1),pd.Series(percent_null_1)],axis=1)
missing_data_1.columns = ['Total','Percent']
print(missing_data_1)
# code ends here


# --------------

#Code starts here
g = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
g.set_xticklabels(rotation = 90)
plt.title('Rating vs Category [BoxPlot]')


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts(dropna=False))

data['Installs'] = data['Installs'].str.replace("+","")
data['Installs'] = data['Installs'].str.replace(",","").astype(int)

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sns.regplot(x="Installs", y="Rating", data=data)
plt.title('Rating vs Installs [RegPlot]')


#Code ends here



# --------------
#Code starts here
print(data['Price'])
data['Price'] = data['Price'].str.replace("$","").astype(float)
sns.regplot(x="Price",y = "Rating",data=data)
plt.title("Rating vs Price [RegPlot]")



#Code ends here


# --------------

#Code starts here
#data['Genres'].unique()
data['Genres'] = data['Genres'].str.split(";").str[0]
#print(data['Genres'])
gr_mean = pd.DataFrame(data[['Genres','Rating']].groupby('Genres',as_index = False).mean())
print(gr_mean)
gr_mean.describe()
gr_mean = gr_mean.sort_values(by = 'Rating')
print(gr_mean.head(1))
print(gr_mean.tail(1))
#Code ends here


# --------------

#Code starts here
#print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
#print(data['Last Updated Days'])

sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


