# Liquidity Premium

> [!NOTE]
> There are three Python code files. You can find instructions on how to use them below.

## Tidying Data

### File Objectives:

- Imports Svensson Parameters published by the German Federal Bank (GFB) using the GFB API.
- Calculates interest rates for any desired maturity for German government bonds and covered bonds in basis points.
- Calculates the yield spread for any desired maturity between German government bonds and covered bonds in basis points. 

### Settings:

Determine how many years of maturity you would like to calculate. If you set *T = 50*, it will generate a CSV file that includes interest rates for 50 years. 
The output file will have columns that indicate what maturity the interest rates refer to.
```
T = 50
```

Set your file path. This is where your output will be exported to. You don't need to create any output folders as this is done automatically. 
```
file_path = "C:/Users/..." 
```

### Output:

This code generates five output files:

- *ts_federal_bonds_svensson_parameters_yyyy_mm_dd.csv* = German Government Bond Svensson Parameters for each day
- *ts_covered_bonds_svensson_parameters_yyyy_mm_dd.csv* = Covered Bond Svensson Parameters for each day

The first column of the following files is the date. All other columns are the interest rates in basis points for different maturities.
The column structure is always the same. 0_Y_1 refers to 1-year maturity, 0_Y_2 refers to 2-year maturity, etc. 

- *ts_federal_bonds_yyyy_mm_dd.csv* = German Government Bond interest rates for all maturities for each day in basis points.
- *ts_covered_bonds_yyyy_mm_dd.csv* = Covered Bond interest rates for all maturities for each day in basis points
- *ts_yield_spread_yyyy_mm_dd.csv* = Yield Spread for all maturities for each day in basis points. 

The files will be saved in the folder */Clean_Data*. This folder is automatically generated if it doesn't exist. 

## Visualizing Time Series of Interest Rates

### File Objectives:

- Visualizes the time series of interest rates for any desired maturity 

### Settings:

The settings always follow the same structure! The first two letters of a setting are capitalized and indicate what visualization is affected by it.
The following abbreviations are used:

    - YS = Yield Spread
    - FB = German Federal Government Bonds
    - CB = Covered Bonds

Use this setting to indicate what date ending your CSV input files have (Ref. Output of Tidying Data Code)
For example *YS_csv_suffix = "2023_12_25"* will read the file *ts_federal_bonds_2023_12_25.csv* as input file.
```
YS_csv_suffix = "2023_12_25"
FB_csv_suffix = "2023_12_25"
CB_csv_suffix = "2023_12_25"    
```

Decide if you want to show the graphs. For example, *YS_show_graph = False* will prevent the code from attempting to generate a time series graph of the yield spread.

```
YS_show_graph = True
FB_show_graph = True
CB_show_graph = True
```

Decide if you want to export graphs as PNG to the figures folder. The code will automatically generate a figures folder if there is none.

```
YS_export_png = True
FB_export_png = True
CB_export_png = True
```

Set an export name for the graph

```
YS_export_name = "YS_Time_Series" + datetime.today().strftime('%Y_%m_%d') + ".png"
FB_export_name = "FB_Time_Series" + datetime.today().strftime('%Y_%m_%d') + ".png"
CB_export_name = "CB_Time_Series" + datetime.today().strftime('%Y_%m_%d') + ".png"
```

This will set the first date that is shown on the graph. It indicates on what day you would like to start your time series. 

```
YS_start_date = "2009-01-01"
FB_start_date = "2009-01-01"
CB_start_date = "2009-01-01"
```

This will set the last date that is shown on the graph.

YS_end_date = "2022-01-30"
FB_end_date = "2022-01-30"
CB_end_date = "2022-01-30"

This list should include all maturities that you would like to show on the graph. You can only visualize the maturities that the Tidying code has generated.
A list of *[1, 5, 10]* will generate three lines with 1, 5, and 10-year maturity. 

```
YS_maturity_list =  [1, 5, 10]
FB_maturity_list =  [1, 5, 10]
CB_maturity_list =  [1, 5, 10]
```

Depending on your preferences and the period considered in your graphs you can determine how many dates you want to show on the x-axis. 

```
YS_amount_x_ticks = 20
FB_amount_x_ticks = 20
CB_amount_x_ticks = 20
```

Set x-axis label

```
YS_x_label = ""
FB_x_label = ""
CB_x_label = ""
```

Set y-axis label

```
YS_y_label = "Yield Spread [in bp]"
FB_y_label = "Interest Rate [in bp]"
CB_y_label = "Interest Rate [in bp]"
```

Set graph title

```
YS_graph_title = "Yield Spread between Covered Bonds & Gov. Bonds"
FB_graph_title = "German Government Bonds Interest Rates"
CB_graph_title = "Covered Bonds Interest Rates"
```

Set legend title

```
YS_legend_title = "Maturity"
FB_legend_title = "Maturity"
CB_legend_title = "Maturity"
```

Decide if you want to show a zero line on the graph. If you set this to true, it will generate a dashed straight line for y = 0. 

```
YS_show_zero_line = False
FB_show_zero_line = True
CB_show_zero_line = True
```

Set source text of data. This will be printed in the bottom left part of the graph. 

```
YS_source_text = "Source: Svensson Parameter Bundesbank"
FB_source_text = "Source: Svensson Parameter Bundesbank"
CB_source_text = "Source: Svensson Parameter Bundesbank"
```

Set file path to the directory that includes the figures and data input folders */Figures* and */Clean_Data*. 
```
file_path = "C:/Users/..."
```

### Output:

This code can generate three PNG files. These are visualizations of the time series of interest rates for German Government Bonds, Covered Bonds, and the respective yield spread between the two types of bonds. 

Here is an example of a graph that was generated with this code. It shows the time series of interest rates for German Government bonds with maturities of 1 year, 5 years, and 10 years in basis points. 

![Time Series of interest rates for German Government bonds with maturities 1, 5, and 10 years.](https://drive.google.com/file/d/1_OZNqQbO0StkctRKtcy2iYKnxV8GzAaD/view?usp=sharing)

## Visualizing Term Structure of Interest Rates

### File Objectives:

- Calculate interest rates for German government bonds and covered bonds using Svensson Parameters published by the German Federal Bank. 
- Calculate the yield spread between interest rates of German government bonds and covered bonds.
- Visualize the time series of interest rates for German government bonds and covered bonds. 
- Visualize the term structure of interest rates.

### Settings:

The settings always follow the same structure! The first two letters of a setting are capitalized and indicate what visualization is affected by it.
The following abbreviations are used:

    - YS = Yield Spread
    - FB = German Federal Government Bonds
    - CB = Covered Bonds

Use this setting to indicate what date ending your CSV input files have (Ref. Output of Tidying Data Code)
For example *YS_csv_suffix = "2023_12_25"* will read the file *ts_federal_bonds_2023_12_25.csv* as input file.

```
YS_csv_suffix = "2023_12_25"
FB_csv_suffix = "2023_12_25"
CB_csv_suffix = "2023_12_25"
```

Decide if you want to show the graphs. For example, *YS_show_graph = False* will prevent the code from attempting to generate a time series graph of the yield spread.

```
YS_show_graph = False
FB_show_graph = True
CB_show_graph = True
```

Decide if you want to export graphs as PNG to the figures folder. If the folder doesn't exist, it will be generated automatically. 

```
YS_export_png = True
FB_export_png = True
CB_export_png = True
```

Set an export name for the graph

```
YS_export_name = "YS_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"
FB_export_name = "FB_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"
CB_export_name = "CB_Term_Structure_" + datetime.today().strftime('%Y_%m_%d') + ".png"
```

Set the dates for which you would like to show the term structure. For example, a list of *["2009-12-01", "2022-12-01", "2023-12-01"]* will generate three lines showing the term structures for the respective dates in the list. 

```
YS_date = ["2009-12-01", "2022-12-01", "2023-12-01"]
FB_date = ["2009-12-01", "2022-12-01", "2023-12-01"]
CB_date = ["2009-12-01", "2022-12-01", "2023-12-01"]
```

Set a list of maturities that you would like to show on the graph for each term structure. For example, *YS_maturity_list = list(range(1, 31))* will generate a list of numbers from 1 to 30. This will generate a graph that shows 30 interest rates in basis points. 

```
# YS_maturity_list =  [1, 2, 3, 4, 5, 6, 7]
YS_maturity_list = list(range(1, 31))
# FB_maturity_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
FB_maturity_list = list(range(1, 31))
# CB_maturity_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
CB_maturity_list = list(range(1, 31))
```

Set how many years you would like to see between two ticks on the x-axis. This allows you to modify the amount of dates shown on the x-axis. Here you don't set the amount of ticks but rather the distance between the ticks.

```
YS_show_every_nth_x_tick = 5
FB_show_every_nth_x_tick = 5
CB_show_every_nth_x_tick = 5
```

Set x-axis label

```
YS_x_label = "Number of Years"
FB_x_label = "Number of Years"
CB_x_label = "Number of Years"
```

Set y-axis label

```
YS_y_label = "Yield Spread [in bp]"
FB_y_label = "Interest Rate [in bp]"
CB_y_label = "Interest Rate [in bp]"
```

Set graph title

```
YS_graph_title = "Yield Spread Term Structure"
FB_graph_title = "Government Bonds Term Structure"
CB_graph_title = "Covered Bonds Term Structure"
```

Set legend title

```
YS_legend_title = "Date"
FB_legend_title = "Date"
CB_legend_title = "Date"
```

Decide if you want to show a zero line on the graph. If you set this to true, it will generate a dashed straight line for y = 0. 

```
YS_show_zero_line = False
FB_show_zero_line = True
CB_show_zero_line = True
```

Set source text of data. This will be printed in the bottom left part of the graph. 

```
YS_source_text = "Source: Svensson Parameter Bundesbank"
FB_source_text = "Source: Svensson Parameter Bundesbank"
CB_source_text = "Source: Svensson Parameter Bundesbank"
```

Set file path to the directory that includes the figures and data input folders */Figures* and */Clean_Data*. 

```
file_path = "C:/Users/..."
```

### Output:

This code can generate three PNG files. These are visualizations of the term structure of interest rates for German Government Bonds, Covered Bonds, and the respective yield spread between the two types of bonds. 
