##################################### Importing Packages #####################################
import pandas as pd  #Used for variety of tasks
import os #Used to change & verify directory
import seaborn as sns #Used to create lineplot
import matplotlib.pyplot as plt #Used to edit plot
from datetime import datetime

##################################### Settings #####################################
    
# CSV File name
file_name = "ts_federal_bond_price_2024_04_27.csv"

show_graph = True # Decide if you want to show the graphs
export_png = True # Decide if you want to export graphs as png to figures folder

graph_resolution = 1000 # Graph resolution in dpi
export_name = "Bond_Price_Time_Series_" + datetime.today().strftime('%Y_%m_%d') + ".png" # Set export name for graph

start_date = "2009-01-01"# Start date on graph
end_date = "2024-04-19" # End date on graph

x = "Date" # Set column name for data for x-axis
y = "Bond_Price"

x_label = "" # Set x-axis label
y_label = "Federal Bond Price" # Set  y-axis label

amount_x_ticks = 20 # Set amount of ticks shown on x-axis
show_zero_line = False # Decide if you want to show zero line in graph

graph_title = "Bond Price over Time" # Set graph title

show_legend = False # Decide if you want to show the legend
legend_title = "Legend" # Set legend title
legend_value = "Federal Bond Price" # Set the value of the legend

source_text = "Source: Svensson Parameter Bundesbank" # Set source of data

# Set file path for main folder of data for first y-axis
file_path = "C:/Users/mauri/Desktop/Work/1) Current Employers/University of Tübingen (HIWI)/Department of Finance/3) Liquidity Project/Liquidity_Project" 
#file_path = r'C:\Users\Tobias\OneDrive - UT Cloud\02 Forschung\06 Asset Allocation\hiwis\Interest-Rates'

#Set folder path for data to be imported for first y-axis.
#This is a path starting from the location of "file_path".
folder_path = "Clean_Data/"


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
bond_price = pd.read_csv(f"{folder_path}{file_name}") # Importing Yield Spread Data (Frist y-axis)
    
##################################### Visualizing Data #####################################

# First Y-Axis = Left Y-Axis
# Second Y-Axis = Right Y-Axis

def createPlot(showGraph, #Boolean indicating if you want to generate & show a graph
               
               graph_resolution, #Resoltion for graph
               
               data, #Data for first y-axis
               
               start_date, #Start date for x-axis
               end_date, #End date for x-axis
               
               x_value, #Column name of x-axis in dataframe
               y_value, #Column name of y-axis in dataframe
               
               x_label, #Label for x-axis
               y_label, #Label for first y-axis 
               
               graph_title, #Title of graph
               
               show_legend,
               legend_title,  #Title of legend
               legend_value,
               
               number_of_x_ticks, #Number of ticks shown on x-axis
               show_zero_line, #Boolean indicating if you want to see a line indicating the zero line on the left y-axis
               source_text,  #Text for source of Data shown below the graph
               export_graph, #Boolean indicating if graph should be exported as png. 
               export_name): #Name of graph being exported (if export_graph = true)

    #Only show graph if this is wanted
    if showGraph:
        
        ######## DATA ########
        subsetted_data = data[data["Date"] >= start_date]
        subsetted_data = subsetted_data[subsetted_data["Date"] <= end_date]
        
        ######## Figure Size & Resolution ########
        
        # Set the figure size and resolution
        plt.figure(figsize=(10, 6), dpi=graph_resolution)
        
        # Plotting with Seaborn
        sns.set(style="ticks")  # Set the style of the plot
        
        ######## Y - Axis ########
        
        # Generates colorblind color palette
        color_palette = sns.color_palette("colorblind")
                
        ######## Line - Plots ########
        
        #If legend should be plotted, labels are added. Otherwise they are omitted.
        if show_legend:
            sns.lineplot(y=y_value, x=x_value, data=subsetted_data, palette=color_palette, label=legend_value)
        else:
            sns.lineplot(y=y_value, x=x_value, data=subsetted_data, palette=color_palette)
        
        ######## Labels, Title, Legend ########
        
        # Adding labels and title
        
        plt.xlabel(x_label) # X-Axis Label
        plt.ylabel(y_label) # Y-Axis Label
        
        plt.title(graph_title) # Title
        
        #Only plots legend if this is wanted
        if show_legend:
            # Show the legend
            plt.legend(bbox_to_anchor=(1, 1), #Anchors legend outsite of graph
                       loc="upper left", 
                       title=legend_title, #Sets legend title
                       frameon=False) #Removes edge of legend box
      
        ######## X - Axis ########
        
        #Set Amount of ticks on x-axis
        x_ticks = subsetted_data[x_value].unique()[::len(subsetted_data[x_value].unique()) // number_of_x_ticks]
        plt.xticks(x_ticks, [date.strftime('%m/%Y') for date in pd.to_datetime(x_ticks)])
        
        # Set the x-axis limits to start from the first value
        plt.xlim(subsetted_data[x_value].min(), subsetted_data[x_value].max())
    
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

createPlot(show_graph, graph_resolution, bond_price, start_date, end_date, x, y, x_label, y_label, graph_title, show_legend, legend_title, legend_value, amount_x_ticks, show_zero_line, source_text, export_png, export_name)
