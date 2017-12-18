//
//  ReplaceViewSegue.swift
//  lvc-mac
//
//  Created by Zack Clark-Kington on 17/12/2017.
//  Copyright © 2017 Zack Clark-Kington. All rights reserved.
//

import Foundation
import Cocoa

class ReplaceViewSegue : NSStoryboardSegue{
    
    override func perform() {
        guard let sourceController = self.sourceController as? NSViewController,
            let destinationController = self.destinationController as? NSViewController,
            let window = sourceController.view.window
            else{return}
        window.contentViewController = destinationController
    }
}
