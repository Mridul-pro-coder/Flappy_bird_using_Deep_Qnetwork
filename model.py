import torch 
import torch.nn as nn



class DQN(nn.Module):
    def __init__(self , STATE_SIZE= 12 , ACTION_SIZE= 2 , HIDDEN_SIZE= 256):
        super(DQN, self).__init__()
        
        self.model = nn.Sequential(
            #1st hidden layer
            nn.Linear(STATE_SIZE, HIDDEN_SIZE),
            nn.ReLU(),
            
            #2nd hidden layer
            nn.Linear(HIDDEN_SIZE, HIDDEN_SIZE),
            nn.ReLU(),

            #output layer
            nn.Linear(HIDDEN_SIZE, ACTION_SIZE)
        )
    
    def forward(self, x):
        return self.model(x)