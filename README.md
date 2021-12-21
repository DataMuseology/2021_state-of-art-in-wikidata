# 2021_state-of-art-in-wikidata
2021 PFCH Final Project
Title: “The State of Art in Wikidata”
(with a limit)


My (perhaps over-ambitious) goal with this project was to perform a global survey of art work data in Wikidata through Python that queried, collected, and analyzed the properties associated with ALL the “instances of”(P31) “painting” (Q3305213) including all subclasses.  The hope of this project was to provide some utility to cultural heritage institutions in understanding best practices with data modeling and aligning application profiles for a more robust and universally usable art dataset in the sphere of linked data. The scripts of this project work in conjunction with each other through JSON to identify all the QID’s of items classified as “painting”/+ all subclasses, then request all the claim information(i.e. associated properties) of those QID’s from wikidata, and then output as an aggregate by property number and number of occurrence in the dataset.

I say “ambitious”  because it took multiple plans of attack to gather only a portion of the originally intended scope. At the time of this project, there were 566,444 items/ instances of painting/subclass of paintings, but the results of this project only consider 203,063 items in the analysis due to the considerable amount of time it took to pull all the claims.

[Data]: The main source of data was accessed through Wikidata’s SPARQL endpoint, Wikidata’s Query Service, and through the Special:EntityData API endpoint through respective python scripts.<br>
An example of each type of query straight in the browser:<br>
<ul>
<li>https://w.wiki/4aUb 
<li>https://www.wikidata.org/wiki/Special:EntityData/Q25986.json
</ul>


[Method]: Multiple steps comprise this workflow:<br>
wikidatawork.py<br>
<ul>
<li>Query and collect all the QID’s via query constructed through https://query.wikidata.org/
<li>Test the query using SPARQL in the web interface
<li>Creates and writes dictionary in JSON to dir 
<li>Output = qidsfull.json
</ul>

wikidata_painting _full.py<br>
<ul>
<li>Load in all the QIDs collected with JSON previously (qidsfull.json)
<li>Requests through Special:EntityData endpoint to query all the claims for each QID item (properties included) - one QID at a time
<li>Store as JSON dictionary (1 file per QID) in local dir called wikidata_q_data (Example: Q23946.json)
<li>Time module and  os.path.exists() to allow for stops and starts of script running. Also accounts for where left off and will check to see if already completed QID look up and file creation ---->Helpful In case of timeout error or need to stop bc 200k QIDs took MANY days!
<li>(Additional and multiple thanks to Matt Miller for his help with this script- many failed attempts had previously ensued with naive notions of getting all 500K QID claims in one go…)
</ul>

collect.py<br>
<ul>
<li>Retrieve all JSON files from wikidata_q_data dir with glob
<li>Load data with JSON
<li>Iterate through the JSON files to collect just the property claims data per QID file
<li>Aggregated to one dictionary with all property numbers and their occurrence (key-value pair)
<li>Sorted dictionary to highest value to to lowest
<li>Write to CSV for visualization
</ul>

Final steps<br>
<ul>
<li>Used https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all
  <ul>
    <li>To correlate the names (i.e. label) of the properties 
    <li>Understand current property utilization in Wikidata (i.e. count)
  </ul>
<li>Cleaned CSV, transposed data, added data from all properties
<li>Visualizations in Tableau Public
</ul>

[Conclusion]: Some interesting findings:<br>
<ul>
<li>For 203,063 items, 566 unique properties  were used in their claims
<li>Top 10 Highest usage (excluding “instance of” which all items had as a property claim):
  <ul>
    <li>collection
    <li>inventory number
    <li>location
    <li>creator
    <li>inception
    <li>height
    <li>width
    <li>made from material
    <li>title
    <li>copyright status
  </ul>
<li>It was interesting to note the properties that contained “ID”, which infer an effort of a particular institution to provide a unique identifier of an object in their collection. This particular claim can then serve as a vehicle to aggregate all items in a particular collection.
  <ul>
    <li>Additionally this is an optimal identifier for search
  </ul>
<li>There were 174 properties only used once in a claim and 52 properties used twice.
  <ul>
    <li>116 of those items had reference to “ID” in their property name, which could indicate either inconsistencies with Identification assignment
  </ul>


[Some barriers]: Wikidata doesn’t like it when you request hundreds of thousands of requests in succession. Weird, right? That necessitated adjustment to the plan of attack via the collection, retrieval, and storage of the Special:EntityData search results. Since it took a long time to request all the claim information for each of the 566,444 items, I made the decision to limit the claim collection to just 203,063 items (instances of “painting”).
Future iterations of this project will include completing the 500K survey, expanding the scope to all instances of “work of art” (Q838948) Wikidata items for similar analysis, and creating more robust code in the process. Additionally I would like to investigate the data modeling relationships between items tagged to a certain identifier ID, like comparing those with “RKDimages ID” (P350) to “The Met object ID”(P3634), for example.

This project has definitely served as my foray into programmatic inquiry. I look forward to further expanding this project (and skillset) to “instances of” other entities in the Wiki-verse in the hopes of creating a utility to understand current state modeling (by popularity) activities within the linked open data realm


Image attribution: 
"Jacob Cornelisz. van Oostsanen Painting a Portrait of His Wife"<br>
Artist: Dirck Jacobsz.<br> 
Date: 1550<br> 
<a href="https://commons.wikimedia.org/wiki/File:Dirck_Jacobsz_-_Jacob_Cornelisz._van_Oostsanen_Painting_a_Portrait_of_His_Wife_-_Google_Art_Project.jpg">Retrieved</a> 2021<br> 

With edits by Jessika Davis
