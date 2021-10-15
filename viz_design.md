# AI Incident Database

## Ideas

* Visualization of article counts over time, by taxonomies
* Timeline of the all incidents

* Visualization of all `indidents` and 
* Graph of all `incidents`

<div class='tableauPlaceholder' id='viz1634284175623' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NY&#47;NYT_2&#47;README&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NYT_2&#47;README' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NY&#47;NYT_2&#47;README&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1634284175623');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='610px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>


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
