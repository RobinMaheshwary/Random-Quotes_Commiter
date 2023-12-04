import subprocess
import time

# Message
message =  'Qoute added'

# Function to commit changes
def commit_changes(message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])

# Function to push changes and sync
def push_and_sync():
    subprocess.run(['git', 'push'])
    subprocess.run(['git', 'fetch', 'origin'])
    subprocess.run(['git', 'merge', 'origin/main'])  # Replace "main" with your branch name if different


# Example: Auto commit every hour

while True:
    commit_message = message
    commit_changes(commit_message)
    push_and_sync()
    print("Changes committed, pushed, and synchronized with the repository.")

    # Wait for an hour before the next commit
    time.sleep(5)  # 3600 seconds = 1 hour
