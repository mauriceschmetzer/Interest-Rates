##################################### Importing Packages #####################################
import pandas as pd  # Used for variety of tasks
import os  # Used to change & verify directory
import seaborn as sns  # Used to create lineplot
import matplotlib.pyplot as plt  # Used to edit plot
import numpy as np  # Used to set amount of ticks on x-axis
from datetime import datetime

##################################### Settings #####################################

# In the settings section, the following abreviations will be used:

# YS = Yield Spread
# FB = Federal Bonds
# CB = Covered Bonds

# CSV File suffix (Is part of csv file name)
YS_csv_suffix = "2023_12_25"
FB_csv_suffix = "2023_12_25"
CB_csv_suffix = "2023_12_25"

# Decide if you want to show the graphs
YS_show_graph = False
FB_show_graph = True
CB_show_graph = True

# Decide if you want to export graphs as png to figures folder
YS_export_png = True
FB_export_png = True
CB_export_png = True

# Set export name for graph
YS_export_name = "YS_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"
FB_export_name = "FB_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"
CB_export_name = "CB_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"

# Set the dates for which you would like to show the term structure
YS_date = ["2009-12-01", "2022-12-01", "2023-12-01", "2014-12-01"]
FB_date = ["2009-12-01", "2022-12-01", "2023-12-01", "2014-12-01"]
CB_date = ["2009-12-01", "2022-12-01", "2023-12-01", "2014-12-01"]

# Set list of maturities that you would like to show on the graph
# YS_maturity_list =  [1, 2, 3, 4, 5, 6, 7]
YS_maturity_list = list(range(1, 31))
# FB_maturity_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
FB_maturity_list = list(range(1, 31))
# CB_maturity_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
CB_maturity_list = list(range(1, 31))

# Set how many years you would like to see between two ticks on the x-axis
YS_show_every_nth_x_tick = 5
FB_show_every_nth_x_tick = 5
CB_show_every_nth_x_tick = 5

# Set x-axis label
YS_x_label = "Number of Years"
FB_x_label = "Number of Years"
CB_x_label = "Number of Years"

# Set y-axis label
YS_y_label = "Yield Spread [in bp]"
FB_y_label = "Interest Rate [in bp]"
CB_y_label = "Interest Rate [in bp]"

# Set graph title
YS_graph_title = "Yield Spread Term Structure"
FB_graph_title = "Government Bonds Term Structure"
CB_graph_title = "Covered Bonds Term Structure"

# Set legend title
YS_legend_title = "Date"
FB_legend_title = "Date"
CB_legend_title = "Date"

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
# Changing Working Directory
os.chdir(file_path)

##################################### Verifying Directory Exists #####################################
# Ensure that the "Figures" directory exists
figures_directory = "Figures"

if not os.path.exists(figures_directory):
    os.makedirs(figures_directory)

##################################### Importing Data #####################################

# Import Data
yield_spread = pd.read_csv(f"Clean_Data/ts_yield_spread_{YS_csv_suffix}.csv") # Importing Yield Spread Data
federal_bonds = pd.read_csv(f"Clean_Data/ts_federal_bonds_{FB_csv_suffix}.csv") # Importing Federal Bonds Data
covered_bonds = pd.read_csv(f"Clean_Data/ts_covered_bonds_{CB_csv_suffix}.csv") # Importing Covered Bonds Data

##################################### Selecting & Transposing Data #####################################

# First I subset & transpose the data to allow for easier visualization

def subsetData(showGraph, dataframe, date_list, maturity_list):
    if showGraph:

        # Keep only the requested date
        subsetted_data = dataframe[dataframe["Date"].isin(date_list)]

        # Get list of all columns in dataframe
        columns = subsetted_data.columns

        # Extracts the maturity from each column name and check if it's in the maturity list
        selected_columns = [col for col in columns if col.startswith('0_Y_') and int(col.split('_')[-1]) in maturity_list]

        # Includes all other columns too.
        selected_columns += [col for col in columns if not col.startswith('0_Y_')]

        # Subset the dataframe with the selected columns
        subsetted_data = subsetted_data[selected_columns]

        # Transposing wide to long format
        subsetted_data = pd.melt(subsetted_data, id_vars="Date", var_name="Maturity", value_name='Interest_Rate')

        # Keep only the year information in maturitiy columns
        subsetted_data["Maturity"] = subsetted_data['Maturity'].str.extract('_(\d+)$')

        # Convert "Maturity" column to integers
        subsetted_data["Maturity"] = subsetted_data["Maturity"].astype(int)

        # Return subsetted & transposed dataframe
        return subsetted_data


##################################### Visualizing Data #####################################

def createPlot(showGraph, dataframe, y_label, x_label, graph_title, legend_title, show_every_nth_tick, show_zero_line, source_text, export_graph, export_name):
    # Only show graph is this is wanted
    if showGraph:

        # Set the figure size and resolution
        plt.figure(figsize=(14, 6), dpi=300)

        # Plotting with Seaborn
        sns.set(style="ticks")  # Set the style of the plot

        # Creating a line plot for each date
        sns.lineplot(y="Interest_Rate", x="Maturity", hue= "Date", data=dataframe)

        # Adding labels and title
        plt.xlabel(x_label)  # X-Axis Label
        plt.ylabel(y_label)  # Y-Axis Label
        plt.title(graph_title)  # Title
        
        # Show the legend
        plt.legend(bbox_to_anchor=(1, 1), #Anchors legend outsite of graph
                   loc="upper left", 
                   title=legend_title, #Sets legend title
                   frameon=False) #Removes edge of legend box

        # Set x-axis ticks to every fifth number
        plt.xticks(np.arange(min(dataframe["Maturity"])-1, max(dataframe["Maturity"])+1, show_every_nth_tick))

        # Set the x-axis limits to start from the first value
        plt.xlim(dataframe["Maturity"].min(), dataframe["Maturity"].max())

        # Draw a horizontal line at y = 0
        if show_zero_line:
            plt.axhline(y=0, color='black', linestyle='--', linewidth=1)

        # Set text for source of data
        plt.gcf().text(0.2, 0.02, source_text, ha="center")

        # Save the plot
        if export_graph:
            plt.savefig(os.path.join(figures_directory, export_name))

        # Show the plot
        plt.show()

##################################### Executing functions #####################################

# Subsetting & transposing data
ys_subsetted = subsetData(YS_show_graph, yield_spread, YS_date, YS_maturity_list)
fb_subsetted = subsetData(FB_show_graph, federal_bonds, FB_date, FB_maturity_list)
cb_subsetted = subsetData(CB_show_graph, covered_bonds, CB_date, CB_maturity_list)

# Creating & exporting plots
createPlot(YS_show_graph, ys_subsetted, YS_y_label, YS_x_label, YS_graph_title, YS_legend_title, YS_show_every_nth_x_tick, YS_show_zero_line, YS_source_text, YS_export_png, YS_export_name)
createPlot(FB_show_graph, fb_subsetted, FB_y_label, FB_x_label, FB_graph_title, FB_legend_title, FB_show_every_nth_x_tick, FB_show_zero_line, FB_source_text, FB_export_png, FB_export_name)
createPlot(CB_show_graph, cb_subsetted, CB_y_label, CB_x_label, CB_graph_title, CB_legend_title, CB_show_every_nth_x_tick, CB_show_zero_line, CB_source_text, CB_export_png, CB_export_name)
