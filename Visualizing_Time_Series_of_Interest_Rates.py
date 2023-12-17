##################################### Importing Packages #####################################
import pandas as pd  #Used for variety of tasks
import os #Used to change & verify directory
import seaborn as sns #Used to create lineplot
import matplotlib.pyplot as plt #Used to edit plot
from datetime import datetime

##################################### Settings #####################################

#In the settings section, the following abreviations will be used:
    
    # YS = Yield Spread
    # FB = Federal Bonds
    # CB = Covered Bonds
    
# CSV File suffix (Is part of csv file name)
YS_csv_suffix = "2023_12_17"
FB_csv_suffix = "2023_12_17"
CB_csv_suffix = "2023_12_17"    

# Decide if you want to show the graphs
YS_show_graph = True
FB_show_graph = True
CB_show_graph = True

# Decide if you want to export graphs as png to figures folder
YS_export_png = True
FB_export_png = True
CB_export_png = True

#Set export name for graph
YS_export_name = "YS_" + datetime.today().strftime('%Y_%m_%d') + ".png"
FB_export_name = "FB_" + datetime.today().strftime('%Y_%m_%d') + ".png"
CB_export_name = "CB_" + datetime.today().strftime('%Y_%m_%d') + ".png"

# Start date on graph
YS_start_date = "2009-01-01"
FB_start_date = "2009-01-01"
CB_start_date = "2009-01-01"

# End date on graph
YS_end_date = "2022-01-30"
FB_end_date = "2022-01-30"
CB_end_date = "2022-01-30"

# Set list of maturities that you would like to show on the graph
YS_maturity_list =  [1, 5, 10]
FB_maturity_list =  [1, 5, 10]
CB_maturity_list =  [1, 5, 10]

# Set amount of ticks shown on x-axis
YS_amount_x_ticks = 20
FB_amount_x_ticks = 20
CB_amount_x_ticks = 20

# Set x-axis label
YS_x_label = ""
FB_x_label = ""
CB_x_label = ""

# Set y-axis label
YS_y_label = "Yield Spread [in bp]"
FB_y_label = "Interest Rate [in bp]"
CB_y_label = "Interest Rate [in bp]"

# Set graph title
YS_graph_title = "Yield Spread between Covered Bonds & Gov. Bonds"
FB_graph_title = "German Government Bonds Interest Rates"
CB_graph_title = "Covered Bonds Interest Rates"

# Set legend title
YS_legend_title = "Maturity"
FB_legend_title = "Maturity"
CB_legend_title = "Maturity"

# Decide if you want to show zero line in graph
YS_show_zero_line = False
FB_show_zero_line = True
CB_show_zero_line = True

# Set source of data
YS_source_text = "Source: Svensson Parameter Bundesbank"
FB_source_text = "Source: Svensson Parameter Bundesbank"
CB_source_text = "Source: Svensson Parameter Bundesbank"

file_path = "C:/Users/mauri/Desktop/Work/1) Current Employers/University of Tübingen (HIWI)/3) Liquidity Project/Liquidity_Project"

##################################### Changing Working Directory #####################################
#Changing Working Directory
os.chdir(file_path)

##################################### Verifying Directory Exists #####################################
# Ensure that the "Figures" directory exists
figures_directory = "Figures"

if not os.path.exists(figures_directory):
    os.makedirs(figures_directory)
    
##################################### Importing Data #####################################

#Import Data
yield_spread = pd.read_csv(f"Clean_Data/ts_yield_spread_{YS_csv_suffix}.csv") #Importing Federal Bonds Data
federal_bonds = pd.read_csv(f"Clean_Data/ts_federal_bonds_{FB_csv_suffix}.csv") #Importing Federal Bonds Data
covered_bonds = pd.read_csv(f"Clean_Data/ts_covered_bonds_{CB_csv_suffix}.csv") #Importing Federal Bonds Data

##################################### Visualizing Data #####################################

def createPlot(showGraph, dataframe, start_date, end_date, maturity_list, y_label, x_label, graph_title, legend_title, number_of_x_ticks, show_zero_line, source_text, export_graph, export_name):
    #Only show graph is this is wanted
    if showGraph:
        
        subsetted_data = dataframe[dataframe["Date"] >= start_date]
        subsetted_data = subsetted_data[subsetted_data["Date"] <= end_date]
        
        # Set the figure size and resolution
        plt.figure(figsize=(10, 6), dpi=300)
        
        # Plotting with Seaborn
        sns.set(style="ticks")  # Set the style of the plot
        
        # Creating a line plot
        for maturity in maturity_list:
            sns.lineplot(y=f"0_Y_{maturity}", x="Date", data=subsetted_data, label=f"{maturity}y")
        
        # Adding labels and title
        plt.xlabel(x_label) # X-Axis Label
        plt.ylabel(y_label) # Y-Axis Label
        plt.title(graph_title) # Title
        
        # Show the legend
        plt.legend(bbox_to_anchor=(1, 1), #Anchors legend outsite of graph
                   loc="upper left", 
                   title=legend_title, #Sets legend title
                   frameon=False) #Removes edge of legend box
      
        x_ticks = subsetted_data["Date"].unique()[::len(subsetted_data["Date"].unique()) // number_of_x_ticks]
        plt.xticks(x_ticks, [date.strftime('%m/%Y') for date in pd.to_datetime(x_ticks)])
        
        # Set the x-axis limits to start from the first value
        plt.xlim(subsetted_data["Date"].min(), subsetted_data["Date"].max())
        
        # Draw a horizontal line at y = 0
        if show_zero_line:
            plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
        
        # Rotate x-axis labels for better visibility
        plt.gcf().autofmt_xdate()
        
        #Set text for source of data
        plt.gcf().text(0.2, 0.02, source_text, ha="center")
        
        # Save the plot
        if export_graph:
            plt.savefig(os.path.join(figures_directory, export_name))
    
        # Show the plot
        plt.show()

createPlot(YS_show_graph, yield_spread, YS_start_date, YS_end_date, YS_maturity_list, YS_y_label, YS_x_label, YS_graph_title, YS_legend_title, YS_amount_x_ticks, YS_show_zero_line, YS_source_text, YS_export_png, YS_export_name) 
createPlot(FB_show_graph, federal_bonds, FB_start_date, FB_end_date, FB_maturity_list, FB_y_label, FB_x_label, FB_graph_title, FB_legend_title, FB_amount_x_ticks, FB_show_zero_line, FB_source_text, FB_export_png, FB_export_name) 
createPlot(CB_show_graph, covered_bonds, CB_start_date, CB_end_date, CB_maturity_list, CB_y_label, CB_x_label, CB_graph_title, CB_legend_title, CB_amount_x_ticks, CB_show_zero_line, CB_source_text, CB_export_png, CB_export_name) 

