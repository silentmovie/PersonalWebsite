# Bohan's Personal Website
https://math.dartmouth.edu/~bzhou

## Moving into production.
There are two special branches in this repository: the `staging` branch and the `production` branch.  The staging branch is used to create the website displayed at [https://math.dartmouth.edu/~bzhou/staging](https://math.dartmouth.edu/~bzhou/staging).  Similarly, the production branch is used to create the main website at [https://math.dartmouth.edu/~bzhou](https://math.dartmouth.edu/~bzhou).   The `staging` branch should be used to test the website before moving it into `production`.

Every two minutes, a script on gauss.dartmouth.edu checks to see if there have been changes to the `staging` branch.   If there are changes, the latest commit is pulled and Jekyll is run to build the site, which is then displayed at [https://math.dartmouth.edu/~bzhou/staging](https://math.dartmouth.edu/~bzhou/staging).    

Every hours, the same process is performed for the `production` branch.

It is relatively straightforward to add additional testing branches if we think that will be helpful later on.

## Suggested workflow.
1. Clone this repository.
2. Using the production branch as a starting point, create a new branch (e.g, `mparno`) for your changes.
```
git checkout production
git checkout -b mparno
```
3. Pull in the latest changes from the production branch
```
git pull origin staging
```
4. Add any new content to the website, testing locally (see local instructions below).  It is possible to backup your local changes by pushing your local branch to github with `git push`.
5. Once the new content looks as you would expect on your machine, pull the changes into the `staging` branch for testing on Gauss.  If your branch exists on GitHub, this would involve something like
      ```
      git checkout staging
      git pull origin mparno
      git push
      ```
6. Once the new content looks as you would expect on Gauss, pull the contents of the `staging` branch into `production`:
      ```
      git checkout production
      git pull origin staging
      git push
      ```

## How to add a new blog page.
1. Add a local markdown file in the folder `_posts` starting with `yyyy-mm-dd-` ending with `.md`.
2. Include the front matter by
      ```
      ---
      layout: post
      author: yourname
      image-slider: the relative link of the image you want to show in the homepage in the format: /assets/images/lead.JPG
      excerpt: the keywords you want to show under the image in the homepage
      categories: blog
      ---
      ```
3. [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/).
4. Follow the above workflow for git.

## How to add a new person to the People page.
1. Check out the `staging` branch (or your own branch)
1. Add a headshot image to the `assets/images` folder.  Try to keep the filesize under 1 MB.
1. Add the person's name, the name of the image file, and some text describing their position to `_data/people.yml`.   Copy one of the other entries to get started.   Indentation is important (use spaces).   
1. Commit and push your changes to the `staging` branch on GitHub.   If everything is working correctly, a few minutes later you should see the update on the [staging website](https://math.dartmouth.edu/~bzhou/staging/People.html).
1. Once everything looks good on the staging website, contact someone with write privelages on the `production` branch (e.g., Matt or Yoonsang) to update the [main website](https://math.dartmouth.edu/~bzhou/staging/People.html).


## Testing Locally
The SIMDA website is built from the markdown files in this repository using the [Jekyll](https://jekyllrb.com/) static site generator.   

#### Installing Jekyll in a conda environment
1. Create a new environment for Jekyll:
```bash
conda create --name simda-web
```
2. Install jekyll in the new environment:
```
conda activate simda-web
conda install -c conda-forge rb-jekyll compilers
```

#### Building the website with jekyll
Now you can `cd` into the `simda/website` folder and run jekyll:
```
cd website
bundle install
bundle exec jekyll serve
```
You should now be able to use a browser to view a test version of the website.  Typically, this will be at http://127.0.0.1:4000
