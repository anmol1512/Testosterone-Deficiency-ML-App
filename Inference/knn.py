import pickle
import pandas as pd
knn = pickle.load(open('model\KNN_Model.pkl', 'rb'))

df = pd.read_excel('data/ptestost.xlsx')
df = df[df['T'] == 1].drop(['T'],axis = 1).sample(10)

print (df)
print(knn.predict(df))
