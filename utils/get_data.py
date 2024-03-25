from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import torch as t

class Data:
    def __init__(self, model_name, *args) -> None:
        self.Age = args[0]
        self.DM = args[1]
        self.TG = args[2]
        self.HT = args[3]
        self.HDL = args[4]
        self.AC = args[5]
        self.model_name = model_name
    
    def get_data(self):

        user_input = None
        columns = None
        df = None

        if self.model_name == "SVM":
            user_input = [[int(self.Age), int(self.TG), int(self.HT), float(self.HDL), float(self.AC)]]
            columns = ['Age', 'TG', 'HT', 'HDL', 'AC']
            df = pd.DataFrame(user_input, columns=columns)
        
        elif self.model_name == "XGB":
            user_input = [[int(self.DM), int(self.TG), int(self.HT), float(self.HDL), float(self.AC)]]
            columns = ['DM', 'TG', 'HT', 'HDL', 'AC']
            df = pd.DataFrame(user_input, columns=columns)
        
        elif self.model_name == "RF":
            user_input = [[int(self.Age), int(self.TG), float(self.HDL), float(self.AC)]]
            columns = ['Age', 'TG', 'HDL', 'AC']
            df = pd.DataFrame(user_input, columns=columns)

            scaler = MinMaxScaler()
            df = scaler.fit_transform(df)
            df = pd.DataFrame(df, columns=columns)
        
        elif self.model_name == "ANN":
            user_input = [[int(self.Age), int(self.TG), int(self.HT), float(self.HDL), float(self.AC)]]
            columns = ['Age', 'TG', 'HT', 'HDL', 'AC']
            df = pd.DataFrame(user_input, columns=columns)

            df = t.tensor(df.values, dtype = t.float32)
            scaler = StandardScaler()
            df = t.tensor(scaler.fit_transform(df), dtype = t.float32)


        elif self.model_name == "KNN":
            user_input = [[int(self.Age), int(self.DM), int(self.TG), int(self.HT), float(self.HDL), float(self.AC)]]
            columns = ['Age', 'DM', 'TG', 'HT', 'HDL', 'AC']
            df = pd.DataFrame(user_input, columns=columns)

        return df