# WhackJobs

First, let's determine the aim of the website -> Let anyone search for jobs across different job portals. The ones I am thinking of supporting right now are - LinkedIn, Indeed, and Stack Overflow.

Since it's a hobby app, I do not want to GET jobs everytime someone searches on the app. So, I will retrieve jobs, keep them in a database and run a Jenkins/cron job to update the database every week. Job postings that are older than 2 months will be deleted.

Also, keep a track of what user searches and then update the database with those searches.

The main focus of this app is to find jobs that are related to ML, Python, DL, Data Science, Data Analytics, Product Management. I am not planning to include jobs from all the sectors.

The fields that will be displayed are - Job Title, Salary (if available), Job Description, Location, Visa Sponsorship, Link to Apply, Additional insights if available.

Another page -> Job Insights (How many total jobs with a particular title? Where are the most jobs?)


##Step 1 - Let's start by determining the stack. I am using Python Flask for backend development.

First, I want to GET all jobs from different platforms and save them in a database. Also, schedule this job for every week preferably using Jenkins.

Since to access LinkedIn data using an API, I need to join their developer partner program, I decide to scrape the data.

pip3 install ipython 
pip3 install selenium  
pip3 install time 
pip3 install parsel
pip3 install csv

https://stackoverflow.com/questions/31248804/is-it-possible-to-locate-element-by-partial-id-match-in-selenium

https://selenium-python.readthedocs.io/navigating.html

