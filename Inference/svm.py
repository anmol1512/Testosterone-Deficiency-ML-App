import pickle
import pandas as pd
svc = pickle.load(open('model\SVM_Model.pkl', 'rb'))

df = pd.read_excel('data/ptestost.xlsx')
df = df[df['T'] == 1].drop(['T','DM'],axis = 1).sample(10)
print (df)
print(svc.predict(df))
