#In this datafile, the United States is broken up into four regions using the "REGION" column.

#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.

#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():  
    census_df = pd.read_csv('census.csv')
    f = census_df[census_df['REGION'] < 3]
    f = f[f['CTYNAME'].str.startswith('Washington', na=False)]
    f = f[f['POPESTIMATE2015'] > f['POPESTIMATE2014']]
    f = f[ ['STNAME', 'CTYNAME']]
    return f