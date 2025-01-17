from typing import Any, Dict, List, Optional, Union
import requests


class CTABusTrackerAPI:
    """
    A Python 3 wrapper for the CTA Bus Tracker API.
    Documentation: 
        https://www.transitchicago.com/assets/1/6/cta_Bus_Tracker_API_Developer_Guide_and_Documentation_20160929.pdf
    """

    def __init__(self, api_key: str, timeout: int = 10) -> None:
        """
        Initialize the CTA Bus Tracker API client.

        :param api_key: Your CTA API key.
        :param timeout: HTTP request timeout in seconds.
        """
        self.api_key: str = api_key
        self.base_url: str = "http://www.ctabustracker.com/bustime/api/v2"
        self.timeout: int = timeout

    def _make_request(self, endpoint: str, params: Dict[str, Union[str, int]]) -> Dict[str, Any]:
        """
        Internal method to handle GET requests to the CTA Bus Tracker API.

        :param endpoint: The API endpoint to call (e.g., 'gettime').
        :param params: A dictionary of query parameters.
        :return: The JSON response as a Python dictionary.
        """
        # Insert the API key and JSON format by default
        params.setdefault("key", self.api_key)
        params.setdefault("format", "json")

        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()

        # The CTA API typically returns JSON with top-level keys
        return response.json()

    def get_time(self) -> Dict[str, Any]:
        """
        Returns the current time from the Bus Tracker system.

        :return: A dict with the system time.
        """
        return self._make_request("gettime", {})

    def get_vehicles(self, 
                     vid: Optional[List[str]] = None, 
                     routes: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Returns the current locations of vehicles either by vehicle ID(s) or by route(s).

        :param vid: A list of vehicle IDs to retrieve. If provided, 'routes' is ignored.
        :param routes: A list of route identifiers to retrieve.
        :return: A dict with vehicle location data.
        """
        params: Dict[str, Union[str, int]] = {}
        if vid:
            # CTA allows multiple vehicle IDs separated by commas
            params["vid"] = ",".join(vid)
        elif routes:
            # CTA allows multiple routes separated by commas
            params["rt"] = ",".join(routes)

        return self._make_request("getvehicles", params)

    def get_predictions(self,
                        stpid: Optional[List[str]] = None,
                        vid: Optional[List[str]] = None,
                        rt: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Returns prediction information for one or more stops, vehicles, or routes.

        :param stpid: List of stop IDs to get predictions for.
        :param vid: List of vehicle IDs to get predictions for.
        :param rt: List of routes to get predictions for.
        :return: A dict with predictions data.
        """
        params: Dict[str, Union[str, int]] = {}
        if stpid:
            params["stpid"] = ",".join(stpid)
        if vid:
            params["vid"] = ",".join(vid)
        if rt:
            params["rt"] = ",".join(rt)

        return self._make_request("getpredictions", params)

    def get_routes(self) -> Dict[str, Any]:
        """
        Returns a list of all currently enabled routes.

        :return: A dict with route information.
        """
        return self._make_request("getroutes", {})

    def get_directions(self, route: str) -> Dict[str, Any]:
        """
        Returns the directions (e.g., Eastbound/Westbound) for a given route.

        :param route: The route identifier (e.g., '22', 'X9', etc.).
        :return: A dict with available directions for the route.
        """
        params = {"rt": route}
        return self._make_request("getdirections", params)

    def get_stops(self, route: str, direction: str) -> Dict[str, Any]:
        """
        Returns the list of stops for a given route and direction.

        :param route: The route identifier.
        :param direction: The direction (must match exactly what the API expects, 
                          e.g. 'Eastbound', 'Northbound', etc. as returned by getDirections).
        :return: A dict with stops data.
        """
        params = {
            "rt": route,
            "dir": direction
        }
        return self._make_request("getstops", params)

    def get_patterns(self,
                     pid: Optional[List[str]] = None,
                     rt: Optional[str] = None) -> Dict[str, Any]:
        """
        Returns the pattern of a bus route (geospatial path and stops).

        :param pid: A list of pattern IDs to retrieve (optional).
        :param rt: A route identifier to retrieve pattern(s) for (optional).
        :return: A dict with pattern data.
        """
        params: Dict[str, Union[str, int]] = {}
        if pid:
            params["pid"] = ",".join(pid)
        if rt:
            params["rt"] = rt

        return self._make_request("getpatterns", params)

    def get_service_bulletins(self,
                              rt: Optional[List[str]] = None,
                              rtdir: Optional[List[str]] = None,
                              stpid: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Returns service bulletin information.

        :param rt: A list of routes to filter bulletins by.
        :param rtdir: A list of route directions to filter bulletins by.
        :param stpid: A list of stop IDs to filter bulletins by.
        :return: A dict with service bulletin data.
        """
        params: Dict[str, Union[str, int]] = {}
        if rt:
            params["rt"] = ",".join(rt)
        if rtdir:
            params["rtdir"] = ",".join(rtdir)
        if stpid:
            params["stpid"] = ",".join(stpid)

        return self._make_request("getservicebulletins", params)


if __name__ == "__main__":
    # Example usage:
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