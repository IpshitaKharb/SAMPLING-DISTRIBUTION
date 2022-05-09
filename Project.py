import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
fig=ff.create_distplot([data],['reading_time'],show_hist=False)
fig.show()

def randg (counter):
    dataset=[]
    for i in range (0,counter):
        randIndex=random.randint(0,len(data)-1)
        value=data[randIndex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list): 
    df = mean_list 
    mean = statistics.mean(df) 
    fig = ff.create_distplot([df], ["temp"], show_hist=False) 
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN")) 
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        meanpeople=randg(100)
        mean_list.append(meanpeople)
    show_fig(mean_list)
    meansample=statistics.mean(mean_list)
    print('meansample',meansample)

    std_deviation = statistics.stdev(mean_list) 
    print("Standard deviation of sampling distribution:- ", std_deviation)

setup()

population_mean = statistics.mean(data) 
population_sd=statistics.stdev(data) 
print("population mean:- ", population_mean) 
print("std dev",population_sd)
