
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
Push-Location $dir/..

docker run --rm --detach --volume "/etc/localtime:/etc/localtime" --volume "${PWD}/hotreloader/inotify.conf:/config/inotify.conf:rw" --volume "${PWD}:/workspace" --name=classy_config-docs-hotreloader hotreloader