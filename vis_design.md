# AI Incident Database

## Idea

* What is it? Timeline of all incidents over time
* Who is it for? First time users of AIID, people who want a broad survey of the incidents
* What problem does it solve? AIID doesn't currently have a tool to look at the big picture

### UX

* Version 1.0: observable notebook, d3
* Features
    - Timeline: Gantt chart of all incidents
    - Tooltip: shows details, links to report url, image?
        * Smaller tooltip (default): short description, dates
        * Click: expand to a larger tooltip
            * Details: dates, full description, harm, etc.
    - Zoomable: zooms to focus on a particular time frame
    - Filters: filters incidents by options
        * Options (to be reordered): near miss, intent, severity, lives lost, harm type, harm distribution basis, infrastructure sectors, public sector deployment, level of autonomy, relevant AI functions, problem nature
        * High-n options: technology purveyor, named entities?
            * Check membership
    - Sorts: sorts data
        * Options: time (default), popularity (number of reports), incident #
* Components
    - Timeline
    - Tooltip
    - Zoom
    - Filter
        * Filter transition
    - Sort

### Versioning

* [x] Timeline
* [ ] Tooltip
    - [x] v1.0: smaller tooltip, click to expand, some details
    - [ ] v1.1: all details
    - [ ] v1.2: visually appealing layout
* [ ] Zoom
    - [x] v1.0: zoomable
* [ ] Filter
    - [ ] v1.0: filterable, transition
* [ ] Sort
    - [x] v1.0: sortable, transition
        * Sorts: time, incident #
    - [ ] v1.1: sort by popularity
* [ ] Misc
    - [ ] v1.0: acknowledgements, code organization, code comments
    - [ ] v1.1: grid lines
