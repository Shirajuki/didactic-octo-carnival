<h3 align="center">vyscrap</h3>
<p align="center">It just request the tickets faster, really...</p>

### Installation

1. Clone the repository `https://github.com/Shirajuki/vyscrap`
```sh
$ git clone git@github.com:Shirajuki/vyscrap.git
```

2. Change the working directory to vyscrap
```sh
$ cd vyscrap
```

3. Install the requirements
```sh
$ python3 -m pip install -r requirements.txt
```

### Usage

```sh
$ python3 vy.py --help
usage: vy.py [the -f FROM -t TO -d DEPARTURE_DATE [-n N]
             [-w WEEKDAYS [WEEKDAYS ...]] [-v [VERBOSE [VERBOSE ...]]]

A python CLI for vy.no, effectively displaying train/bus tickets from location A to B

optional arguments:
  -h, --help            show this help message and exit
  -f FROM, --from FROM  the location you will travel from
  -t TO, --to TO        the location you will travel to
  -d DEPARTURE_DATE, --departure-date DEPARTURE_DATE
                        the departure date in format "YYYY-mm-dd"
  -n N, --n N           the amount of days you want to search
  -w WEEKDAYS [WEEKDAYS ...], --weekdays WEEKDAYS [WEEKDAYS ...]
                        filter on weekdays (mon tue wed thu fri sat sun)
  -v, --verbose         displays parsed debug

Get tickets from-to: python3 vy.py -f trondheim -t lillehammer -d 2021-10-10 -n 3
Get tickets weekday filtered: python3 vy.py -f trondheim -t lillehammer -d 2021-10-10 -n 5 -w mon tue fri
Made by me, for me c:
```

### License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.
