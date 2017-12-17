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
    @IBOutlet weak var revisionSlider: NSSlider!
    
    var fp : String = ""
    
    var connManager : ConnectionManager? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let contents = connManager?.getLatestRevision(fp: self.fp)
        let numRevisions = connManager?.getNumberOfRevisions(fp: self.fp)
        
        revisionTextDisplay.string = contents
        revisionSlider.maxValue = Double(numRevisions!) - 1.0
        revisionSlider.numberOfTickMarks = numRevisions!
    }
    
    override var representedObject: Any? {
        didSet {
            // Update the view, if already loaded.
        }
    }
    @IBAction func revisionSliderMoved(_ sender: Any) {
        let revisionIndex = Int(revisionSlider.doubleValue)
        revisionTextDisplay.string = connManager?.getRevisionByIndex(fp: self.fp, index: revisionIndex)
    }
}
