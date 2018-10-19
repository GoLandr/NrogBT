DIRDEST_LINUX=/Users/hesk/go/src/github.com/GoLandr/NrogBT/build/linux_amd64
DIRDEST_WIN=/Users/hesk/go/src/github.com/GoLandr/NrogBT/build/windows_amd64
DIRDEST_OSX=/Users/hesk/go/src/github.com/GoLandr/NrogBT/build/osx_amd64

env CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags=gpu bluntcat.go
mv -f bluntcat $DIRDEST_LINUX
echo "Linux build done."
env CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -tags=gpu bluntcat.go
mv -f bluntcat.exe $DIRDEST_WIN
echo "Windows build done."
env CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build -tags=gpu bluntcat.go
mv -f bluntcat $DIRDEST_OSX
echo "OSX build done."
