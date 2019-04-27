# ufo.github.io
UFO sightings throughout the world

Objectives:
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
