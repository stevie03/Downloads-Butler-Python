# Automated Downloads Organizer

This is a background-running Python automation tool that keeps the Windows Downloads folder clean. The program monitors the specified path and organizes files into categories (Images, Documents, Music, Others) based on their extensions.

# Features
**Automated organization:** Scans the folder every 2 hours (customizable).
**Windows integration:** Can be configured with Task Scheduler for automatic invisible startup.

# Installation and usage
1. Copy the `rendszerezo.py` file.
2. Modify the `folder_path` variable to your own user path.
3. Run it in the terminal: `python rendszerezo.py`
4. (Optional) Configure it in Windows Task Scheduler for continuous, invisible execution.
