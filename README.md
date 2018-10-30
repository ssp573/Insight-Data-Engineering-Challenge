# Insight-Data-Engineering-Challenge
Submission for Insights Data Engineering Coding Challenge

Run the shell script as follows:
sh run.sh

There was a problem of field names and order being different for different csv files. So I used a user prompt to ask the user what the new names for the fields are if the defaults don't match the current fields.

The defaults are according to majority of the test inputs given and are as follows:

Status: CASE_STATUS

Working state: WORKSITE_STATE

Occupation: SOC_NAME

Whenever the field names are not the same as above, the user is repeatedly prompted for the substitute field names to use.
