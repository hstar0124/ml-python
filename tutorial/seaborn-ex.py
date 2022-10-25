import seaborn as sns
import pandas as pd

col_id = pd.Series(data=[5, 14, 21, 25])
col_team = pd.Series(data=['A', 'A', 'B', 'B'])
col_name = pd.Series(data=['김패캠', '정코딩', '박데사', '장머신'])
col_score = pd.Series(data=[100, 95, 60, 80])

df = pd.DataFrame(data={'Id': col_id,
                        'Team': col_team,
                        'Name': col_name,
                        'Score': col_score})
df.set_index('Id', inplace=True)

sns.histplot(x='Score', data=df, hue='Team')


sns.boxplot(y='Score', x='Team', data=df)