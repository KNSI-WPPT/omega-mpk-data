# MPK Data Crawlers

## What? and Why?
It's possible to access some interesting data shared by city of [Wrocław](https://www.wroclaw.pl/open-data/) and make some use of it. We decided to collect and then analize data of public transportation and find as many usefull applications as possible. Just out of curiousity and for fun.

## What data?
We collect data of:
- Current position of vehicles in Wrocław [from here](https://www.wroclaw.pl/open-data/index.php?option=com_content&view=article&id=106:rozklad-jazdy-transportu-publicznego&catid=17&Itemid=165).
- Current bus & tram schedules [from here](http://mpk.wroc.pl/jak-jezdzimy/mapa-pozycji-pojazdow).

## How?
Crawlers are written in python, we download data from web and then upload it to out database. This is done periodicly, depending on data collected.

## How we run crawlers?
In most cases this command should suffice.
```bash
nohup ./run.sh &
```

## Dependencies?
```
python3  # Tested on python 3.5
```
