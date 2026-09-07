from datetime import datetime
from pathlib import Path

# Get today's date
today = datetime.now()

year = today.strftime("%Y")
month = today.strftime("%m")
date = today.strftime("%Y-%m-%d")

# Create the directory:
# daily/YYYY/MM/
log_directory = Path("daily") / year / month
log_directory.mkdir(parents=True, exist_ok=True)

# Today's log file
log_file = log_directory / f"{date}.md"

# Don't overwrite an existing log
if log_file.exists():
    print(f"Daily log already exists: {log_file}")
else:
    content = f"""# Daily Developer Log - {date}

## 🎯 What I Worked On

- 

## 📚 What I Learned

- 

## 💻 Code / Projects

- 

## 🧠 Problems I Solved

- 

## 🔍 Things I Need to Improve

- 

## 🚀 Tomorrow

- 

"""

    log_file.write_text(content, encoding="utf-8")
    print(f"Created daily log: {log_file}")