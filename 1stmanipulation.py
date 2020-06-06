#Which country has won the most gold medals in summer games?
def answer_one():
         save=0
         dfcp = df['Gold']==df['Gold'].max()
         for i in range(len (dfcp)):
             if dfcp[i]==True : save = i
         return dfcp.index[save]