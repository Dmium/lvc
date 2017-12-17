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

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do view setup here.
    }
    
    @IBAction func connectBtnClicked(_ sender: Any) {
        let host = hostInput.stringValue
        let port = portInput.stringValue
        
        let connectionManager : ConnectionManager = ConnectionManager(host: host, port: port)
        if(connectionManager.testConnection()){
            performSegue(withIdentifier: "showVersionedFiles", sender: nil)
        }
    }
    
}
