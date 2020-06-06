# a function that creates a Series called "Points" which is a weighted value where each gold medal (`Gold.2`) counts for 3 points, silver medals (`Silver.2`) for 2 points, and bronze medals (`Bronze.2`) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.

#*This function should return a Series named `Points` of length 146*
def answer_four():
    df = df.assign(total = df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2'])
    Points = pd.Series(df['total'],index=df.index)
    return Points
   