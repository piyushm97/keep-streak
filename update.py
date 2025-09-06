from datetime import datetime

# Update one file with today's date
with open("status.md", "w") as f:
    f.write(f"Last updated on {datetime.utcnow()} UTC\n")
