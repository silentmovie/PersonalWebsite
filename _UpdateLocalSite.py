# Usage:
# python _UpdateLocalSite.py <branch>
#
# Description:
# Updates the local copy of one branch of the website repository.
# If any changes have been made to the site, this script will then
#  run Jekyll to build the static HTML and then copy the results
# site and copy the static HTML into the public_html or
# public_html/staging folders as necessary.

import datetime
import dateutil.parser
import subprocess
import sys
import os

assert(len(sys.argv)>=2)

force_update = False
if(len(sys.argv)==3):
    force_update = True

branch_name = sys.argv[1].strip()

base_path = '/home/mparno/muri_website'
os.chdir(base_path)

# Checkout the branch of interest
subprocess.run(['git', 'checkout', branch_name])

# Check the time of the latest commit we currently have
res = subprocess.run(['git', 'show', '--format="%aI"', '--no-patch'],  stdout=subprocess.PIPE)
old_time = dateutil.parser.isoparse(res.stdout.strip()[1:-1])

# Pull down the latest version of this branch
subprocess.run(['git', 'pull'], stdout=subprocess.PIPE)

# Get the time of the latest commit after the pull
res = subprocess.run(['git', 'show', '--format="%aI"', '--no-patch'], stdout=subprocess.PIPE)
new_time = dateutil.parser.isoparse(res.stdout.strip()[1:-1])

# If an update has occurred or the branch hasn't been built and
# copied to public_html, then we need to run Jekyll
if(branch_name=='production'):
    dest_path = '/home/muri/public_html/'
else:
    dest_path = '/home/muri/public_html/'+branch_name

dest_exists = os.path.exists(dest_path)
run_jekyll = (not dest_exists) | (new_time != old_time)
if(force_update):
    run_jekyll = True

if(run_jekyll):
    print('Rebuilding ' + branch_name + ' site.')

    if(not dest_exists):
        os.mkdir(dest_path)


    if(branch_name!='production'):
        old_url_string = 'baseurl: "/~muri"'
        new_url_string = 'baseurl: "/~muri/%s"'%branch_name

        subprocess.run(['mv', '_config.yml', '_old_config.yml'])

        with open('_old_config.yml', 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(old_url_string, new_url_string)

        # Write the file out again
        with open('_config.yml', 'w') as file:
            file.write(filedata)

    # Run Jekyll
    subprocess.run(['bundle', 'install'])
    env = {
    **os.environ,
    "JEKYLL_ENV": str("production"),
    }
    subprocess.Popen(['bundle exec jekyll build'], shell=True, env=env).wait()

    # Copy the results in _site to a folder in public_html
    subprocess.run('cp -r _site/* %s'%dest_path, shell=True)

    # Reset the config file if we changed it.
    if(branch_name!='production'):
        subprocess.run(['mv', '_old_config.yml', '_config.yml'])

else:
    print('Site is up to date.')
