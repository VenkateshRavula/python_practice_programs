import logging
import requests
from bs4 import BeautifulSoup
import sys
import os
from datetime import datetime

rel_dict = {'FC Networks': 'fc_networks',
            'FCOE Networks': 'fcoe_networks',
            'Ethernet Networks': 'ethernet_networks',
            'Network Set': 'network_sets',
            'Connection Templates': 'connection_templates',
            'Certificates Server': 'certificates_server',
            'Enclosures': 'enclosures',
            'Enclosure Groups': 'enclosure_groups',
            'Firmware Drivers': 'firmware_drivers',
            'Hypervisor Cluster Profiles': 'hypervisor_cluster_profiles',
            'Hypervisor Managers': 'hypervisor_managers',
            'Interconnects': 'interconnects',
            'Interconnect Types': 'interconnect_types',
            'Logical Enclosures': 'logical_enclosures',
            'Logical Interconnects': 'logical_interconnects',
            'Logical Interconnect Group': 'logical_interconnect_groups',
            'Restores': 'restores',
            'Scopes': 'scopes',
            'Server Hardware': 'server_hardware',
            'Server Hardware Types': 'server_hardware_types',
            'Server Profiles': 'server_profiles',
            'Server Profile Templates': 'server_profile_templates',
            'Storage Pools': 'storage_pools',
            'Storage Systems': 'storage_systems',
            'Storage Templates': 'storage_volume_templates',
            'Storage Volume Attachments': 'storage_volume_attachments',
            'Storage Volume': 'volumes',
            'Tasks': 'tasks',
            'Uplink Sets': 'uplink_sets'
            }

class DataFromWebScraping(object):
    def __init__(self, ele):
        self.ele = ele
        self.replaced_ele = self.ele.replace('_', '-')

    def data_scraped(self):
        URL = "https://techlibrary.hpe.com/docs/enterprise/servers/oneview5.0/cicf-api/en/rest/" + self.replaced_ele + ".html.js"
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
        body = soup.find('body')
        string = str(body).replace('<body>define([],"', '').replace('");</body>', '')
        soup = BeautifulSoup(string, 'html5lib')
        api_list = soup.find('div', {"class": "\\\"api-list\\\""})
        api_with_method = []
        http_methods = []
        apis = []
        for span in api_list.find_all('span', {'class', '\\\"uri\\\"'}):
            apis.append(span.text.strip())
        for span in api_list.find_all('span', {'class', '\\\"method'}):
            http_methods.append(span.text.strip())
        for http_method, api in zip(http_methods, apis):
            api_with_method.append({api, http_method})
    
        return api_with_method

def LoadResourcesFromFile(file_name='resourcename_list.txt'):
    resource_file = open(file_name, 'r')
    resources_from_file = resource_file.read().splitlines()
    resource_file.close()
    return resources_from_file

def ExecuteFiles():
    loaded_resources = LoadResourcesFromFile()
    cwd = os.getcwd()
    failed_files = []
    success_files = []
    examples = []
    valid_sdks = ['python', 'ruby', 'chef']
    print("loaded_resources are {}".format(str(loaded_resources)))
    val = input("Please enter SDK you want to validate: ")
    print("Started executing files")
    LOG_FILENAME = datetime.now().strftime('logfile_%H_%M_%d_%m_%Y.log')
    sys.stdout = open(LOG_FILENAME, 'w')    #flushing console logs to a logFile
    if val in valid_sdks:
        for ele in loaded_resources:
            examples.append(rel_dict[ele])
        for example in examples:
            example_file = cwd + '/' + example
            try:
                if val == 'python':
                    example_file_with_extension = example_file + str('.py')
                    print(">> Executing {}..".format(example))
                    exec(compile(open(example_file_with_extension).read(), example_file_with_extension, 'exec'))
                    success_files.append(example)
                else:
                    pass
            except Exception as e:
                print("Failed to execute {} with exception {}".format(str(example),(str(e))))
                failed_files.append(example)
        sys.stdout.close()
        print("success files are {}".format(str(success_files)))
        return success_files
    else:
        print("Sorry, please enter the valid SDK among the following {}".format(str(valid_sdks)))

class WriteToChangeLog(object):
    """
    Here we have exception handling. In case if any of the value for the key is not present,
    then it will raise a exception and we are catching it. Our script will continue further and
    will add modules other than the missing one.

    Output will look like:
    ##### Features supported with the current release(v5.0.0)
    - FC Network
    - FCOE-Network
                   
    :param rel_list:
    :param rel_version:
    :return:
    """
    def __init__(self, rel_list):
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        f = open("CHANGELOG.md", "r")
        first_line = f.readline()
        self.added_integer = float(first_line[2:5]) + float('0.1')
        self.final_version = str(self.added_integer) + '.0'
        f.close()

    def write_data(self):
        rel_modules = []
        api_version = '2200'
        oneview_api_version = 'OneView ' + 'v' + str(self.added_integer)
        try:
            for ele in self.rel_list:
                rel_modules.append(rel_dict[ele])
        except Exception as e:
            logging.debug("Unable to find a module {0}".format(str(e)))

        print("Started writing to CHANGELOG")

        dummy_file = open("dummy_CHANGELOG.md", "w")
        dummy_file.write("# {}(unreleased)".format(str(self.final_version)))
        dummy_file.write("\n#### Notes\n")
        dummy_file.write("Extends support of the SDK to OneView REST API version {} ({})".format(str(api_version),str(oneview_api_version)))
        dummy_file.write("\n\n##### Features supported with the current release\n")
        for ele in sorted(rel_modules):
            dummy_file.write("- {0} \n".format(str(ele)))
        dummy_file.write("\n")
        dummy_file.close()
    
        original_file = open("CHANGELOG.md", "r")
        data = original_file.read()
        original_file.close()

        dummy_file = open("dummy_CHANGELOG.md", "r")
        data2 = dummy_file.read()
        dummy_file.close()

        data2 += data
        with open("CHANGELOG.md", "w") as final:
            final.write(data2)
        final.close()
        os.remove("dummy_CHANGELOG.md")
        print("Completed writing to CHANGELOG")

resource_names = []


class WriteToEndpointsFile(object):
    def __init__(self, product_table_name, new_version, executed_files):
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        self.line_nos = {}
        self.res_lines = {}
        self.product_table_name = product_table_name
        self.new_version = new_version
        self.all_lines = None
        self.executed_files = executed_files
        
    def write_md(self):
        file = open('endpoints-support.md', 'w')
        file.writelines(self.all_lines)
        file.close()

    def load_md(self):
        file = open('endpoints-support.md')
        self.all_lines = file.readlines()

    def add_column(self, product_table_name, new_version):
        count = 0
        self.load_md()
        for line in self.all_lines:
            count += 1
            if product_table_name in line:
                break

        head_line = self.all_lines[count + 1].split()
        if new_version:
            curr_version = int(head_line[-2].split('V')[-1])
            new_version = 'V' + str(curr_version + 200)

        column_added = False
        while count < len(self.all_lines):
            add_col = None
            line = self.all_lines[count].rstrip('\n')

            if "Endpoints" in self.all_lines[count]:
                add_col = line + " " + new_version + '               |\n'

            elif "---------" in self.all_lines[count]:
                add_col = line + ' :-----------------: |\n'
                column_added = True

            if add_col:
                self.all_lines[count] = add_col
                self.write_md()

            if column_added:
                break

            count += 1

    def get_rows(self, resource_name):
        count = 0
        resource_name_row_start = 0
        resource_name_row_end = 0
        self.load_md()
        for line in self.all_lines:
            count += 1
            if line.startswith('|     '+resource_name):
                resource_name_row_start = count
                
                for no in range(count, len(self.all_lines)):
                    if self.all_lines[no].startswith('|     **'):
                        resource_name_row_end = no
                        break
                return resource_name_row_start, resource_name_row_end

    def add_checks(self, st_no, end_no, scraped_data):
        lines = list()
        self.load_md()
        for no in range(st_no, end_no):
            lines.append(dict({'line_no':no, 'line':self.all_lines[no]}))

        new_end_points = []
        for end_point in scraped_data:
            end_point_found = False
            for ele in lines:
                line_no = ele.get('line_no')
                line = ele.get('line')
                if line.startswith('|<sub>'):
                    ln = line.split('|')
                    split_module = ln[1].strip().split('<sub>')
                    module = split_module[-1].split('</sub>')[0]
                    
                    if end_point == {module, ln[2].strip()}:
                        ln = line.rstrip('\n')                                                          
                        add_col = ln + '  :white_check_mark:   |\n'                                     
                        self.all_lines[line_no] = add_col                                               
                        end_point_found = True                                                          
                        break

            if not end_point_found:
                new_end_points.append(end_point)
            for end_point in new_end_points:
                add_col = '|<sub>'+list(end_point)[0]+'</sub>                                                      |'+' '+list(end_point)[1]+'      '+ \
                                              '|  :heavy_minus_sign:   | :heavy_minus_sign:   | :heavy_minus_sign:   |  ' \
                                                                    ':heavy_minus_sign:   |  :heavy_minus_sign:   |  :heavy_minus_sign:   |  :white_check_mark:   |\n'
                line_no = lines[-1].get('line_no')
                self.all_lines[line_no] = self.all_lines[line_no]+add_col
                self.write_md()
                self.load_md()
                lines.append(dict({'line_no':line_no+1, 'line':self.all_lines[line_no+1]}))

    def main(self, new_version = True):
        print("------Initiating write to endpoints file--------")
        for ele in self.executed_files:
            resource = list(rel_dict.keys())[list(rel_dict.values()).index(ele)]
            formatted_resource_name = '**' + resource + '**'
            resource_names.append(formatted_resource_name)
        self.add_column(self.product_table_name, new_version)
        for resource_name in resource_names:
            webscraping_data = DataFromWebScraping(ele)
            data_returned_from_web_scraping = webscraping_data.data_scraped()
            st_no, end_no = self.get_rows(resource_name)
            self.add_checks(st_no, end_no, data_returned_from_web_scraping)
        print("-------Completed write to endpoints filr--------")


if __name__ == '__main__':
    executed_files = ExecuteFiles()
    print(executed_files)
    resources_from_textfile = LoadResourcesFromFile()
    val1 = input("Do you want to write data to CHANGELOG.md: ")
    if val1 == 'y' or 'yes':
        if executed_files is not None and len(executed_files) != len(resources_from_textfile):
            val3 = input("There are few failed resources, even then do you want to write data to CHANGELOG.md")
            if val3 == 'y' or 'yes':
                write_obj = WriteToChangeLog(executed_files)
                write_obj.write_data()
            else:
                pass
    val2 = input("Do you want to editendpoints-support.md: ")
    if val2 == 'y' or 'yes':
        read_md_obj = WriteToEndpointsFile('## HPE OneView', True, executed_files)
        read_md_obj.main()
