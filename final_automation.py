import os
import logging

rel_dict = {'fc_networks.py': 'FC Networks',
            'fcoe_networks.py': 'FCOE-Networks',
            'ethernet_networks.py': 'Ethernet Networks',
            'network_sets.py': 'Network Sets',
            'connection_templates.py': 'ConnectionTemplates'}

def generate_library_files(resource_name='', api_version=2200):
    '''
    This method will generate the library files for each api version for ruby SDK.
    '''
    cwd = os.getcwd() # gets the path of current working directory
    print(cwd)
    lib_path_list = ['lib', 'oneview-sdk', 'resource']
    lib_path = str(cwd) + os.path.sep + os.path.sep.join(lib_path_list)
    os.chdir(lib_path)
    cwd = os.getcwd() # gets the path of current working directory
    print(cwd)


if __name__ == '__main__':
    generate_library_files()
