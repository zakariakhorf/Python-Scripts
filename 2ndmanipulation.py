#Which country had the biggest difference between their summer and winter gold medal counts
def answer_two():
        df = df.assign(Val10_minus_Val1 = abs(df['Gold'] - df['Gold.1']))
        save=df['Val10_minus_Val1'].max()
        return df.index[df['Val10_minus_Val1']==save][0]
   