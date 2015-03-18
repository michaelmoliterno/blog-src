Title: How to set up a python Cron job
Date: 2015-03-11 14:33
Category: blog
Tags: python, cron job
Author: Michael Moliterno
Summary: I recently wanted to set up a couple of python scripts that would run regularly and pull down data via APIs and web scraping.  This post walks you through the process of setting that up for yourself. 

### Why set up a Cron job?

If you have a script that you want to run regularly, but don’t want to have to manually start it, you can use Cron.  Per [Wikipedia](https://en.wikipedia.org/wiki/Cron), “the software utility Cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals.”

### A few quick steps

#### Step 0: Ensure the file you want to run is on the host server/computer
Ensure that the python file (e.g. script_to_run_with_cron.py) is on the server/computer that will be running the script via Cron.  I use SCP for this task, and always find myself referencing [this documentation](http://www.hypexr.org/linux_scp_help.php).  

#### Step 1: Ensure the proper interpreter is used for your script
To ensure that your server knows to run the script using python, make sure that the very first line of file_to_run_with_cron.py is this:

```python
#!/usr/bin/env python
```

#### Step 2: Make the file executable
To run your file via Cron, it has to be executable.  This can be done from a shell with this quick command:

```bash
chmod +x file_to_run_with_cron.py
```

#### Step 3: Modify your crontab file
To configure Cron, you need to modify the crontab file that’s on your server/computer.  Open up your shell and run the following command:

```bash
crontab -e
```
If you’ve never set up a Cron job, there will be no uncommented lines (commented lines begin with ‘#’)  in the file.  All you need to do is add a line that tells your server when and what to run; follow [this documentation](http://www.adminschoice.com/crontab-quick-reference) for all of the configuration options.  For example, this would run file_to_run_with_cron.py every 30 minutes:

```
*/30 * * * * /home/michael/python_project/file_to_run_with_cron.py

```
The first ‘*’ was required for my script to run even though it was missing from some other examples I found online.  If you want to stop your Cron job but keep it for future use, just open the crontab file and comment the job out (and maybe leave a comment in there for when you find it in 3 months…). 

#### All set!
Once you save and close the crontab file, you’re all set.  Now you can set up jobs to run in the middle of the night or weekends so that your server is working for you while you are not working at all!
