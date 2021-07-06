#!/usr/bin/python

import time, os, re, sys
from subprocess import Popen, PIPE
from pprint import pprint
import platform

# Currently supported WebDriver implementations are Firefox, Chrome, Ie and Remote
from selenium import webdriver

# Interacting with the RETURN KEY
from selenium.webdriver.common.keys import Keys
### user inputs ####
username = "<AD_username>"
password = "<AD_password>"
sudo_password = "<system_password>"
build = input("Enter the version number : ")
build_type = input("Enter type of build.. iso/tar..? ")
build_type = build_type.strip()
version = "release-" + str(build)
build_info = {}

# Creating a web driver firefox instance
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

############### LOGIN PAGE ############
# With the get method we go to the webpage in the url given
driver.get("https://dev.pulsesecure.net/bamboo/browse/DOCKER")
if driver.find_element_by_xpath("//*[@id='fieldLabelArea_loginForm_os_username']"):
	driver.find_element_by_xpath("//*[@id='loginForm_os_username']").send_keys(username)
	driver.find_element_by_xpath("//*[@id='loginForm_os_password']").send_keys(password)
	driver.find_element_by_xpath("//*[@id='loginForm_save']").click()
else:
	print "Username not found"
print ">>>> Logged in bamboo successfully...."

############# Navigating to PulseOne installer builds page #########
driver.find_element_by_xpath("//*[@id='viewBuild:DOCKER-BPOI']").click()
print ">>>> Clicked PulseOne build installer"

########### selecting the branch ###########
driver.find_element_by_xpath("//*[@id='branch-selector']").click()

bs_list = driver.find_elements_by_xpath("//div[@class='aui-inline-dialog-contents contents']/ul/li") 
for elem in bs_list:
	ver = elem.find_element_by_xpath(".//span/a").text
	if ver.encode('ascii', 'ignore') == version:
		elem.find_element_by_xpath(".//span/a").click()
		break

########### confirm whether we are in expected build page or not ########
if driver.find_element_by_xpath("//span[@class='plan-branch-name']").text.encode('ascii', 'ignore') == version:
	print ">>>> Now we are in required build version page.."
else:
	print "ALERT: We are in wrong page.. Selecting the branch again.."
	driver.find_element_by_xpath("//*[@id='branch-selector']").click()

	for elem in bs_list:
        	ver = elem.find_element_by_xpath(".//span/a").text
        	if ver.encode('ascii', 'ignore') == version:
                	elem.find_element_by_xpath(".//span/a").click()
                	break



###########################################
for index in range(1,10):
	gen_xpath = "//*[@id='buildResultsTable']/tbody/tr["+str(index)+"]/td[1]/a"
	if driver.find_element_by_xpath("//*[@id='buildResultsTable']/tbody/tr["+str(index)+"]/td[1]/a").get_attribute("title").encode('ascii', 'ignore') == "Successful":
		build_number = driver.find_element_by_xpath("//*[@id='buildResultsTable']/tbody/tr["+str(index)+"]/td[1]/a").text.encode('ascii', 'ignore')
		print ">>>> Latest P1 ",version," successful build number is : ", build_number
		driver.find_element_by_xpath("//*[@id='buildResultsTable']/tbody/tr["+str(index)+"]/td[1]/a").click()
		break

latest_build = "Build " + build_number
build_info["build_number"] = latest_build    ##### Storing build number in dictionary ######

if driver.find_element_by_xpath("//*[@class='has-branch-selector']").text.encode('ascii', 'ignore') == latest_build:
	print ">>>> Now we are in ", version," ",latest_build, " page"

########### Fetch P1 ISO and upgrade bundle URL ###########
iso_url = driver.find_element_by_xpath("//*[@id='artifact-ISO Installer']").get_attribute("href").encode('ascii', 'ignore')
upgrade_bundle = driver.find_element_by_xpath("//*[@id='artifact-pulse-one-upgrade-bundle']").get_attribute("href").encode('ascii', 'ignore')

build_info["iso_url"] = iso_url
build_info["upgrade_bundle"] = upgrade_bundle
print ">>>> Fetched the build url successfully..."
############## LOGOUT PAGE ############
driver.find_element_by_css_selector(".aui-avatar-inner>img").click()
driver.find_element_by_xpath("//*[@id='log-out']").click()
print ">>>> Logout bamboo successful..."
driver.quit()

############## Downloading the build from bamboo ##############
captured_build = re.findall('\d+', build_number)

if build_type == "iso":
	output_filename = "alpine-pulseone_" + str(build) + "-" + captured_build[0] + ".iso"

	if not os.path.isfile(output_filename):
		print ">>>>>> Downloading the iso build <<<<<<"
		result = os.system("curl -u " + username + ":" + password + " -o " + output_filename + " -k -g " + build_info["iso_url"])
		if result == 0:
			print ">>>> File : ",output_filename," downloaded successfully.."
		else:
			print "Failed to download the file"
	else:
		print "%s File already exists.. Skipping download.." % output_filename
elif build_type == "tar":
	output_filename = "pulse-one_" + str(build) + "-" + captured_build[0] + ".tgz"
	os.chdir('/Users/venkatesh/Documents/HTTP_server')
        if not os.path.isfile(output_filename):
                print ">>>>>> Downloading the upgrade bundle <<<<<<"
                result = os.system("curl -u " + username + ":" + password + " -o " + output_filename + " -k -g " + build_info["upgrade_bundle"])
                if result == 0:
                        print ">>>> File : ",output_filename," downloaded successfully in ", os.getcwd()
                else:
                        print "Failed to download the file"
        else:
                print "%s File already exists.. Skipping download.." % output_filename
	sys.exit()
else:
	sys.exit("Error: Invalid build type.. Exiting")

############# Building USB installer in mac os ################
if platform.system() == "Darwin":
	print ">>>>>>>> Building USB installer <<<<<<<<"
	command1 = "diskutil list".split()
	console = Popen(command1, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	out, inp = console.communicate()
	partition_match = re.search('([a-z0-9A-Z\/]+)\s+\(external', out)
	if partition_match is not None:
	        partition = partition_match.group(1)
	        parts = re.match('(\/\w+\/)(\w+)', partition)
	        part1 = parts.group(1)
	        part2 = parts.group(2)
	else:
	        print "Failed: External USB drive not inserted.."
		sys.exit("exiting...")

	unmount_command = "diskutil unmountdisk " + partition
	command2 = unmount_command.split()
	console = Popen(command2, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	out, inp = console.communicate()
	unmount_output = re.search('^unmount.*successful$', out, re.I)
	if unmount_output is None:
	        print "Failed to unmount USB drive partition"

	mount_command = "sudo -S dd if=" + output_filename + " of=" + part1 + "r" + part2 + " bs=5m"
	command3 = mount_command.split()
	console = Popen(command3, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	out, inp = console.communicate(sudo_password + '\n')

	eject_command = "diskutil eject " + partition
	command4 = eject_command.split()
	console = Popen(command4, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	out, inp = console.communicate()
	eject_output = re.search('^disk.*ejected$', out, re.I)
	if eject_output is None:
	        print "Failed to eject USB drive partition"

	print ">>>> Latest P1 %s build is mounted on USB drive" %version
else:
	print "Mount the build onto USB manually.."
