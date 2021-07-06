import jenkins
 
server = jenkins.Jenkins('https://15.212.166.183:443/', username='i3sqa', password='i3sqa123')

version = server.get_version()
print(version)

# Get all builds
#jobs = server.get_all_jobs(folder_depth=None)
#for job in jobs:
#    print(job['fullname'])