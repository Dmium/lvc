//
//  ConnectionManager.swift
//  lvc-mac
//
//  Created by Zack Clark-Kington on 17/12/2017.
//  Copyright © 2017 Zack Clark-Kington. All rights reserved.
//

import Foundation
import Cocoa

class ConnectionManager{
    private var host : String? = nil
    private var port : String? = nil
    

    init(host: String, port: String) {
        self.host = host
        self.port = port
        
        self.testConnection()
    }
    
    public func testConnection() -> Bool{
        let host = self.host
        let port = self.port
        let url = URL(string: "http://" + host! + ":" + port! + "/api/registerClient")
        let request = URLRequest(url: url!)
        let response:AutoreleasingUnsafeMutablePointer<URLResponse?>?=nil
        do{
            let responseData = try NSURLConnection.sendSynchronousRequest(request, returning: response)
            if(response == nil){
                self.host = host
                self.port = port
                return true
            }
        } catch(let e){
            let alert = NSAlert.init(error: e)
            alert.runModal()
        }
    
        return false
    }
}
