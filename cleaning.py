import pandas as pd 
import numpy as np 




##load the confirmatory dataframes
df_names = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/NDC_drug_categories/ndc_map-master/FDA NDC Database File with ATC4/2018_03_27 13_09 atc4_name.csv")
df_ndc = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/NDC_drug_categories/ndc_map-master/FDA NDC Database File with ATC4/2018_03_27 13_09 year_month_ndc_atc4.csv")
df_all = pd.read_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/NDC_drug_categories/ndc_map-master/FDA NDC Database File with ATC4/2018_03_27 13_09 ndc_rxcui_atc4.csv", encoding = "ISO-8859-1")

df_ndc_2 = df_ndc
df_ndc_2 = df_ndc_2.drop(columns=['YEAR','MONTH'])
df_ndc_2['NDC'] = df_ndc_2['NDC'].replace({'-': ''}, regex=True)
df_ndc_2['NDC'] = df_ndc_2['NDC'].astype(int)
df_ndc_2 = df_ndc_2.merge(df_names, how='left', on='ATC4')


final = df_ndc_2


final.to_csv("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/NDC_drug_categories/output/ndc_categories.csv")
final.to_pickle("/Users/hantswilliams/Dropbox/Biovirtua/Python_Projects/NDC_drug_categories/output/ndc_categories.pkl")