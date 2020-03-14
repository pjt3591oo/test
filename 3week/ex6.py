import pandas

df = pandas.read_csv('test.csv')

# print(df[df['나이'] > 21])
print(df[df['나이'].notnull()])