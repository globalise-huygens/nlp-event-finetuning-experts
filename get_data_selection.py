# create dictionary where each doc gets an identifier and is linked to its name, its year, its annotator, the half century correspondent to the  year
import os
import random

def get_filepath_list(root_path):
    """
    Get complete filepaths leading to all relevant training data documents in a list
    :param root_path: str
    """
    file_list = []
    for root, _, filenames in os.walk(root_path):
        for filename in filenames:
            file_list.append(os.path.join(root, filename))
    return(file_list)

def create_data_inventory(file_list):
    """
    creates a data inventory according to filepath and filename structure of data
    """
    data_inventory = []
    for x in file_list:
        d = dict()
        spl = x.split('/')
        print(spl)
        if spl[3] == 'train_2':
            round = '2'
        if spl[3] == 'train_3':
            round = '3'
        if spl[3] == 'train_4':
            round = '4'
        if spl[3] == 'train_5':
            round = '5'
        if spl[3] == 'synthetic':
            round = 'synthetic'
        if spl[4] == 'special_topic_ESTA':
            round = '3_ESTA'
        if round == '2':
            inv_nr = ((spl[-1].split('_'))[2]).split(' - ')[0]
            scan_nrs = ((spl[-1].split('_'))[3]).split(' - ')[0]
        if round == '3' or round == '3_ESTA':
            inv_nr = ((spl[-1].split('_'))[4]).split(' - ')[0]
            scan_nrs = ((spl[-1].split('_'))[5]).split(' - ')[0]
        if round == '4':
            inv_nr = ((spl[-1].split('_'))[2]).split(' - ')[0]
            scan_nrs = ((spl[-1].split('_'))[3]).split(' - ')[0]
        if round == '5':
            inv_nr = ((spl[-1].split('_'))[2]).split(' - ')[0]
            scan_nrs = ((spl[-1].split('_'))[3]).split(' - ')[0]
        if round == 'synthetic':
            inv_nr = 'synthetic'
            scan_nrs = 'synthetic'
        d['original_filename'] = spl[-1]
        d['round'] = round
        d['inv_nr'] = inv_nr
        d['scan_nrs'] = scan_nrs
        data_inventory.append(d)
    return(data_inventory)

def file_selection_invnr(root_path, inv_nr):
    """
    Single test file selection on basis of inventory number
    Creates "settings.json" and adds metadata of test file
    """

    filepaths = get_filepath_list(root_path)

    settings = dict()
    metadata = []

    data_inventory = create_data_inventory(filepaths)
    for d in data_inventory:
        if d['inv_nr'] == inv_nr:
            metadata = d
    settings['metadata_testfile'] = metadata
    return (settings)


if __name__ == "__main__":
    root_path = "json_per_doc/"
    filepaths=get_filepath_list(root_path)
    data_inv=create_data_inventory(filepaths)
    settings = file_selection_invnr(root_path, data_inv)

