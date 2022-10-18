#!/bin/bash

docker run --rm \
   -p 4000:4000 \
   --volume="$PWD:/srv/jekyll" \
  -it jekyll/minimal \
  bash

# Once inside container, run bundle install; bundle exec jekyll build
