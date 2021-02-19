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
        # print(fc_data.data.columns)
        # fc_data.data = fc_data.data[['FL1-A', 'FL3-A']]
        converted_data = ut.transformed_data(fc_data)
        transformed_data.append(converted_data.data)
        
    clean_data = []
    for data in transformed_data:
        
        cleaned = ut.clean_data(data)
        print(str(len(data)) + ", " + str(len(cleaned)))
        clean_data.append(cleaned)
        
    
        
    # Plotting heatmap based on selected columns
    for i in clean_data: 
        ut.plot_fl1_fl3(i, "Title")
        ut.plot_sca_fca(i, "Title")
    
    

    
main()