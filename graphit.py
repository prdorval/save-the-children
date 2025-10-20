import plotly 
import plotly.express as px 
import random

participants = ["Gabe","Jordan","Olie","Mathias","Bryan"] 
min_contrib = 5
max_contrib = 25
contributions = [random.randint(min_contrib, max_contrib) for x in range(len(participants))]

# print(contributions)

data = {
    "participants": participants, 
    "contributions": contributions
}

print(data)

# Visualize the results.
fig = px.bar(x=participants, y=contributions)
fig.show()
