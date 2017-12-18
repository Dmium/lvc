//
//  ConnectViewController.swift
//  lvc-mac
//
//  Created by Zack Clark-Kington on 17/12/2017.
//  Copyright © 2017 Zack Clark-Kington. All rights reserved.
//

import Cocoa

class ConnectViewController: NSViewController {
    @IBOutlet weak var hostInput: NSTextField!
    @IBOutlet weak var portInput: NSTextField!
    
    var connectionManager : ConnectionManager? = nil

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do view setup here.
    }
    
    override func prepare(for segue: NSStoryboardSegue, sender: Any?) {
        if let destinationViewController = segue.destinationController as? ViewController{
            destinationViewController.connManager = self.connectionManager!
        }
    }
    
    @IBAction func connectBtnClicked(_ sender: Any) {
        let host = hostInput.stringValue
        let port = portInput.stringValue
        
        self.connectionManager = ConnectionManager(host: host, port: port)
        if(self.connectionManager?.testConnection())!{
            performSegue(withIdentifier: "showVersionedFiles", sender: nil)
        }
    }
    
}
