import pandas

data = {
  "9746000": ["0.1", "0.2", "0.3", "0.1"],
  "9747000": ["0.1", "0.2", "0.3", "0.1"],
  "9748000": ["0.1", "0.2", "0.3", "0.1"],
  "9749000": ["0.1", "0.2", "0.3", "0.1"],
  "9750000": ["0.1", "0.2", "0.3", "0.4"]
}

df = pandas.DataFrame(data, index=data['9750000'])
# df.to_csv('result.csv')
# print(df)

  # print(df.loc['0.1'])
  # print(df.iloc[2])

a = df.groupby(df['9750000'])
print(df.corr())