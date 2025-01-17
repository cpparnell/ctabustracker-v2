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
YOUR_CTA_API_KEY = "YOUR_API_KEY_HERE"
cta_client = CTABusTrackerAPI(YOUR_CTA_API_KEY)

# Get system time
time_response = cta_client.get_time()
print("System Time:", time_response)

# Get all routes
routes_response = cta_client.get_routes()
print("All Routes:", routes_response)

# Example: get directions for route #22
directions_response = cta_client.get_directions("22")
print("Directions for Route 22:", directions_response)

# Example: get stops for route #22, Eastbound
stops_response = cta_client.get_stops("22", "Eastbound")
print("Stops for Route 22 Eastbound:", stops_response)

# Example: get predictions for stop(s)
# (Replace 'STOP_ID' with a valid stop ID from above stops_response)
predictions_response = cta_client.get_predictions(stpid=["STOP_ID"])
print("Predictions for STOP_ID:", predictions_response)
```