import pandas

# Load dataset
dataframe = pandas.read_csv("emobank.csv")

# take a look at the dataset
print(' === Min === ')
print(dataframe[['V', 'A', 'D']].min())
print(' === Max === ')
print(dataframe[['V', 'A', 'D']].max())
print(dataframe.describe())
print(dataframe.sort_values('V', ascending=False).head(3))
print(dataframe.sort_values('A', ascending=False).head(3))
print(dataframe.sort_values('D', ascending=False).head(3))