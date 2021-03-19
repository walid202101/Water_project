import read_fcs_files as read
import transformation
import heatmap_plotting
import differences


# 1st Upload File (send to server, return back with channels and metadata)
# 2nd channel1, channel2, transform method, b (between 300 & 1000) 
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
    #Important Note
    # To save
    
    
    
    # Phase 1
    # the current directory (this should be replace by link to the fcs files from the cloud storage )
    directory = r'fcs_files'    
    datasets = read.loading_fcs_from_directory(directory)
    
    # Phase 2
    # channels name
    channel1 = "FL1-A"
    channel2 = "FL3-A"
    
    # Phase 3
    transformed_data = []
    #Transformed
    for data in datasets:
        transformed_data.append(transformation.transform_file(
            channel1, channel2, 
            data, 'hlog', 500))
    # To save use read_fcs_files save_dataframe
    # To load Use read_fcs_files load_dataframe

    # Phase 4
    generated_maps = []
    for data in transformed_data:
        generated_maps.append(heatmap_plotting.generate_map(data, "Hello", channel1, channel2))
    # To save use read_fcs_files save_array
    # To load Use read_fcs_files load_array 
    
    for data in generated_maps:
        heatmap_plotting.plotting(channel1, channel2, data)
      
    
    # Phase 5
    gates = []
    for data in generated_maps:
        gates.append(heatmap_plotting.gating(0,3,1,4, data))
    # To save use read_fcs_files save_array
    # To load Use read_fcs_files load_array 
    
    # Phase 6
    diff = differences.get_diff(gates[0], gates[1])
    # To save use read_fcs_files save_array
    # To load Use read_fcs_files load_array 
    print(diff)
   
    
    
main()