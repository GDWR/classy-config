#!/usr/bin/env bash
cd "$(dirname "$0")/.."

docker run --rm --detach --volume "/etc/localtime:/etc/localtime" --volume "${PWD}/hotreloader/inotify.conf:/config/inotify.conf:rw" --volume "${PWD}:/workspace" --name=classy_config-docs-hotreloader hotreloader