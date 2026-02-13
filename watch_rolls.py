"""
California Rolls Detector
Author: Kihara Amata (木原数多)
This script uses Playwright to monitor new California rolls on specified websites (e.g. DoorDash in this sample)
When a new roll is found, it triggers a persistent alarm (beep) until the user acknowledges it.

"""

import json
import os
import time
import random
from datetime import datetime, timedelta

from playwright.sync_api import sync_playwright

import platform

if platform.system() == "Windows":
    import winsound

# ========= CONFIG =========
SEARCH_URL = (
    "https://www.doordash.com/search/store/california%20rolls?event_type=search" # DoorDash for data resource
)

STATE_FILE = "seen_rolls.json"

BASE_INTERVAL = 30
BASE_JITTER_MIN = -10
BASE_JITTER_MAX = 15

# ==========================


def load_seen():
    """Load seen roll IDs from file"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_seen(ids):
    """Save seen roll IDs to file"""
    with open(STATE_FILE, "w") as f:
        json.dump(sorted(ids), f, indent=2)

def human_scroll(page):
    """Randomized human-like scrolling"""
    height = page.evaluate("() => document.body.scrollHeight")
    current = 0
    while current < height:
        step = random.randint(100, 300)
        page.evaluate(f"window.scrollBy(0, {step})")
        time.sleep(random.uniform(0.05, 0.2))
        current += step

def human_pause(min_ms=200, max_ms=900):
    time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))

def random_mouse_jitter(page, moves=3):
    """Small, natural mouse movements"""
    for _ in range(moves):
        x = random.randint(100, 800)
        y = random.randint(100, 600)
        page.mouse.move(x, y, steps=random.randint(10, 25))
        human_pause(80, 200)

def check_once(page):
    """Check if there are new California rolls"""
    page.goto(SEARCH_URL, timeout=60000)
    page.wait_for_selector('[id^="search-result-"]', timeout=60000)
    
    random_mouse_jitter(page)

    seen = load_seen()
    current = set()
    new_rolls = []

    cards = page.query_selector_all('[id^="search-result-"]')

    for card in cards:
        roll_id = card.get_attribute("id").replace("search-result-", "")
        title_el = card.query_selector('[data-test-component="StencilText"]')
        title = title_el.inner_text().strip() if title_el else "Unknown title"

        current.add(roll_id)
        if roll_id not in seen:
            new_rolls.append((roll_id, title))

    save_seen(current)
    
    if new_rolls:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"\n🚨 NEW CALIFORNIA ROLLS FOUND ({ts})")
        for rid, title in new_rolls:
            print(f"- {title} (ID: {rid})")
        print("=================================")
        
        persistent_alarm()

    else:
        print(f"[{datetime.now().strftime('%H:%M')}] No new California rolls.")

def persistent_alarm():
    """Call windows beep"""
    system_name = platform.system()

    try:
        while True:
            # Produce the beep
            if system_name == "Windows" and winsound:
                for freq in [2000, 2500, 3000]:
                    winsound.Beep(freq, 500)
            else:
                print("\a", end="", flush=True)
                time.sleep(0.5)
    except KeyboardInterrupt:
        pass


def main():
    print("▶ California Rolls Watcher Started\n")

    last_hour_check = datetime.now()

    USER_DATA_DIR = os.path.abspath("browser_profile")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            slow_mo=random.randint(100, 300),
            viewport={"width": 1400, "height": 800}
        )

        page = context.new_page()

        while True:
            try:
                check_once(page)

                now = datetime.now()
                if now - last_hour_check >= timedelta(hours=1):
                    last_hour_check = now

            except Exception as e:
                print("⚠️ Error:", e)

            sleep_time = BASE_INTERVAL + random.randint(BASE_JITTER_MIN, BASE_JITTER_MAX)
            print(f"Sleeping ~{sleep_time} seconds...\n")
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
