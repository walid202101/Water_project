import utils as ut
import numpy as np

def main():
    np.seterr(divide = 'ignore') 
    # the current directory (this should be replace by link to the fcs files from the cloud storage )
    directory = r'fcs_files'
    datasets = ut.loading_fcs_from_directory(directory)
    
    # After reading the files we transforms the data and keep only the dataframe from the FCS file 
    transformed_data = []
    for fc_data in datasets:
        # fc_data.data = fc_data.data[fc_data.data['FSC-A'] > 10]
        # fc_data.data = fc_data.data[fc_data.data['SSC-A'] > 10]
        # print(fc_data.data.columns)
        # fc_data.data = fc_data.data[['FL1-A', 'FL3-A']]
        converted_data = ut.transformed_data(fc_data)
        transformed_data.append(converted_data.data)
        
    # Plotting heatmap based on selected columns
    for i in transformed_data: 
        ut.plot_heatmap(i, 'FL1-A', 'FL3-A', datasets[0].ID)
    
    

    
main()