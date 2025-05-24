# Program to demonstrate integration with GitHub to fetch the 
# details of commit dates with count on Kubernetes Github repo.

import requests

# URL to fetch commits from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/commits'

# Make a GET request to fetch commit_dates data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    commits = response.json()

    # Create an empty dictionary to store commit dates and their counts
    commit_dates = {}

    # Iterate through each commits and extract the commit dates
    for commit in commits:
        # Extract date from the timestamp
        commitor = commit['commit']['committer']['date'].split("T")[0]
        if commitor in commit_dates:
            commit_dates[commitor] += 1
        else:
            commit_dates[commitor] = 1

    # Display the dictionary of commit dates and their counts
    print("Commit Date and Counts:")
    for commitor, count in commit_dates.items():
        print(f"{commitor}: {count}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
