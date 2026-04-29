# model.py
import random

def get_deployment_strategy():
    
    strategies = ["heroku", "aws", "gcp"]
    return random.choice(strategies)
