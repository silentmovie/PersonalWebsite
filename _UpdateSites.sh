#!/bin/bash

# USAGE:
# This script simply copies the contents of the _site folder to the correct folder on math.dartmouth.edu.
# For someone with a username on math.dartmouth.edu, the following command will copy the website:
#     ./UpdateSites.sh <username>
#

# Change permissions so that everything is group access
chmod -R g+w _site/*

# Update the site on math.dartmouth.edu
#rsync -av _site/ $1@math.dartmouth.edu:/home/muri/public_html
rsync -av --no-t _site/ $1@math.dartmouth.edu:/home/muri/public_html
