import pandas as pd
fname = '/Users/arnoldas/Desktop/DailyTemps-Albany.csv'
df = pd.read_csv(fname,parse_dates=[0])
df
df.head()
(df['EDT'] >= '2018-06-01') & (df['EDT'] < '2018-07-01')
june = (df['EDT'] >= '2018-06-01') & (df['EDT'] < '2018-07-01')
june_df = df.loc[is_june2018, :]
june_df = df.loc[june, :]
june_df
import matplotlib
figsize(10,10)
import matplotlib as plt
plt.figsize(10,10)
plt.plot(june_df,label="factorial"))
plt.plot(june_df,label="factorial")
import matplotlib.pyplot as plt
plt.plot(june_df,label="factorial")
plt.show()
plt.plot(june_df[0],label="date")
plt.plot(june_df['EDT'],label="date")
plt.show()
plt.plot(june_df['Max TemperatureF'],label="Max TemperatureF")
plt.show()
plt.plot(june_df['EDT'],label="date")
plt.plot(june_df['Max TemperatureF'],label="Max TemperatureF")
plt.show()
plt.plot(june_df['Max TemperatureF'],label="Max TemperatureF")
plt.plot(june_df['Min TemperatureF'],label="Min TemperatureF")
plt.show()
plt.plot(june['Max TemperatureF'],label="Max TemperatureF")
df.mean()
plt.plot(df['Max TemperatureF'],label="Max TemperatureF")
plt.show()
df['Max TemperatureF'].min()
plt.plot(df['Max TemperatureF'],label="Max TemperatureF")
plt.show()
plt.plot(df['Max TemperatureF']>-10,label="Max TemperatureF")
plt.show()
ylim(ymin=-10)
plt.ylim(ymin=-10)
plt.ylim(ymax=110)
plt.plot(df['Max TemperatureF']>-10,label="Max TemperatureF")
plt.show()
plt.ylim(ymin=-10)
plt.ylim(ymax=110)
plt.plot(df['Max TemperatureF'],label="Max TemperatureF")
plt.show()
