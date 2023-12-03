import subprocess
import time

# Message
message =  'Qoute added'

# Function to commit changes
def commit_changes(message):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])

# Function to push changes
def push_changes():
    subprocess.run(['git', 'push'])

# Example: Auto commit every hour
while True:
    commit_message = message
    commit_changes(commit_message)
    push_changes()
    print("Changes committed and pushed to the repository.")
    
    # Wait for an hour before the next commit
    time.sleep(20)  # 3600 seconds = 1 hour
