# 1. Python Sets Adventure

def compare_flights(our_routes, competitor_routes):
    print("Destinations that both airlines fly to:")
    print(our_routes.intersection(competitor_routes))
    print("Destinations unique to our airline:")
    print(our_routes.difference(competitor_routes))
    print("Destinations that neither airline shares:")
    print(our_routes.symmetric_difference(competitor_routes))

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

compare_flights(our_routes, competitor_routes)