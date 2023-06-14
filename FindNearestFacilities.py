# -*- coding: utf-8 -*-
'''
@Time    : 2023/6/12 12:57
@Author  : Ericyi
@File    : FindNearestFacilities.py

'''
import arcpy
arcpy.CheckOutExtension("network")

# set network path
network_dataset = r"\Road Network.gdb\Road\Beijing_road"

nd_layer_name = "RoadNetwork"

# station - destination
input_facilities = r"\io.gdb\baidu_station_metro_entrance_deduplicated_110100_2022"
# entrance - origin
input_incidents = r"\io.gdb\entrance"
# output: route including fields, length and other information
output_routes = r"\io.gdb\ClosestRoutes"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(network_dataset, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)

travel_mode = nd_travel_modes["New Travel Mode"]
print(travel_mode)

# Instantiate a ClosestFacility solver object
closest_facility = arcpy.nax.ClosestFacility(nd_layer_name)

# Set properties
closest_facility.travelMode = travel_mode
closest_facility.defaultImpedanceCutoff = 15
closest_facility.defaultTargetFacilityCount = 1
closest_facility.routeShapeType = arcpy.nax.RouteShapeType.TrueShapeWithMeasures

# Load inputs
closest_facility.load(arcpy.nax.ClosestFacilityInputDataType.Facilities, input_facilities)
closest_facility.load(arcpy.nax.ClosestFacilityInputDataType.Incidents, input_incidents)
# Solve the analysis
result = closest_facility.solve()

print(result)
# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.ClosestFacilityOutputDataType.Routes, output_routes)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
