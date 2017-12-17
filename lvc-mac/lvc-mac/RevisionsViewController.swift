//
//  RevisionsViewController.swift
//  lvc-mac
//
//  Created by Zack Clark-Kington on 16/12/2017.
//  Copyright © 2017 Zack Clark-Kington. All rights reserved.
//

import Cocoa

class RevisionsViewController : NSViewController{
    @IBOutlet var revisionTextDisplay: NSTextView!
    
    var fp : String = ""
    
    var connManager : ConnectionManager? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let contents = connManager?.getLatestRevision(fp: self.fp)
        revisionTextDisplay.string = contents
    }
    
    override var representedObject: Any? {
        didSet {
            // Update the view, if already loaded.
        }
    }
}
