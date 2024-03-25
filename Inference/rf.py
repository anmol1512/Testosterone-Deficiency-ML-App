import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

rf = pickle.load(open('model\RF_Model.pkl', 'rb'))

df = pd.read_excel('data/ptestost.xlsx')
df = df[df['T'] == 1].drop(['T','DM','HT'],axis = 1).sample(10)
columns = df.columns

scaler = MinMaxScaler()
df = scaler.fit_transform(df)
df = pd.DataFrame(df, columns=columns)


print (df)
print(rf.predict(df))