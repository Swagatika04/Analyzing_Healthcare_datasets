import numpy as np
import pandas as pd

#Read the asthma data file
df= pd.read_csv("~//Desktop/asthma.csv")

#Numerator column is a string column , so first commas are removed and then converted to a float column
df["Numerator"]=df["Numerator"].str.replace(',', '').astype(float)

########   Part A-1

# 2 dataframes created based with filters on year(2012 and 2015), age group (all ages) and strata name (only women).
df_filtered_2012= df[(df["Strata Name"]=="Female") & (df["Year"]==2012) & (df["Age Group"]=="All Ages")].reset_index(drop=True)
df_filtered_2015= df[(df["Strata Name"]=="Female") & (df["Year"]==2015) & (df["Age Group"]=="All Ages")].reset_index(drop=True)

#All unnecesary columns deleted so that duplicate columns not formed during merging
df_filtered_2012_final=df_filtered_2012.drop(columns=['Year', 'Age Group', "Strata", "Strata Name", "Numerator"])
df_filtered_2015_final=df_filtered_2015.drop(columns=['Year', 'Age Group', "Strata", "Strata Name", "Numerator"])

#Two dataframes, one for 2012 and another for 2015 merged on Geography column
df_merged= pd.merge(df_filtered_2012_final,df_filtered_2015_final, on="Geography" )

#Percentage change in rate is calculated
df_merged["rate_percent_change"]= (df_merged['Percent_y'] - df_merged['Percent_x']) / (df_merged['Percent_x']) *100

#The values are sorted by percentage change in rate and top 5 countries are selected
df_merged_top_five=df_merged.sort_values(by=['rate_percent_change'], ascending=False).head(5).reset_index(drop=True)


########   Part A-2

#Dataframe filtered for 2015 to make it ready to calculate population for each county
df_total= df[(df["Strata"]=="Total Population")& (df["Year"]==2015) & (df["Age Group"]=="All Ages")].reset_index(drop=True)

#Population calculated by dividing numerator by percent10000 column
df_total["Population"]=df_total["Numerator"]*10000/(df_total["Percent"])

#A new column called category created to see if a county is a large one or small based on population
df_total["Category"] = np.where(df_total["Population"] >=400000, 'Large', 'Small')

#All unnecesary columns deleted so that duplicate columns not formed during merging
df_total=df_total.drop(columns=['Year', 'Age Group', "Strata", "Strata Name", "Percent", "Numerator", "Population"])

#Dataframes merged so that we get category column
df_merged_category= pd.merge(df, df_total, on = "Geography")

#Merged dataframe filtered so that we have data as desired
df_merged_category_filtered= df_merged_category[(df_merged_category["Strata"]=="Sex") & (df_merged_category["Age Group"]=="All Ages")].reset_index(drop=True)
df_final_sorted=df_merged_category_filtered.sort_values(by=["Geography",'Year', 'Strata Name', "Category"]).drop(columns=['Age Group',"Strata", "Numerator"]).reset_index(drop=True)
