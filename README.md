# Closest-Facilities

This tutorial provides step-by-step instructions on how to create a road network dataset using ArcGIS Pro and perform network analysis using **the Closest Facility** tool in the ArcPy module. The tutorial assumes you have basic knowledge of ArcGIS Pro and Python scripting. Main Reference: 
https://pro.arcgis.com/en/pro-app/latest/arcpy/network-analyst/closestfacility.htm

## Prerequisites
- ArcGIS Pro installed on your computer
- RoadNetwork.shp file containing road network data and your facilities.shp files

## Output
- For every origin, find the closest destination on the road network, including a complete **route.shp** which contains the information of fields, distance and so on.

## Step 1: Create a File Geodatabase and Import Road Network Data
1. Launch ArcGIS Pro and open a new project.
2. Right-click on the Catalog pane and select **"New File Geodatabase."**
3. Provide a name for the geodatabase, e.g., Road Network.gdb, and click "Save."
4. Right-click on the newly created geodatabase and select **"New Feature Dataset."**
5. Specify a name for the feature dataset, e.g., Road, and choose the appropriate coordinate system, such as GCS_WGS_1984.
6. Right-click on the feature dataset and select **"Import > Feature Class (single)."**
7. Browse to locate the RoadNetwork.shp file and import it into the feature dataset.

    ![Geodatabase](images/Geodatabase.png)

8. Right-click on the Road, **New Network Dataset.**

    ![Network Dataset](images/Network_Dataset.png)      ![Road Network](images/Road_Network.png) 
    
9. Right-click Beijing_road, choose Properties to add **Travel Mode**. **Important**

    ![Properties](images/Properties.png) ![Travel Mode](images/Travel_Mode.png) 

## Step 2: Create Facilities Geodatabase
1. Right-click on the Catalog pane and select "New File Geodatabase."
2. Provide a name for the geodatabase, e.g., io.gdb, and click "Save."

    ![io](images/io.png)
    
## Step 3: Set Python Environment
1. Open the Python Command Prompt within ArcGIS Pro or any Python IDE.
2. Set the Python environment to the ArcGIS Pro interpreter, following is mine address:

     ![Py_Env](images/Py_Env.png)
     
## Step 4: Run FindNearestFacilities.py

