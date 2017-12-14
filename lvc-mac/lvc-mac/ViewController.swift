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
            
            for file in jsonResult{
                fileNames.append(file.key as! String)
                fileDates.append(file.value as! NSNumber)
            }
            
           
            
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
    
    func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any? {
        var text = ""
        
        if(tableColumn?.headerCell.title == "Name"){
            text = fileNames[row]
        } else {
            text = String(fileDates[row] as! Int)
        }
        
        print(text)
        
        return text
    }
    
    /*func tableView(_ tableView: NSTableView, dataCellFor tableColumn: NSTableColumn?, row: Int) -> NSCell? {
        let cell = tableColumn?.dataCell(forRow: row) as! NSCell
        var text = ""
        
        if(tableColumn?.headerCell.title == "Name"){
            text = fileNames[row]
        } else {
            text = String(fileDates[row] as! Int)
        }
        cell.title = text
        print(cell.title)
        
        return cell
    }*/

}

