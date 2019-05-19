# Description

Initial setup for load testing with locust.

Locust is an open source tool where tests are described in python code.

- Webpage: https://locust.io/
- GitHub code: https://github.com/locustio/locust
- Documentation: https://docs.locust.io/en/stable/
- Quick Start: https://docs.locust.io/en/stable/quickstart.html


## Installation

```
pip install locustio
```

## Usage

The main file needs to be named locustfile.py

A class is created for each locust (a virtual user that extends HttpLocust)

A class is created for each locust behavior (a set of tasks, class that extends TaskSet)

Each behavior can contain multiple tasks (methods); every method can have a different weight, speciffied in the @task decorator.

Each locust needs to have a host (base URL), min_wait and max_wait

Each locust can also have it's own weight


## Run

```
Terminal command: locust
```

Open http://localhost:8089/
