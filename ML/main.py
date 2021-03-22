import read_fcs_files as read
import transformation
import heatmapping
import differences
import plotting


# 1st Upload File (send to server, return back with channels and metadata)
# 2nd channel1, channel2, transform method, b (between 300 & 1000), file name plot
# 3rd transformation plot result in front-end (save in transform directory if the user agree)
#   IF Agree
#       4th send Bindwith option(between 500 & 1000), return heatmap
#       IF Agree
#           5th choose x1,x2, y1, y2 file is read
#           6th find diff with other file
#        ELSE
#           repeat
#   ELSE 
#       back to 2nd


directory_fcs = r'fcs_files' 
directory_transformed = r'transformed_files'
directory_generatedmap = r'generatedmap_files'
def main():
    
    # Phase 1
    # Input: <class 'FlowCytometryTools.core.containers.FCMeasurement'>
    # Output: <class 'FlowCytometryTools.core.containers.FCMeasurement'>
    directory = r'fcs_files'    
    datasets = read.loading_fcs_from_directory(directory)
    
    # Phase 2
    # channels name
    channel1 = "FL1-A"
    channel2 = "FL3-A"

        
    # Phase 3
    #Transformed
    # Input: <class 'FlowCytometryTools.core.containers.FCMeasurement'>
    # Output: <class 'pandas.core.frame.DataFrame'>
    transformed_data1 = transformation.transform_file(channel1, channel2,datasets[0], 'hlog', 500)
    transformed_data2 = transformation.transform_file(channel1, channel2,datasets[1], 'hlog', 500)

    # Phase 4
    # Input: <class 'pandas.core.frame.DataFrame'>
    # Output: <class 'numpy.ndarray'>
    generated_map1 = heatmapping.generate_map(transformed_data1, channel1, channel2, 1000)
    generated_map2 = heatmapping.generate_map(transformed_data2, channel1, channel2, 1000)
    
    # Phase 5
    # Input: <class 'numpy.ndarray'>
    # Output: <class 'numpy.ndarray'>
    gate1 = heatmapping.gating(1,2,0,2, generated_map1)
    gate2 = heatmapping.gating(0,2,0,2, generated_map2)
    
    # Phase 6
    # Input: <class 'numpy.ndarray'>
    # Output: <class 'numpy.ndarray'>
    diff = differences.get_diff(gate1, gate2)
    
    
main()