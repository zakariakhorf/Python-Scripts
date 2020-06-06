#Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
def answer_three():
    dfs=df.drop(df.index[df['Gold.1']<1])
    dfs=dfs.drop(dfs.index[dfs['Gold']<1])
    dfs = dfs.assign(Val10_minus_Val1 = abs(df['Gold'] - df['Gold.1']))
    dfs['division']=dfs['Val10_minus_Val1'] / dfs['Gold.2']
    save=dfs.index[dfs['division']==dfs['division'].max()][0]
    return save

   