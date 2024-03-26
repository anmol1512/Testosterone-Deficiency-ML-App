import pickle
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

class Model:
    def __init__(self) -> None:
        pass

    def SVM(self):
        svc = pickle.load(open('model/SVM_Model.pkl', 'rb'))
        return svc

    def XGB(self):
        xgb =  pickle.load(open('model/XGB_Model.pkl', 'rb'))
        return xgb

    def RF(self):
        rf =  pickle.load(open('model/RF_Model.pkl', 'rb'))
        return rf

    def neural_net(self):
        ann =  ANN()
        ann.load_state_dict(t.load('model/ANN_model.pth'))
        return ann

    def KNN(self):
        knn = pickle.load(open('model/KNN_Model.pkl', 'rb'))
        return knn
    
    def get_model(self,model_name):
        
        model = None
        if model_name == "SVM":
            model = self.SVM()
        
        elif model_name == "XGB":
            model = self.XGB()
        
        elif model_name == "RF":
            model = self.RF()
        
        elif model_name == "ANN":
            model = self.neural_net()

        elif model_name == "KNN":
            model = self.KNN()
        
        return model

        
    
    