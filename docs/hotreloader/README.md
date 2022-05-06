# Hot Reloader

Rebuilds the docs on save, after a configurable amount of time. This is using [inotify](https://man7.org/linux/man-pages/man7/inotify.7.html).

Configuration and be found at [inotify.conf](./inotify.conf)

## Requirements

- Docker

## How to use

Linux
```shell
./run-hotreloader.sh

docker stop hotreloader # Stops it from running
```

Windows
```powershell
./run-hotreloader.ps1

docker stop hotreloader # Stops it from running
```

