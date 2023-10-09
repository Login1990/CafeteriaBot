import schedule
import time
import subprocess

def run_daily_script():
    # Schedule the job to run every day at 2 AM
    schedule.every().day.at("23:10").do(run_script)

    while True:
        schedule.run_pending()
        time.sleep(1)

def run_script():
    try:
        # Replace 'daily_script.py' with the actual name of your script
        subprocess.run(["python", "scraper.py"])
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    run_daily_script()