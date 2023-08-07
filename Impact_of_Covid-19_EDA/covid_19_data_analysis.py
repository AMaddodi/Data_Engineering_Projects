import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Archana\Documents\DataAnalysis\python\covid_19_dataset\covid_19_india.csv",
                 parse_dates=['Date'], dayfirst=True)

# retrieve only required columns
df = df[['Date', 'State/UT', 'Cured', 'Deaths', 'Confirmed']]

# renaming column names 
df.columns = ['date', 'state', 'cured', 'deaths', 'confirmed']

today_cases = df[df.date == '2020-04-15']

max_cases = today_cases.sort_values(by='confirmed', ascending=False)

# Top 5 states with max confirmed cases
top_max_cases = max_cases[0:5]

# bar plot for states vs confirmed cases
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="state", y="confirmed", data=top_max_cases, hue='state')
plt.show()

# Death cases
max_death_cases = today_cases.sort_values(by='deaths', ascending=False)

# bar plot for states vs death
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="state", y="deaths", data=max_death_cases[0:5], hue='state')
plt.show()

# cured cases
cured_cases = today_cases.sort_values(by='cured', ascending=False)

# bar plot for states vs cured cases
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="state", y="cured", data=cured_cases[0:5], hue='state')
plt.show()

# top state
top_state = df[df.state == 'Maharashtra']

# line plot
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x="date", y="confirmed", data=top_state, color='g')
plt.show()

# line plot
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x="date", y="deaths", data=top_state, color='r')
plt.show()

# linear regression
top_state['date'] = top_state['date'].map(dt.datetime.toordinal)
x= top_state['date']
y = top_state['confirmed']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

lr = LinearRegression()

lr.fit(np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1))

lr.predict(np.array([[737527]]))
