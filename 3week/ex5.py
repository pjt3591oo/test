import pandas

df = pandas.read_csv('test.csv')
name = df['나이']
addr = df['주소']

n_df = pandas.concat([name, addr], axis=1)
print(n_df)
