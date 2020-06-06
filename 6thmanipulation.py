#Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.

#This function should return a list of string values.
def answer_six():
    census_df = pd.read_csv('census.csv')
    g = census_df[['STNAME','CENSUS2010POP']]
    g = g.groupby('STNAME').sum()
    g=g.sort_values(by=['CENSUS2010POP'],ascending=False)
    l=list()
    l.append(g.index[0])
    l.append(g.index[1])
    l.append(g.index[2])
    return l