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
    # SY = Second Y-Axis Data (Here as an Example: VDAX)
    
### 1) Settings - 1st Y-Axis
    
# CSV File name

YS_file_name = "ts_yield_spread_2024_04_26.csv"
FB_file_name = "ts_federal_bonds_2024_04_26.csv"
CB_file_name = "ts_covered_bonds_2024_04_26.csv"

# Decide if you want to show the graphs
YS_show_graph = True
FB_show_graph = True
CB_show_graph = True

# Decide if you want to export graphs as png to figures folder
YS_export_png = True
FB_export_png = True
CB_export_png = True

# Graph resolution in dpi
YS_graph_resolution = 1000
FB_graph_resolution = 1000
CB_graph_resolution = 1000

# Set export name for graph
YS_export_name = "YS_Time_Series_" + datetime.today().strftime('%Y_%m_%d') + ".png"
FB_export_name = "FB_Time_Series_" + datetime.today().strftime('%Y_%m_%d') + ".png"
CB_export_name = "CB_Time_Series_" + datetime.today().strftime('%Y_%m_%d') + ".png"

# Start date on graph
YS_start_date = "2009-01-01"
FB_start_date = "2009-01-01"
CB_start_date = "2009-01-01"

# End date on graph
YS_end_date = "2024-04-19"
FB_end_date = "2024-04-19"
CB_end_date = "2024-04-19"

# Set list of maturities that you would like to show on the graph (first y-axis)
YS_maturity_list =  [1]
FB_maturity_list =  [1, 5, 10]
CB_maturity_list =  [1, 5, 10]

# Set column name for data for x-axis
YS_x = "Date"
FB_x = "Date"
CB_x = "Date"

# Set amount of ticks shown on x-axis
YS_amount_x_ticks = 20
FB_amount_x_ticks = 20
CB_amount_x_ticks = 20

# Set x-axis label
YS_x_label = ""
FB_x_label = ""
CB_x_label = ""

# Set first y-axis label
YS_y_label = "Yield Spread [in bp]"
FB_y_label = "Interest Rate [in bp]"
CB_y_label = "Interest Rate [in bp]"

# Set graph title
YS_graph_title = "Yield Spread between Covered Bonds & Gov. Bonds compared to VDAX"
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

# Set file path for main folder of data for first y-axis
file_path = "C:/Users/mauri/Desktop/Work/1) Current Employers/University of Tübingen (HIWI)/Department of Finance/3) Liquidity Project/Liquidity_Project" 
#file_path = r'C:\Users\Tobias\OneDrive - UT Cloud\02 Forschung\06 Asset Allocation\hiwis\Interest-Rates'

#Set folder path for data to be imported for first y-axis.
#This is a path starting from the location of "file_path".
FY_folder_path = "Clean_Data/"

### 2) Settings - 2nd Y-Axis

SY_show_on_graph = True # Decide if you want to add a second y-axis
SY_folder_path = "Clean_data/" # Set file path for values on second y-axis
SY_file_name = "VDAX.csv" #Set file name for values on the second y-axis
SY_y = "Price" #Set column name for data for the second y-axis
SY_x = "Date" #Set column name for data for the x-axis
SY_y_label = "VDAX" #Set second y-axis label
SY_legend_label = "VDAX" #Set the label that is shown in the legend on the right


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
yield_spread = pd.read_csv(f"{FY_folder_path}{YS_file_name}") # Importing Yield Spread Data (Frist y-axis)
federal_bonds = pd.read_csv(f"{FY_folder_path}{FB_file_name}") # Importing Federal Bonds Data (Frist y-axis)
covered_bonds = pd.read_csv(f"{FY_folder_path}{CB_file_name}") # Importing Covered Bonds Data (Frist y-axis)

if SY_show_on_graph:
    second_y_axis_data = pd.read_csv(f"{FY_folder_path}{SY_file_name}") # Importing Data for second y-axis 
else:
    second_y_axis_data = pd.DataFrame() #Empty dataframe
    
##################################### Visualizing Data #####################################

# First Y-Axis = Left Y-Axis
# Second Y-Axis = Right Y-Axis

def createPlot(showGraph, #Boolean indicating if you want to generate & show a graph
               sy_show_graph, #Boolean indicating if you want to show values on the second y-axis
               
               graph_resolution, #Resoltion for graph
               
               data_fy_axis, #Data for first y-axis (left)
               data_sy_axis, #Data for second y-axis (right) -> Add empty dataframe if no 2nd y-axis needed
               
               start_date, #Start date for x-axis
               end_date, #End date for x-axis
               
               maturity_list, #List of column names of y-axis in dataframe for first y-axis
               sy_y_value, #Column name of y-axis in dataframe for second y-axis
               
               fy_x_value, #Column name of x-axis in dataframe for first y-axis
               sy_x_value, #Column name of x-axis in dataframe for second y-axis
               
               fy_y_label, #Label for first y-axis 
               sy_y_label, #Label for second y-axis
               x_label, #Label for x-axis
               sy_label_legend, #Legend label for second y-axis values shown in legend.
               
               graph_title, #Title of graph
               legend_title,  #Title of legend
               
               number_of_x_ticks, #Number of ticks shown on x-axis
               show_zero_line, #Boolean indicating if you want to see a line indicating the zero line on the left y-axis
               source_text,  #Text for source of Data shown below the graph
               export_graph, #Boolean indicating if graph should be exported as png. 
               export_name): #Name of graph being exported (if export_graph = true)

    #Only show graph if this is wanted
    if showGraph:
        
        ######## DATA ########
        subsetted_fy_data = data_fy_axis[data_fy_axis["Date"] >= start_date]
        subsetted_fy_data = subsetted_fy_data[subsetted_fy_data["Date"] <= end_date]
        
        if sy_show_graph:
            subsetted_sy_data = data_sy_axis[data_sy_axis["Date"] >= start_date]
            subsetted_sy_data = subsetted_sy_data[subsetted_sy_data["Date"] <= end_date]
        
        ######## Figure Size & Resolution ########
        
        # Set the figure size and resolution
        plt.figure(figsize=(10, 6), dpi=graph_resolution)
        
        # Plotting with Seaborn
        sns.set(style="ticks")  # Set the style of the plot
        
        ######## Y - Axis ########
        
        ax1 = plt.gca()  # Gets the left y-axis
        
        if sy_show_graph:
            ax2 = plt.gca().twinx()  # Creates a second y-axis (right y-axis) sharing the same x-axis
        
        # Generates colorblind color palette with enough colors for each maturity + 1 for values on second y-axis
        color_palette = sns.color_palette("colorblind", len(maturity_list) + 1)
                
        ######## Line - Plots ########
        
        #In order to be able to show both y-axis legends on the same legend table, we create:
        lines = [] # A list with the line plots 
        labels = [] # A list with the labels of the line okits
        
        #Creates a line plot for each maturity.
        for i, maturity in enumerate(maturity_list):
            #Placed on first y-axis (left). The colors are taken from the above created color palette. 
            line = sns.lineplot(y=f"0_Y_{maturity}", x=fy_x_value, data=subsetted_fy_data, color=color_palette[i], ax=ax1)
                 
            lines.append(line.lines[i]) #Adds the current line plot to the list of line plots
            labels.append(f"{maturity}y") #Adds the label of the current line plot to the list of labels
    
        #Creates a lineplot for the data on the second y-axis (right). Uses -1 to get the color from the above created color palette
        
        if sy_show_graph:
            line = sns.lineplot(y=sy_y_value, x=sy_x_value, data=subsetted_sy_data, color=color_palette[-1], ax=ax2)
            
            lines.append(line.lines[0]) #Adds the current line plot to the list of line plots
            labels.append(sy_label_legend) #Adds the label of the current line plot to the list of labels
        
        ######## Labels, Title, Legend ########
        
        # Adding labels and title
        plt.xlabel(x_label) # X-Axis Label
        
        ax1.set_ylabel(fy_y_label) # Y-Axis (Left) Label
        if sy_show_graph:
            ax2.set_ylabel(sy_y_label) # Y-Axis (Right) Label
        
        plt.title(graph_title) # Title
        
        # Show the legend with lines and labels added to the above lists.
        plt.legend(lines, labels, bbox_to_anchor=(1.05, 1), loc="upper left", title=legend_title, frameon=False)
      
        ######## X - Axis ########
        
        #Set Amount of ticks on x-axis
        x_ticks = subsetted_fy_data[fy_x_value].unique()[::len(subsetted_fy_data[fy_x_value].unique()) // number_of_x_ticks]
        plt.xticks(x_ticks, [date.strftime('%m/%Y') for date in pd.to_datetime(x_ticks)])
        
        # Set the x-axis limits to start from the first value
        plt.xlim(subsetted_fy_data[fy_x_value].min(), subsetted_fy_data[fy_x_value].max())
        
        # Rotate x-axis labels for better visibility
        plt.gcf().autofmt_xdate()
        
        ######## Other Settings ########
        
        # Draw a horizontal line at y = 0
        if show_zero_line:
            plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
            
        #Set text for source of data
        plt.gcf().text(0.2, 0.02, source_text, ha="center")
        
        # Save the plot
        if export_graph:
            #The bbox_inches option makes sure that everything is included in the graph (including the legend)
            plt.savefig(os.path.join(figures_directory, export_name), bbox_inches='tight')
    
        # Show the plot
        plt.show()

##################################### Executing functions #####################################

createPlot(YS_show_graph, SY_show_on_graph, YS_graph_resolution, yield_spread, second_y_axis_data , YS_start_date, YS_end_date, YS_maturity_list, SY_y, YS_x, SY_x, YS_y_label, SY_y_label, YS_x_label, SY_legend_label, YS_graph_title, YS_legend_title, YS_amount_x_ticks, YS_show_zero_line, YS_source_text, YS_export_png, YS_export_name) 

#Don't want to show second y-axis for covered bonds and federal bonds
createPlot(FB_show_graph, False, FB_graph_resolution, federal_bonds, second_y_axis_data , FB_start_date, FB_end_date, FB_maturity_list, SY_y, FB_x, SY_x, FB_y_label, SY_y_label, FB_x_label, SY_legend_label, FB_graph_title, FB_legend_title, FB_amount_x_ticks, FB_show_zero_line, FB_source_text, FB_export_png, FB_export_name) 
createPlot(CB_show_graph, False, CB_graph_resolution, covered_bonds, second_y_axis_data , CB_start_date, CB_end_date, CB_maturity_list, SY_y, CB_x, SY_x, CB_y_label, CB_y_label, CB_x_label, SY_legend_label, CB_graph_title, CB_legend_title, CB_amount_x_ticks, CB_show_zero_line, CB_source_text, CB_export_png, CB_export_name) 
