# UNDER_LINE for California Rolls

### Background

**UNDER\_LINE** (<ruby>滞空回線<rt>アンダーライン</rt></ruby>) is a **network of miniscule machines** spread all over [Academy City](https://toarumajutsunoindex.fandom.com/wiki/Academy_City "Academy City") which serve as the sole direct line of information to [Aleister Crowley](https://toarumajutsunoindex.fandom.com/wiki/Aleister_Crowley "Aleister Crowley").

Currently in California, **Kihara Amata** (<ruby>木原数多<rt>きはらあまた</rt></ruby>) seeks to know the moment new California rolls comes out, so he redeveloped the **UNDER\_LINE** into a system that is dedicated to detecting the release of the rolls.

<p align="lef">
  <img src="images/kihara_amata.jpg" width="40%">
  <br>
  <sub>Kihara Amata observing California Roll emergence.</sub>
</p>

### Description

In the real world, there are websites that update California roll listings in real time.

UNDER_LINE is a **Python-based tracking script** designed to run in the background for California rolls trackers by Kihara Amata. The script queries the roll source every 30 seconds to 1 minute. **Whenever a new roll appears**, it triggers the Windows beeper to produce a loud alert, notifying Kihara immediately so he can investigate.

- Monitors California roll listings **in near real time (1 min)**
- Runs with **a persistent browser profile**

### Install

- Install **Python 3.8+**
- Install the Python package for [Playwright](https://playwright.dev/python/docs/intro)

```
pip install playwright
```

- Install the Playwright-managed Chromium

```
playwright install chromium
```

- Need the operating system to be **Windows (e.g., Windows 10 or later)** to use the [Python winsound](https://docs.python.org/3/library/winsound.html) module.

### Usage

Specify a source of California rolls before you watch them (in this sample the source is [DoorDash](https://www.doordash.com/search/store/california%20rolls?event_type=search)), then run:

```
python watch_rolls.py
```

### Sample Result

```
underline-for-california-rolls>python watch_roles.py
▶ California Rolls Watcher Started

🚨 NEW ROLLS FOUND (2026-01-23 04:56)
- Dashi Japanese Restaurant
- Joy Sushi
- Yama Sushi
- Sushi Arashi
```

### References

1. [Python Playwright](https://playwright.dev/python/) Documentation
2. [UNDER_LINE](https://toarumajutsunoindex.fandom.com/wiki/UNDER_LINE)  (<ruby>滞空回線<rt>アンダーライン</rt></ruby>)  - Toaru Majutsu no Index Wiki
3. [Kihara Amata](https://toarumajutsunoindex.fandom.com/wiki/Kihara_Amata) (<ruby>木原数多<rt>きはらあまた</rt></ruby>) - Toaru Majutsu no Index Wiki


