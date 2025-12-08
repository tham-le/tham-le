#!/usr/bin/env python3
"""
Generate 3D contribution graph from GitLab profile
Fetches public contribution calendar from GitLab and saves as JSON
Then use github-profile-3d-contrib with custom data
"""

import requests
import json
import sys
from datetime import datetime

def fetch_gitlab_contributions(username):
    """Fetch contribution data from GitLab profile page"""
    url = f"https://gitlab.com/users/{username}/calendar.json"
    
    try:
        print(f"Fetching GitLab contributions from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # GitLab returns data in format: {"2024-12-08": 5, ...}
        total = sum(data.values())
        print(f"Found {total} contributions across {len(data)} days")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitLab data: {e}")
        sys.exit(1)

def save_contributions(data, output_file="gitlab-contributions.json"):
    """Save contribution data to JSON file"""
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved contributions to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate-gitlab-3d.py <gitlab-username>")
        print("Example: python3 generate-gitlab-3d.py tham-le")
        sys.exit(1)
    
    username = sys.argv[1]
    contributions = fetch_gitlab_contributions(username)
    save_contributions(contributions)
    
    print("\nNext steps:")
    print("1. The GitLab contribution data has been saved")
    print("2. Unfortunately, there's no automated GitHub Action for GitLab")
    print("3. You can manually create a visualization or use GitLab's built-in calendar")

