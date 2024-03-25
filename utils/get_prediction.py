import torch as t

class Inference:
    def __init__(self,model,model_name):
        self.model = model
        self.model_name = model_name
    
    def predict(self,data):
        if self.model_name == "ANN":
            self.model.eval()
            with t.no_grad():
                pred = self.model(data).squeeze()
                threshold = 0.5
                pred = (pred >= threshold).int().item()
                return pred
        return self.model.predict(data)[0]

