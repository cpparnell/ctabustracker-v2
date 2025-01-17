# CTA Bus Tracker API Wrapper

A simple Python 3 client for the [Chicago Transit Authority (CTA) Bus Tracker API](https://www.transitchicago.com/assets/1/6/cta_Bus_Tracker_API_Developer_Guide_and_Documentation_20160929.pdf). This library wraps common endpoints, providing a straightforward way to query real-time bus information such as routes, directions, stops, and predictions.

## Features

- Fetch current system time from CTA Bus Tracker
- Get vehicles by route or vehicle ID
- Get predictions by stop ID, vehicle ID, or route
- List all currently enabled routes
- Retrieve directions for a route
- Retrieve stops for a route + direction
- Retrieve patterns (geospatial paths)
- Retrieve service bulletins

## Requirements

- Python 3.7+

## Installation

```bash
pip install ctabustracker-api-v2
```
## Usage

```python
from ctabustracker import CTABusTrackerAPI

api_key = "YOUR_API_KEY_HERE"
cta_client = CTABusTrackerAPI(api_key)
time_response = cta_client.get_time()
print(time_response)
```