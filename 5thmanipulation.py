# For the next set of questions, we will be using census data from the United States Census Bureau. Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. See this document for a description of the variable names.

#The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.

#Which state has the most counties in it? 
def answer_five():
    census_df = pd.read_csv('census.csv')
    i=census_df.groupby('STNAME').count().rename(columns={'SUMLEV':'NUMBEROFCOUNTIES'})['NUMBEROFCOUNTIES']
    value = i.max()
    l=i.argmax(value)
    return l