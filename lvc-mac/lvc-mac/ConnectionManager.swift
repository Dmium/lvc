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
    
    private func makeRequest(requestEndpoint: String) -> Any?{
        print(requestEndpoint)
        let url = URL(string: "http://" + self.host! + ":" + self.port! + requestEndpoint)
        let request = URLRequest(url: url!)
        let response:AutoreleasingUnsafeMutablePointer<URLResponse?>?=nil
        
        do{
            let responseData = try NSURLConnection.sendSynchronousRequest(request, returning: response)
            return responseData
        } catch(let e){
            let alert = NSAlert.init(error: e)
            alert.runModal()
        }
        
        return nil
    }
    
    public func testConnection() -> Bool{
        let response = makeRequest(requestEndpoint: "/api/registerClient")
        return !(response == nil)
    }
    
    public func getVersionedDocuments() -> NSMutableDictionary{
        let response : Data = makeRequest(requestEndpoint: "/api/getFileList") as! Data
        do{
            return try JSONSerialization.jsonObject(with: response, options: JSONSerialization.ReadingOptions.mutableContainers) as! NSMutableDictionary
        } catch {
            return NSMutableDictionary.init(dictionary: [String : String](), copyItems: false)
        }
    }
    
    public func getNumberOfRevisions(fp: String) -> Int{
        let requestEndpoint = "/api/getNumberRevisions/" + fp
        let responseData : Data = makeRequest(requestEndpoint: requestEndpoint) as! Data
        do{
            let jsonDict = try JSONSerialization.jsonObject(with: responseData, options: JSONSerialization.ReadingOptions.mutableContainers) as! NSMutableDictionary
            return Int(jsonDict.value(forKey: "numRevisions") as! NSNumber)
        } catch {
            return 0
        }
    }
    
    public func getRevisionByIndex(fp: String, index: Int) -> String{
        let requestEndpoint = "/api/getRevisionByIndex/" + String(index) + "/" + fp
        let responseData : Data = makeRequest(requestEndpoint: requestEndpoint) as! Data
        do{
            let jsonDict = try JSONSerialization.jsonObject(with: responseData, options: JSONSerialization.ReadingOptions.mutableContainers) as! NSMutableDictionary
            return jsonDict.value(forKey: "content") as! String
        } catch {
            return ""
        }
    }
    
    public func getLatestRevision(fp: String) -> String{
        let latestRevisionIndex : Int = self.getNumberOfRevisions(fp: fp) - 1
        return getRevisionByIndex(fp: fp, index: latestRevisionIndex)
    }
}
