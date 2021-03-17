import read_fcs_files as read
import transformation
import heatmap_plotting
import differences

directory_fcs = r'fcs_files' 
directory_transformed = r'transformed_files'
directory_generatedmap = r'generatedmap_files'
def main():
    
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

    # Phase 4
    generated_maps = []
    for data in transformed_data:
        generated_maps.append(heatmap_plotting.generate_map(data, "Hello", channel1, channel2))
        
    
    # Phase 5
    gates = []
    for data in generated_maps:
        gates.append(heatmap_plotting.gating(0,3,1,4, data))
    
    # Phase 6
    differences.get_and_save_diff(gates[0], gates[1]) 
   
    
    
main()