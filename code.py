# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns={'Total' : 'Total_Medals'}, inplace = True)
data.head(10)

#Code starts here



# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().index.tolist()[0]



# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index, inplace=True)

def top_ten(df = top_countries, col_name = 'Total_Summer'):
    country_list = []
    country_list = list(df.nlargest(10, col_name)['Country_Name'])
    return country_list

print(top_ten(col_name = 'Total_Summer'))    
print(top_countries.nlargest(10, 'Total_Summer')['Country_Name'])

top_10_summer = top_ten(col_name = 'Total_Summer')
top_10_winter = top_ten(col_name = 'Total_Winter')
top_10 = top_ten(col_name = 'Total_Medals')
print(top_10_summer, top_10_winter, top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)

#plot

plt.figure(figsize = (15,8))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.title("Summer_Event_top_10")
plt.xlabel("Countries")
plt.ylabel("# of Medals")


#winter

winter_df = data[data['Country_Name'].isin(top_10_winter)]

plt.figure(figsize = (15,8))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.title("Winter_Event_top_10")
plt.xlabel("Countries")
plt.ylabel("# of Medals")


#total

top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize = (15,8))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.title("Overall_Event_top_10")
plt.xlabel("Countries")
plt.ylabel("# of Medals")










# --------------
#Code starts here
#summer

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])

summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio, summer_country_gold)
#winter
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'])

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_max_ratio, winter_country_gold)


#overall
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_max_ratio, top_country_gold)









# --------------
#Code starts here


data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total']*1

most_points = max(data_1['Total_Points'])

best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']

print(best_country, most_points)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.reset_index(inplace=True, drop=True)
print(best)   


best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)

l=plt.legend()

l.get_texts()[0].set_text('Gold Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze Total :' + str(best['Bronze_Total'].values))


