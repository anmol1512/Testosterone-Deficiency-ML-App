import pickle
import pandas as pd

xgb = pickle.load(open('model\XGB_Model.pkl', 'rb'))

df = pd.read_excel('data/ptestost.xlsx')
df = df[df['T'] == 1].drop(['T','Age'],axis = 1).sample(10)

print (df)
print(xgb.predict(df))
