##################################### Importing Bundeswertpapiere & Tidying Data #####################################

T = 10
file_path = "C:/Users/mauri/Desktop/Work/1) Current Employers/University of Tübingen (HIWI)/3) Liquidity Project/Liquidity_Project" 

##################################### Importing Packages #####################################
import pandas as pd 
import os #Used to change directory
from functools import reduce #Merge dataframes
import math #Perform mathematical tasks
from datetime import datetime #Add current time as suffix to exported data

#Changing Working Directory
os.chdir(file_path)

##################################### Importing & Tidying Data #####################################

svensson_bonds_parameter_path = "Raw_Data"
svensson_covered_parameter_path = "Raw_Data"

#Importing Federal Bonds
bonds_beta_0 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.B0.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 0
bonds_beta_1 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.B1.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 1
bonds_beta_2 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.B2.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 2
bonds_beta_3 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.B3.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 3
bonds_tau_1 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.T1.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Tau 1
bonds_tau_2 = pd.read_csv(f"{svensson_bonds_parameter_path}/BBSIS.D.I.ZST.T2.EUR.S1311.B.A604._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Tau 2

#Importing Covered Bonds
covered_beta_0 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.B0.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 0
covered_beta_1 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.B1.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 1
covered_beta_2 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.B2.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 2
covered_beta_3 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.B3.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Beta 3
covered_tau_1 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.T1.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Tau 1
covered_tau_2 = pd.read_csv(f"{svensson_covered_parameter_path}/BBSIS.D.I.ZST.T2.EUR.S122.B.A100._Z.R.A.A._Z._Z.A.csv", sep=";", skiprows=range(1, 10), na_values=".") #Importing Tau 2

parameter_dataframe_list = [[bonds_beta_0, bonds_beta_1, bonds_beta_2, bonds_beta_3, bonds_tau_1, bonds_tau_2], 
                            [covered_beta_0, covered_beta_1, covered_beta_2, covered_beta_3, covered_tau_1, covered_tau_2]]

for financial_instrument in parameter_dataframe_list:
    for parameter in financial_instrument:
        #Drop column 3
        parameter.drop(parameter.columns[2], axis=1, inplace=True)
    
        #Create Date Column
        parameter.rename(columns={parameter.columns[0]: "Date_Unformatted"}, inplace=True)
        parameter[["Year", "Month", "Day"]] = parameter['Date_Unformatted'].str.split('-', expand=True)
        parameter["Date"] = pd.to_datetime(parameter[["Year", "Month", "Day"]])
        
        #Rename parameter column
        parameter_column = parameter.columns[1].split(".")[4]
        parameter.rename(columns={parameter.columns[1]: parameter_column}, inplace=True)
        
        #Replace "," with "." in parameter column
        parameter[parameter_column] = parameter[parameter_column].str.replace(',', '.')
        
        #Change column type to float
        parameter[parameter_column] = parameter[parameter_column].astype(float)
        
        #Drop not needed columns
        parameter.drop(columns=["Date_Unformatted", "Year", "Month", "Day"], axis=1, inplace=True)
        
        parameter.dropna(subset=[f"{parameter_column}"], inplace=True)


#Function to merge Svensson Parameters & reorder columns
def mergeAndReoderDataFrames(financial_instrument_index):  
    merged_df  = reduce(lambda left, right: pd.merge(left, right, on='Date', how='outer'), parameter_dataframe_list[financial_instrument_index])
    merged_df = merged_df[["Date", "B0", "B1", "B2", "B3", "T1", "T2"]]
    
    merged_df.rename(columns={"B0": "Beta_0"}, inplace=True)
    merged_df.rename(columns={"B1": "Beta_1"}, inplace=True)
    merged_df.rename(columns={"B2": "Beta_2"}, inplace=True)
    merged_df.rename(columns={"B3": "Beta_3"}, inplace=True)
    merged_df.rename(columns={"T1": "Tau_1"}, inplace=True)
    merged_df.rename(columns={"T2": "Tau_2"}, inplace=True)
    
    return merged_df

#Merge Svensson Parameters & Reorder columns
federal_bonds = mergeAndReoderDataFrames(0)
covered_bonds = mergeAndReoderDataFrames(1)

##################################### Calculating Interest rates for different T #####################################

#Function to calculate interest rates in a table based on Svensson Parameters
def calculateInterestRates(dataset, maturity_T):
    for index, row in dataset.iterrows():
        for maturity in range(1, T + 1):
            beta_factor_0 = row["Beta_0"]
            beta_factor_1 = row["Beta_1"]
            beta_factor_2 = row["Beta_2"]
            beta_factor_3 = row["Beta_3"]
            tau_factor_1 = row["Tau_1"]
            tau_factor_2 = row["Tau_2"]
        
            x_1 = ((1-math.exp(-maturity/tau_factor_1))/(maturity/tau_factor_1))
            x_2 = ((1-math.exp(-maturity/tau_factor_1))/(maturity/tau_factor_1))-math.exp(-maturity/tau_factor_1)
            x_3 = ((1-math.exp(-maturity/tau_factor_2))/(maturity/tau_factor_2))-math.exp(-maturity/tau_factor_2)
            
            dataset.at[index, f"0_Y_{maturity}"] = (beta_factor_0 + beta_factor_1 * x_1 + beta_factor_2 * x_2 + beta_factor_3 * x_3)*100
    
#Calculate interest rates for federal bonds and covered bonds
calculateInterestRates(federal_bonds, T)
calculateInterestRates(covered_bonds, T)

##################################### Creating new Dataset that contains svensson Parameters #####################################

#Creating a new dataset with the svensson parameters to be exported as csv.
federal_bonds_svensson_parameters = federal_bonds[["Date", "Beta_0", "Beta_1", "Beta_2", "Beta_3", "Tau_1", "Tau_2"]]
covered_bonds_svensson_parameters = covered_bonds[["Date", "Beta_0", "Beta_1", "Beta_2", "Beta_3", "Tau_1", "Tau_2"]]

#Dropping the svensson parameters as they  are not needed.
federal_bonds.drop(columns=["Beta_0", "Beta_1", "Beta_2", "Beta_3", "Tau_1", "Tau_2"], axis=1, inplace=True)
covered_bonds.drop(columns=["Beta_0", "Beta_1", "Beta_2", "Beta_3", "Tau_1", "Tau_2"], axis=1, inplace=True)

##################################### Merging Data & Calculating Yield Spread #####################################

#List of columns to change names 
fed_bond_colmns = federal_bonds.columns[1:T + 1]
cov_bond_colmns = covered_bonds.columns[1:T + 1]

#Renaming columns so that we are able to identify federal and covered bonds
federal_bonds_interest_rates = federal_bonds.rename(columns={col: col + "_federal_bonds" for col in fed_bond_colmns})
covered_bonds_interest_rates = covered_bonds.rename(columns={col: col + "_covered_bonds" for col in cov_bond_colmns})

#Creating dataset yield_spread as merge between federal_bonds and covered_bonds. Inner join is used to only keep matching observations. 
yield_spread = pd.merge(federal_bonds_interest_rates, covered_bonds_interest_rates, on='Date', how='inner')

for maturity in range(1, T + 1):
    #Calculating yield spread for each maturity. 
    yield_spread[f"0_Y_{maturity}"] = yield_spread[f"0_Y_{maturity}_covered_bonds"] - yield_spread[f"0_Y_{maturity}_federal_bonds"]
    
    #Dropping interest rates as we only keep yield spread. 
    yield_spread.drop(columns=[f"0_Y_{maturity}_federal_bonds", f"0_Y_{maturity}_covered_bonds"], axis=1, inplace=True)
     
##################################### Exporting Data as CSV #####################################      
#Exporting resulting dataset as csv.

#Generate timestamp to add to data that is exported
#current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
current_datetime = datetime.now().strftime('%Y_%m_%d')

#Exporting Svensson Parameters
federal_bonds_svensson_parameters.to_csv(f"Clean_Data/ts_federal_bonds_svensson_parameters_{current_datetime}.csv", index=False)
covered_bonds_svensson_parameters.to_csv(f"Clean_Data/ts_covered_bonds_svensson_parameters_{current_datetime}.csv", index=False)

#Exporting Interest Rates and Yield Spreads
federal_bonds.to_csv(f"Clean_Data/ts_federal_bonds_{current_datetime}.csv", index=False)
covered_bonds.to_csv(f"Clean_Data/ts_covered_bonds_{current_datetime}.csv", index=False)
yield_spread.to_csv(f"Clean_Data/ts_yield_spread_{current_datetime}.csv", index=False)
