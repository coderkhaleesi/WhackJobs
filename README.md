# WhackJobs

First, let's determine the aim of the website -> Let anyone search for jobs across different job portals. The ones I am thinking of supporting right now are - LinkedIn, Indeed, and Stack Overflow.
Since it's a hobby app, I do not want to get jobs everytime someone searches on the app. So, I will retrieve jobs, keep them in a database and run a Jenkins/cron job to update the database every week. Job postings that are older than 2 months will be deleted.
The main focus of this app is to find jobs that are related to ML, Python, DL, Data Science, Data Analytics, Product Management. I am not planning to include jobs from all the sectors.
The fields that will be displayed are - Job Title, Salary (if available), Job Description, Location, Visa Sponsorship, Link to Apply, Additional insights if available.
Another page -> Job Insights (How many total jobs with a particular title? Where are the most jobs?)
