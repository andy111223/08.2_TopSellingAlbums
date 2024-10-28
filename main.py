import pandas as pd

tables_list = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/',header=0)

df = pd.DataFrame(tables_list[0], columns=['TITLE','ARTIST','YEAR','HIGH POSN'])
print(df[:10])
print(df.info()) 

# 1
df.rename(columns={
    'TITLE':'TYTUŁ',
    'ARTIST':'ARTYSTA',
    'YEAR':'ROK',
    'HIGH POSN':'MAX POZ'
}, inplace=True)

# 2
unique_artists = df['ARTYSTA'].nunique()
print('Unique artists count: ', unique_artists)
# 3
max_artists = df['ARTYSTA'].value_counts()
print('Most frequent artists:\n', max_artists[:3])
# 4
df.rename(str.capitalize, axis='columns',inplace=True)
# 5
df.drop('Max poz',axis=1,inplace=True)
print(df)
# 6
year_max_albums = df['Rok'].value_counts()
print('Year with most titles:\n', year_max_albums[:2])
# 7
albums_between = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].count()
print("Number of albums between 1960-1990: ",albums_between[1])
# 8 
year_descening = df.sort_values(by='Rok',ascending=False)
print("The youngest album:\n",year_descening.iloc[0])
# 9
earliest_albums = df.groupby(pd.Grouper(key='Artysta')).agg({
    'Rok':'min'
})
print(earliest_albums)
# 10
df.to_csv('list.csv')