import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import torch as t
import torch.nn as nn

class ANN(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden1 = nn.Linear(5, 256)
        self.gelu1 = nn.GELU()

        self.hidden2 = nn.Linear(256, 512)
        self.gelu2 = nn.GELU()

        self.output = nn.Linear(512, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.gelu1(self.hidden1(x))
        x = self.gelu2(self.hidden2(x))
        x = self.sigmoid(self.output(x))
        return x

df = pd.read_excel('data/ptestost.xlsx')
df = df[df['T'] == 1].drop(['T','DM'],axis = 1).sample(1)
print (df)
df = t.tensor(df.values, dtype = t.float32)

scaler = StandardScaler()
df = t.tensor(scaler.fit_transform(df), dtype = t.float32)

ann = ANN()
ann.load_state_dict(t.load('model\ANN_model.pth'))
ann.eval()


# y_pred = ann(df)
# threshold = 0.5
# y_pred = (y_pred >= threshold).float()
# y_pred = y_pred.numpy()
with t.no_grad():
    pred = ann(df).squeeze()
    threshold = 0.5
    pred = (pred >= threshold).int().item()
print(pred)

