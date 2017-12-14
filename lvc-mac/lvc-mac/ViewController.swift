//
//  ViewController.swift
//  lvc-mac
//
//  Created by Zack Clark-Kington on 14/12/2017.
//  Copyright © 2017 Zack Clark-Kington. All rights reserved.
//

import Cocoa

class ViewController: NSViewController, NSTableViewDataSource, NSTableViewDelegate {
    @IBOutlet weak var versionedDocuments: NSTableView!
    private var numRows : Int = 0

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        versionedDocuments.dataSource = self
        versionedDocuments.delegate = self
        
        let url = URL(string: "http://localhost:8080/api/getFileList")
        let request = URLRequest(url: url!)
        let response:AutoreleasingUnsafeMutablePointer<URLResponse?>?=nil
        do {
            let responseData = try NSURLConnection.sendSynchronousRequest(request, returning: response)
            let jsonResult = try JSONSerialization.jsonObject(with: responseData, options: JSONSerialization.ReadingOptions.mutableContainers) as! NSMutableDictionary
            self.numRows = jsonResult.count
            versionedDocuments.reloadData()
        } catch(let e){
            let alert = NSAlert.init(error: e)
            alert.runModal()
        }
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    
    func numberOfRows(in tableView: NSTableView) -> Int {
        return self.numRows
    }

}

