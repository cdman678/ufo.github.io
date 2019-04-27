# ufo.github.io
UFO sightings throughout the world

<h4><b>Objectives</b></h4>
 <ul>
     <li>Clean the dataset, removing all irrelevant attributes and fixing the location attributes <br></li>
     <li>Create a MySQL database from the UFO sightings repository <br></li>
     <li>Break the dataset into a normalized form <br></li>
     <li>Run analysis on the dataset <br></li>
     <li>Create Heatmap with the given locations<br></li>
     <li>Create Graphs to represent the results of our queries<br></li>
     <li>Create Word Clouds for UFO descriptions and shapes</li>
</ul>
<h4><b>Dataset</b></h4>
<ul>
    <li>The original dataset is from the National UFO Reporting Center and can be found <a href="http://www.nuforc.org/webreports.html">here</a> <br> </li>
    <li>The scrubbed dataset that we're using can be found <a href="https://github.com/planetsig/ufo-reports">here</a> <br></li>
    <li>We have removed the attribute that listed the date each sighting was uploaded considering it's irrelevant to the study<br></li>
    <li>We cross referenced the latitude and longitude for each data entry and updated the correct city, state, and country</li>
</ul>
<h4><b>Tools</b></h4>
<ul>
    <li>Python - Used a Python library to go through each coordinate in the data set and return the correct city, state, and country <br> </li>
    <li>MySQL - Used to manipulate data from our dataset as well as to run queries</li>
    <li>MySQL Server - Dedicated server running MySQL Server to store the dataset<br></li>
    <li>HTML/Bootstrap - This website was created using HTML in addition to Bootstrap<br></li>
    <li>JavaScript - Connecting to the Google Map API, creating the graphs, making word clouds and other website functions<br></li>
</ul>


<div style="height: 60px;padding-left: 20px; padding-bottom: 15px" class="panel-heading">Proposal</div>
<div class="panel-body">
    <h4><b>Introduction</b></h4>
    <p>Initially, we brainstormed and thought about what might make an interesting dataset to visualize and determine a trend by looking at a large amount of data. We ended up settling on using a dataset from the National UFO Reporting Center comprised of documented cases around the world of UFO sightings. This data included the location sighted (state, country, longitude and latitude), the shape of the sighted object, the date and time of the sighting, and a brief description of the event. With around 80,000 entries of UFO sightings, we knew we had a large amount of data to use to discover any trends and similarities in sightings whether it be similar object shapes, similar descriptions of events, or even sightings located in close proximity of each other.</p>
    <p>By importing this dataset into a MySQL server, this allowed us to manipulate the data in such a way that made it easily accessible for certain trends and categories of data to be viewed. For example, with a simple MySQL query, we were able to easily see how many sightings have been recorded in the state of Texas by the National UFO Reporting Center website. Other useful queries show metrics like the amount of sightings in the US vs non-US countries, the most commonly sighted shape of objects, and even popular words that people tend to use in describing the event of a UFO sighting.</p><br>
    <h4><b>Questions</b></h4>
    <p>With a dataset this large, it was easy to start wondering what kind of trends could occur by looking at the documented sightings seen over the years. Some of the top questions are as follows:
    <ul>
        <li>How many recorded UFO sightings in the US?</li>
        <li>What's the most common shape of a sighted object?</li>
        <li>What state has the most recorded sightings of UFOs?</li>
        <li>What country has the most recorded sightings of UFOs?</li>
        <li>What city has the most recorded sightings of UFOs?</li>
    </ul>
</p><br>
    <h4><b>Project Plan</b></h4>
    <p>Steps to Implement Our Project:</p>
    <ul>
        <li>Conceptualize the dataset into a Data Model</li>
        <li>Normalize the dataset to 3NF</li>
        <li>Create a Relational Schema of the dataset</li>
        <li>Create a Logical Data Model of the dataset</li>
        <li>Create a Physical Data Model of the dataset</li>
        <li>Insert the dataset into separate tables in a MySQL database using the created schemas</li>
        <li>Remove unnecessary, incomplete or irrelevant data from the dataset</li>
        <li>Cross reference latitude and longitude locations using Python library</li>
        <li>Manipulate the dataset and perform queries to determine metrics and trends</li>
        <li>Create a heatmap visualization of queries based on location of sightings</li>
        <li>Create word cloud visualizations of queries based on object shapes and descriptions</li>
        <li>Create graph visualizations of queries based on top sighting metrics</li>
