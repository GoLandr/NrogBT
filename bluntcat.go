package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
	"runtime"

	"github.com/derekstavis/bluntly/node"
)

func main() {
	// Use all processor cores.
	runtime.GOMAXPROCS(runtime.NumCPU())

	fmt.Println("running bluntly..")

	contacts := node.NewContactList()

	privateKey, _ := rsa.GenerateKey(rand.Reader, 1024)

	contacts.AddContact(&node.Contact{
		PublicKey: &privateKey.PublicKey,
	})

	_, err := node.NewNode(
		node.NewConfig(privateKey, contacts),
	)

	if err != nil {
		fmt.Println("failed to create a node: ", err)
	}
}
