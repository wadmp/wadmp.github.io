# WebAccess/DMP Documentation

Source code of docs.wadmp.com. Written in Markdown, using vuepress static site generator. Admin of the project: jan.svoboda@advantech.com 

## To install locally for adding content:

### Prerequisities:

* Install Node.js LTS version (currently 16) from https://nodejs.org/en/

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

* To build your changes before pushing your branch:
```
npm run build
```
> This creates production build files in the docs folder. Always commit both your changes in source files (src) and built content (docs)

## To contribute:

Anyone is allowed to contribute via pull requests. First, send your request to contribute to jan.svoboda@advantech.com, with your github account info (github account email or name). You will be then enabled to create the pull requests.


## Resources:

* Vuepress docs https://vuepress.vuejs.org/
* Markdown https://www.markdownguide.org/







