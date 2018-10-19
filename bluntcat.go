package main

import (
	"fmt"
	"runtime"

	"github.com/derekstavis/bluntly/node"
)

func main() {
	// Use all processor cores.
	runtime.GOMAXPROCS(runtime.NumCPU())
	fmt.Println("start node with key with CPU: ", runtime.NumCPU())
	contacts := node.NewContactList()
	//privateKey, _ := rsa.GenerateKey(rand.Reader, 1024)
	keyFile := "./data/bvs_rsa"
	_port := 4059
	//fmt.Println("... new node is now started... k1 ", keyFile)
	private_key_b, err := node.RsaKeyFromPEM(keyFile)
	if err != nil {
		fmt.Println("failed to create a node: ", err)
	}
	//private_key_b, _ := rsa.GenerateKey(rand.Reader, 1024)
	//fmt.Println("... new node is now started... k2 ", private_key_b)
	/*contacts.AddContact(&node.Contact{
		PublicKey: &privateKey.PublicKey,
	})*/
	contacts.AddContact(&node.Contact{
		PublicKey: &private_key_b.PublicKey,
	})
	//	fmt.Println("private key is now on: ", contacts)
	_, err = node.NewNode(node.NewConfig(private_key_b, contacts))
	fmt.Println("the new node is now started.....")
	if err != nil {
		fmt.Println("failed to create a node: ", err)
	}

	fmt.Println("The new node is listening on port:", _port)
	//node_active.Listen(_port)
}
