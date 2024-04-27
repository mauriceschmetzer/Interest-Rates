##################################### Settings #####################################
    
# Determine what date the bond was listed & on what date the bond matures. 
# Format YYYY-MM-DD
Start_Date = "2022-01-01"
End_Date = "2024-03-28"

#Set file Path
file_path = "C:/Users/mauri/Desktop/Work/1) Current Employers/University of Tübingen (HIWI)/Department of Finance/3) Liquidity Project/Liquidity_Project" 
#file_path = r'C:\Users\Tobias\OneDrive - UT Cloud\02 Forschung\06 Asset Allocation\hiwis\Interest-Rates'

#This is a path starting from the location of "file_path".
folder_path = "Clean_Data/"

# CSV File name for the svensson parameters
svensson_parameter_file_name = "ts_federal_bonds_svensson_parameters_2024_04_26.csv"

# Set the prefix value of the file that is exported.
export_file_name_prefix = "ts_federal_bond_price_"

##################################### Importing Packages #####################################
import pandas as pd 
import os #Used to change directory
import numpy as np #Used to calculate Interest Rates
from datetime import datetime #Add current time as suffix to exported data

##################################### Changing Working Directory #####################################
#Changing Working Directory
os.chdir(file_path)

##################################### Verifying Directory Exists #####################################
# Ensure that the "Figures" directory exists
output_directory = "Clean_Data"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
##################################### Importing & Tidying Data #####################################

svensson_parameters = pd.read_csv(f"{folder_path}{svensson_parameter_file_name}") # Importing Federal Bonds Data (Frist y-axis)
svensson_parameters["Date"] = pd.to_datetime(svensson_parameters["Date"])

##################################### Creating Dataframe based on Dates #####################################

Start_Date = pd.to_datetime(Start_Date)
End_Date = pd.to_datetime(End_Date)

# Generate range of dates between start and end dates (inclusive)
date_range = pd.date_range(start=Start_Date, end=End_Date)

# Create dataframe bond_price with date range
bond_price = pd.DataFrame(date_range, columns=["Date"])

#Sets End_Date column equal to the variable "End_Date" to be used to calculate Days_to_Maturity
bond_price["End_Date"] = End_Date

#Calculates Days to Maturity as difference between End_Date and current Date
bond_price["Days_to_Maturity"] = (bond_price["End_Date"] - bond_price["Date"]).dt.days

#Calculates Time to Maturity as Days to Maturity divided by 365 days.
bond_price["Time_to_Maturity"] = bond_price["Days_to_Maturity"] / 365

#Merges days with svensson parameters to calculate interest rate for each day
bond_price = pd.merge(bond_price, svensson_parameters, how = "left", on = "Date")

#Removes any days for which there are no svensson parameters (Weekends / Holidays)
bond_price.dropna(inplace=True)

#Calculates factors x1, x2, x3 for calculating interest rates
bond_price["x1"] = ((1-np.exp(-bond_price["Time_to_Maturity"]/bond_price["Tau_1"]))/(bond_price["Time_to_Maturity"]/bond_price["Tau_1"]))
bond_price["x2"] = ((1-np.exp(-bond_price["Time_to_Maturity"]/bond_price["Tau_1"]))/(bond_price["Time_to_Maturity"]/bond_price["Tau_1"]))-np.exp(-bond_price["Time_to_Maturity"]/bond_price["Tau_1"])
bond_price["x3"] = ((1-np.exp(-bond_price["Time_to_Maturity"]/bond_price["Tau_2"]))/(bond_price["Time_to_Maturity"]/bond_price["Tau_2"]))-np.exp(-bond_price["Time_to_Maturity"]/bond_price["Tau_2"])

#Calculates interest rates as yield to maturity using the svensson formula.
bond_price["Yield_to_Maturity"] = (bond_price["Beta_0"] + bond_price["Beta_1"] * bond_price["x1"] + bond_price["Beta_2"] * bond_price["x2"] + bond_price["Beta_3"] * bond_price["x3"])/100

#Calculates the bond price as face value 1 discounted to today using the yield to maturity and time to maturity. 
bond_price["Bond_Price"] = np.exp(-bond_price["Yield_to_Maturity"]*bond_price["Time_to_Maturity"])


columns_to_drop = ["Beta_0", "Beta_1", "Beta_2", "Beta_3", "Tau_1", "Tau_2", "x1", "x2", "x3", "End_Date"]

bond_price.drop(columns=columns_to_drop, inplace=True)

##################################### Exporting Data as CSV #####################################      
#Exporting resulting dataset as csv.

#Generate timestamp to add to data that is exported
#current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
current_datetime = datetime.now().strftime('%Y_%m_%d')

#Exports the bond prices as csv.
bond_price.to_csv(os.path.join(output_directory, f"{export_file_name_prefix}{current_datetime}.csv"), index=False)
        