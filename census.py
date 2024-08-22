import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

census=pd.read_csv('census.csv')

census.head()

census.shape

census['age'].min()