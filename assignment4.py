import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt
import streamlit as st

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Assignment 4")
question = '''1)choose any dataset from given websites(dataset_repo.txt) and use NumPy,Pandas,Seaborn Libraries and deploy using Streamlit  in heroku cloud application?
* There must Complete Analaysis Using NumPy,Pandas,Seaborn Libraries'''
st.write(question)


#import dataset
st.header("COVID 19 INDIA")
df = pd.read_csv('covid_19_india.csv')
first = df.head(20)
st.table(first)

####status of kerala
g = df.groupby('State/UnionTerritory')
kerala = g.get_group('Kerala')
# kerala.plot(kind='bar')
# st.pyplot()

#details of kerala
k1 = kerala['Date']
k2 = kerala['Cured']
k3 = kerala['Deaths']
k4 = kerala['Confirmed']
nk1 = np.array(k1)
nk2 = np.array(k2)
nk3 = np.array(k3)
nk4 = np.array(k4)

#details of india
i1 = df['Date']
i2 = df['Cured']
i3 = df['Deaths']
i4 = df['Confirmed']
ni1 = np.array(i1)
ni2 = np.array(i2)
ni3 = np.array(i3)
ni4 = np.array(i4)

st.subheader("Kerala Cases")
plt.plot(k1,k4)
plt.xlabel('day')
plt.ylabel('cases')
st.pyplot()

st.subheader("India Cases")
plt.plot(i1,i4)
plt.xlabel('day')
plt.ylabel('cases')
st.pyplot()

st.subheader("India vs Kerala Cases Comparision")
# plt.ylim(0,1950000)
plt.plot(i1,i4)
plt.plot(k1,k4)
plt.xlabel('day')
plt.ylabel('cases')
st.pyplot()


#jointplot sns
st.subheader("JointPlot -- Kerala")
sns.jointplot(x='Confirmed',y='Deaths',data=kerala,kind='scatter')
st.pyplot()



st.subheader("Detailed View of States")
# SelectBox
state = st.selectbox("Select State",['Kerala','Tamil Nadu','Telangana','Karnataka', 'Maharashtra', 'West Bengal'])
st.write("You selected this option",state)
state1 = g.get_group(state)
s1 = state1['Date']
s2 = state1['Cured']
s3 = state1['Deaths']
s4 = state1['Confirmed']
ns1 = np.array(s1)
ns2 = np.array(s2)
ns3 = np.array(s3)
ns4 = np.array(s4)
length = len(ns1)
v = ns1[[1,int(length/4),int(length/2),int(length/(3/2)),(length-1)]]
vv = ns4[[1,int(length/4),int(length/2),int(length/(3/2)),(length-1)]]
vvv = ns3[[1,int(length/4),int(length/2),int(length/(3/2)),(length-1)]]
vvvv = ns2[[1,int(length/4),int(length/2),int(length/(3/2)),(length-1)]]
y = {'Date' : v,
    'Confirmed' : vv,
    'Cured' : vvvv,
    'Dead' : vvv}
ffff = pd.DataFrame(y)
st.table(ffff)

