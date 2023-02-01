# WebAccess/DMP Documentation

Source code of docs.wadmp.com. Written in Markdown, using vuepress static site generator. Admin of the project: jan.svoboda@advantech.com 

## To install locally for adding content:

### Prerequisities:

* Install Node.js LTS version (currently 18) from https://nodejs.org/en/
* Note: when running into problems with openssl error (Error: error:0308010C:digital envelope routines::unsupported), on windows run this in cmd: 
```
set NODE_OPTIONS=--openssl-legacy-provider
```

### Install and run:

* Clone this repo
* To install dependencies, run this command in root folder of this repo
```
npm ci
```
* To run local server, run this command in root folder of this repo
```
npm run dev
```
* Access your local web on http://localhost:8080

> Note: Already added content (files, pages) reactively change in the browser, but the web is overall statically generated (front page, menus, sidebars), so when adding new content you need to re-run the generation of static content by stopping the dev server (ctrl + C) and run "npm run dev" again.

To contribute, update only markdown files in src folder! Then push to separate branch (for permission contact admin) and create a pull request. It will be reviewed, merged and built and published.

* To build (publish) your changes, run build before pushing your branch:
```
npm run build
```
> This creates production build files in the docs folder. Always commit both your changes in source files (src) and built content (docs). Note that by commiting the docs folder, the github action will fire and publish new version of production files in the docs folder!

## To contribute:

Anyone is allowed to contribute via pull requests. First, send your request to contribute to jan.svoboda@advantech.com, with your github account info (github account email or name). You will be then enabled to create the pull requests.


## Resources:

* Vuepress docs https://vuepress.vuejs.org/
* Markdown https://www.markdownguide.org/







