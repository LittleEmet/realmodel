from Model import Net
import torch
import joblib
model = Net()
path=('model.pth')
model.load_state_dict(state_dict)
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
