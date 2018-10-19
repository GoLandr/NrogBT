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
	fmt.Println("start node with key with CPU:", runtime.NumCPU())
	contacts := node.NewContactList()
	privateKey, _ := rsa.GenerateKey(rand.Reader, 1024)
	contacts.AddContact(&node.Contact{
		PublicKey: &privateKey.PublicKey,
	})
	fmt.Println("private key is now on: ", contacts)
	_, err := node.NewNode(
		node.NewConfig(privateKey, contacts),
	)
	fmt.Println("the new node is now started.....")
	if err != nil {
		fmt.Println("failed to create a node: ", err)
	}
}
