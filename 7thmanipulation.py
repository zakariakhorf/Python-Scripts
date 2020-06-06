#Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
def answer_seven():
    gr = census_df[['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    gr=gr.set_index('CTYNAME')
    gr['min']=gr.min(axis = 1)
    gr['max']=gr.max(axis = 1)
    gr['diff']=abs(gr['min']-gr['max'])
    g= gr[gr['diff']==gr['diff'].max()].index[0]
    return g