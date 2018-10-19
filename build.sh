DIRDEST_LINUX=/Users/hesk/go/src/github.com/GoLandr/NrogBT/linux_amd64
DIRDEST_WIN=/Users/hesk/go/src/github.com/GoLandr/NrogBT/windows_amd64
DIRDEST_OSX=/Users/hesk/go/src/github.com/GoLandr/NrogBT/osx_amd64

env CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags=gpu bluntcat.go
mv bluntcat $DIRDEST_LINUX
env CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -tags=gpu bluntcat.go
mv bluntcat.exe $DIRDEST_WIN
env CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build -tags=gpu bluntcat.go
mv bluntcat $DIRDEST_OSX

echo "Linux executable is generated and put into target folder."
