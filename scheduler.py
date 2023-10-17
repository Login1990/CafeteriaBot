import schedule
import time
import subprocess
from scraper import scraper

def run_daily_script():
    # Schedule the job to run every day at 2 AM
    schedule.every().day.at("23:10").do(run_script)

    while True:
        schedule.run_pending()
        time.sleep(1)

def run_script():
    try:
        subprocess.run(["python", "scraper.py"])
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    scraper()
    run_daily_script()