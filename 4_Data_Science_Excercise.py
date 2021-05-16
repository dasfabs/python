#Do the following exercise in a Jupyter Notebook (a GitHub Link would be the best):
import pandas as pd
url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'
df = pd.read_csv (url,error_bad_lines=False)

row_count, column_count = df.shape
print('Basic informations')
print("Number of rows ", row_count)
print("Number of columns ", column_count)
print('')
print('---------------------------------------')
print('Show the last 4 rows of the data frame.')
df1 = df.iloc[1:]
print(df1)
print('')
print('---------------------------------------')
print('Show all the row of countries who have the EURO.')
df2 = df.loc[df['Currency'] == 'EUR']
print(df2)
print('')
print('---------------------------------------')
print('Show only name and Currency in a new data frame.')
df3 = df[['Name', 'Currency']]
print(df3)
print('')
print('---------------------------------------')
print('Show only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)')
df4 = df.loc[df['BIP'] > 2000]
print(df4)
print('')
print('---------------------------------------')
print('Select all countries where with inhabitants between 50 and 150 Mio')
df5 = df.loc[(df['People'] >= 50000000) & (df['People'] <= 150000000)]
print(df5)
print('')
print('---------------------------------------')
print('Change BIP to Bip')
df6 = df.rename({'BIP' : 'Bip'}, axis=1)
print(df6)
print('')
print('---------------------------------------')
print('Calculate the Bip sum')
sum1 = df6['Bip'].sum()
print('Total Bip: ' + str(sum1))
print('')
print('---------------------------------------')
print('Calculate the average people of all countries')
sum2 = df['People'].sum()/row_count
print('Avrg People: ' + str(round(sum2)))
print('')
print('---------------------------------------')
print('Sort by name alphabetically')
df7 = df.sort_values(by=['Name'])
print(df7)
print('')
print('---------------------------------------')
print('Create a new data frame from the original where the area is changed as follows: all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced')
df8 = df
df8['Area'] = np.where(df8['Area'] > 1000000, 'BIG', 'SMALL')
print(df8)
