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
    private var fileNames : [String] = []
    private var fileDates : [NSNumber] = []
    private var selectedFilePath : String = ""
    public var connManager : ConnectionManager? = nil
    
    func getVersionedDocuments(){
        let jsonResult = self.connManager?.getVersionedDocuments()
        self.numRows = (jsonResult?.count)!
        
        for file in jsonResult!{
            fileNames.append(file.key as! String)
            fileDates.append(file.value as! NSNumber)
        }

    }

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        self.versionedDocuments.dataSource = self
        self.versionedDocuments.delegate = self
        
        self.getVersionedDocuments()
        
        self.versionedDocuments.reloadData()
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    
    override func prepare(for segue: NSStoryboardSegue, sender: Any?) {
        if let destinationController = segue.destinationController as? RevisionsViewController{
            destinationController.connManager = self.connManager!
            print("File: " + selectedFilePath)
            destinationController.fp = self.selectedFilePath
        }
    }
    
    func numberOfRows(in tableView: NSTableView) -> Int {
        return self.numRows
    }
    
    func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any? {
        var text = ""
        
        if(tableColumn?.headerCell.title == "Name"){
            text = fileNames[row]
        } else {
            text = String(fileDates[row] as! Int)
        }
        
        return text
    }
    
    func tableViewSelectionDidChange(_ notification: Notification) {
        let fileIndex: Int = self.versionedDocuments.selectedRow
        if(fileIndex >= 0 && fileIndex < self.fileNames.count){
            let fileName: String = self.fileNames[fileIndex]
            
            self.selectedFilePath = fileName
            performSegue(withIdentifier: "showRevisions", sender: nil)
            
        }
    }

}

