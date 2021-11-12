# AI Incident Database

## Idea

* What is it? Timeline of all incidents over time
* Who is it for? First time users of AIID, people who want a broad survey of the incidents
* What problem does it solve? AIID doesn't currently have a tool to look at the big picture

## UX

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

### Option order

* Sorts
    1. Time
    2. Incident #
    3. Number of reports - v1.1
* ColorBy options
    1. Severity
    2. Intent
    3. Level of autonomy
    4. Nature of end user
    5. Near miss?
    6. Lives lost?
    7. Public sector deployment? 
* Tooltip
    1. Date(s) - beginning date, ending date
    2. Short description
    3. AI applications
    4. Sector of deployment
    5. Harm type
    6. Harm distribution basis
* Full tooltip
    1. Date(s)
    2. Location
    3. Full description
    4. System developer
    5. Physical system
    6. Data inputs
    7. Laws implicated
    8. Financial cost
    9. Problem nature
    10. Relevant AI function

<!-- AI system description -->

## Versioning

* [x] Timeline
* [ ] Tooltip
    - [x] v1.0: smaller tooltip, click to expand, some details
    - [x] v1.1: all details
    - [ ] v1.2: visually appealing layout
* [x] Zoom
    - [x] v1.0: zoomable
* [ ] Filter
    - [x] v1.0: filterable, transition
* [ ] Sort
    - [x] v1.0: sortable, transition
        * Sorts: time, incident #
    - [ ] v1.1: sort by popularity
* [ ] Misc
    - [x] v1.0: acknowledgements, code organization, code comments
    - [ ] v1.1: grid lines, dynamic sizing to fit any n bars (as dataset grows in size)

## Columns

* incident - 96
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
* financial_cost [nan 'Short term: $1 trillion   unclear of long-term impact' '$528.00' '3.7M Ether ($70M at the time)']
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