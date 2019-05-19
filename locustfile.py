from locust import HttpLocust
from behaviors import VisitorBehavior, SearchingUserBehavior


HOST = 'https://www.google.com'

MIN_WAIT = 5000
MAX_WAIT = 9000



class Visitor(HttpLocust):
    weight: 10
    task_set = VisitorBehavior
    host = HOST
    min_wait = MIN_WAIT
    max_wait = MAX_WAIT


class SearchingUser(HttpLocust):
    weight: 90
    task_set = SearchingUserBehavior
    host = HOST
    min_wait = MIN_WAIT
    max_wait = MAX_WAIT


# Main file needs to be named locustfile.py
# Run the following command in root: locust
# Open http://localhost:8089/

