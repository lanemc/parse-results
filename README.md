# Check Links and Parse Results

This repository contains a bash script that runs broken-link-checker and subsequently parses the results into a csv and/or index.html file that can be displayed using a web server. It was specifically built to be used with https://math.umn.edu; however there are opportunities to extend and refactor for flexibility which will be discussed in a later section.

## Dependencies

<ul>
  <li><a href="https://www.npmjs.com/package/broken-link-checker">broken-link-checker (blc)</a></li>
  <li>python2.7</li>
  <li>pandas</li>
</ul>

## Instructions

Run the bash script and wait for it to finish. You can view the results in the csv or html file. 

## Refactoring

A file could be created that would contain a list of dictionaries that contain the links to filter out when parsing the results for a specific site. Then, a specific site could be called from the bash script and the parser would be able to identify which filter list to reference based on the results.
