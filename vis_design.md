# AI Incident Database

## Idea

* What is it? Timeline of all incidents over time
* Who is it for? First time users of AIID, people who want a broad survey of the incidents
* What problem does it solve? AIID doesn't currently have a tool to look at the big picture

## UX

### 1.0: observable notebook, d3

* Features
    - Timeline: Gantt chart of all incidents
    - Tooltip: shows incident details
        * Small tooltip (default): short description, dates
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

### 1.5: incorporate incident data

* Features
    - Timeline: reports plotted along incident data
    - Tooltip: reports show report details, links to news site url, image?
        * Small tooltip: title, date
        * Full tooltip 
    - Misc: gridlines

### Option order

* Sorts
    01. Time
    02. Incident #
    03. Number of reports - v1.1
    04. All colorBy options
* ColorBy options
    01. Severity
    02. Intent
    03. Level of autonomy
    04. Nature of end user
    05. Near miss?
    06. Lives lost?
    07. Public sector deployment? 
* Tooltip
    01. Date(s) - beginning date, ending date
    02. Short description
    03. AI applications
    04. Sector of deployment
    05. Harm type
    06. Harm distribution basis
* Full tooltip
    01. Date(s)
    02. Location
    03. Full description
    04. System developer
    05. Physical system
    06. Data inputs
    07. Laws implicated
    08. Financial cost
    09. Problem nature
    10. Relevant AI function

<!-- AI system description -->

## Versioning

* [x] Timeline
* [ ] Tooltip
    - [x] v1.0: smaller tooltip, click to expand, some details
    - [x] v1.1: all details
    - [x] v1.2: visually appealing layout
* [x] Zoom
    - [x] v1.0: zoomable
* [x] Filter
    - [x] v1.0: filterable, transition
* [x] Sort
    - [x] v1.0: sortable, transition
        * Sorts: time, incident #
    - [x] v1.1: sort by popularity, 
* [ ] Misc
    - [x] v1.0: acknowledgements, code organization, code comments
    - [x] v1.1: grid lines
    - [x] Dynamic sizing to fit any n bars (as dataset grows in size)
    - [ ] Hovering on legend shows definition

## Columns

* incident_id - 96
* annotator - [1 2 3 4 6 5]
* annotation_status - ['6. Complete and final' '3. In peer review' '4. Peer review complete']
* reviewer - [5 6 2 3]
* quality_control - [False True]
* full_description - 96
* short_description - 96
* beginning_date - 71
* ending_date - 66
* location - 58
* near_miss ['Harm caused' 'Unclear/unknown' 'Near miss']
* named_entities list
* technology_purveyor list
* intent ['Accident' 'Unclear' 'Deliberate or expected']
* severity ['Moderate' 'Critical' 'Severe' 'Minor' 'Negligible' 'Unclear/unknown']
* lives_lost [False  True]
* harm_distribution_basis list
* harm_type list
* infrastructure_sectors list
* financial_cost [nan 'Short term: \$1 trillion unclear of long-term impact' '\$528.00' '3.7M Ether (\$70M at the time)']
* laws_implicated 14
* ai_system_description 89
* data_inputs 81
* system_developer 54
* sector_of_deployment 13
* public_sector_deployment [False True]
* nature_of_end_user [nan 'Expert' 'Amateur']
* level_of_autonomy ['Unclear/unknown' 'High' 'Medium' 'Low' nan]
* relevant_ai_functions list
* ai_techniques 64
* ai_applications list
* physical_system list
* problem_nature list
* publish [True False]
