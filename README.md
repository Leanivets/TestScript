# Project Title

This can help you to display cpu and memory metrics from your host. The script where used is writen on Python. So it's a cross platform script. The Docker containers with this script is present in this project too.

## Getting Started

First, downloading project archives use this link [https://github.com/Leanivets/TestScript/archive/master.zip]. After extract files using unzip programs.
You also may download files one by one using this links:
[metrics.py][https://github.com/Leanivets/TestScript/raw/master/metrics.py]
[Dockerfile][https://github.com/Leanivets/TestScript/raw/master/Dockerfile]
[create.sh][https://github.com/Leanivets/TestScript/raw/master/create.sh]

### Prerequisites

For running metrics script you need to install Python version 3 or later, PIP for Python version 3 and PSUTIL

```
On Ubuntu server:
sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
For other system see your system documentation for installing Python3 and PIP for Python version 3.

For installing PSUTIL run this command on your command line on Linux host wirh root privileges:
pip3 install psutil

```

### Installing

You may start script with next scenarium:

Go to the directory with script metrics.py and then add script execute permission:

```
chmod +x metrics.py
```

After this you may running script use next syntaxe:

```
./metrics.py [cpu/mem/all]
```
Keys have next function:
cpu - view CPU metrics
mem - view Memory metrics
all - view all metrics(CPU and Memory)

## Deployment Docker container

For deploy docker container you must first install Docker on your system.
You may deploy docker container with next scenarium:
Go to the directory with script start.sh and then add script execute permission:
```
chmod +x start.sh
```

After this running script use next syntaxe:
```
./start.sh
```

## Testing Docker containers

For testing work the docker container run next command:
```
docker --rm -it who/psutil
```
In result you will must see the CPU and Memory metrics for your host.

For watching CPU metrics for your host run next command:
```
docker --rm -it who/psutil cpu
```

For watching Memory metrics for your host run next command:
```
docker --rm -it who/psutil mem
```

## Built With

* [psutil](https://psutil.readthedocs.io/en/latest/) - The Python cross-platform library
* [Docker](https://www.docker.com/) - The open container platform

## Versioning

I use [Github](https://github.com/) for versioning 

## Authors

* **Boichuk Taras** - *Сompetitive work* - [Leanivets](https://github.com/Leanivets)

## License

This project is free licensed
