# Devfolio Hackathon Data Downloader

## Introduction

Welcome to the Devfolio Hackathon Data Downloader! Our tool addresses the challenge of accessing comprehensive participant data on Devfolio. By allowing organizers to download data for all participants in a convenient CSV format, we provide a comprehensive solution for managing hackathon data effectively.

## Motivation

Hackathons bring together diverse talents to innovate and create solutions to real-world problems. Access to comprehensive participant data is crucial for smooth communication and event management. Our tool aims to empower organizers with the tools they need to manage events efficiently, maximizing the impact of hackathon events worldwide.

# Devfolio Data Scraper

This Python script helps you retrieve participant data from Devfolio hackathon dashboards and save it into CSV format.

## Instructions

1. Login to your Devfolio account as the organizer of the hackathon.
2. Click on your profile name and select "Organize a Hackathon" to open the dashboard.
3. Navigate to the "Past Hackathons" section and click on "Open Dashboard" for the desired hackathon.
4. In the dashboard, go to the "Review" section to view all participants.
5. Right-click and select "Inspect" to open the browser developer tools.
6. In the developer tools, switch to the "Network" tab and filter requests by selecting only "Fetch/XHR".
7. Press `Ctrl + R` to refresh the page and capture network requests.
8. Look for the request with the name "participants?limit..." which contains the participant data.
9. Right-click on this request and open it in a new tab.
10. You will now have access to the data of the first 200 participants. Save this data into a JSON file.
11. Run the provided Python script, specifying the path to the JSON file and the desired location to save the CSV file.
12. To retrieve data for the next 200 participants, increment the `page` parameter in the URL by 1. Change [ &page=1] to [ &page=2] in url

## Usage

### Method 1: Manual JSON Copy-Paste

Manually copy and paste the participant data from the browser into a JSON file. Then, specify the path to this JSON file in the script provided.This was quick as the json data is present on the system.

### Method 2: Using API
Update the provided Python script with the direct API URL to retrieve data. This may take some time but u can do this using 'requests' library.  


## Notes
- Ensure that the JSON file starts with a `{` and not `\\`, remove if any comments at the beginning.
- Devfolio's API supports retrieving data for up to 200 participants at a time. To get data for more participants, you need to paginate by changing the `page` parameter in the URL.
- The parameters I've considered are as per the General needs in case u want to extract more data adjust the parameters in the script accordingly. 

