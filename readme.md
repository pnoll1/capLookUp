capLookUp
=========
Repository contains several files with the goal of querying a sqlite database using various input and output methods.  
All files use crane.db as the database.

capLookUp.py
------------
File uses a qt gui to get input from user, uses input to query sqlite database and returns result in gui.  
All inputs must exactly match table name and data in each column.  
CraneCapacityLookUp.ui is qt designer file that defines the gui and is loaded in the file.

capPlot.py
----------
File takes input directly in the file, querys sqlite database and returns a graph of radius vs capacity using matplotlib.

xlCapLookup.py
--------------
File takes input from xl workbook, querys sqlite database and returns capacities for configuration and radius in the correct column in the xl workbook.  
File is made to be launched from target sheet using macro that calls RunPython in xlwings.bas that calls the file; see xlwings docs for more info on macro.  
xlwings.bas should be imported into worksheet and setup to correctly find file and python interpreter; see xlwings docs for more info.  
Starting row and column are hardcoded to radius column of first lift. Capacites are hardcoded to be output to 2 columns to left of radius.  
Capacities will be filled working down radius column until it finds a cell in radius column with nothing in it.

crane.db
--------
Sqlite database containing pertinent data.  
Each table is a different model of crane. For example, Demag Ac615 is named DemagAc615.
Each table contains 9 columns:  
	1.BoomType: data stored in all caps
	2.Counterweight: in lbs
	3.Outrigger: data stored with first letter capitalized
	4.BoomLen: in ft
	5.BoomAngle: in degrees
	6.JibLen: in ft
	7.JibAngle: in degrees
	8.Radius: in ft
	9.Capacity: in lbs  
If a column is not applicable it will contain a None type.
