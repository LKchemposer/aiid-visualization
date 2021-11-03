# AI Incident Database

## Ideas

* Visualization of article counts over time, by taxonomies
* Timeline of the all incidents

* Visualization of all `indidents` and 
* Graph of all `incidents`

## Visualization of article counts over time

* **What is it?** Dashboard to look at the big picture of all incidents
* **Who is it for?** People who don't want to necessarily dive into the detailed incidents yet.
* **What problem does it solve?** AIID doesn't currently have a tool to look at the incidents big picture.
* **How is it going to work?** Users click on

### UX

* Version 1.0: static Tableau dashboard
* Future versions: web app?, separate page in the website?, automatically updated

* Basic
    - Article count vs. time (year) by:
        * Low number of options: `near miss`, `intent`, `severity`, `lives lost`, `harm type`, `harm distribution basis, infrastructure sectors`, `public sector deployment`, `level of autonomy`, `relevant AI functions`, `problem nature`
        * High number of options:
            * Methodology of separation: top 50% by count
    - Global map of incident

### Tech Specs

* Data
    - Incident
* Tooltips
    - Short description

* Filters
    - Harm

### To Do

* [ ] Data study
* [ ] 
