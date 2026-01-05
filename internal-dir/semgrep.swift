// Total of 2 TPs

// SQL Injections
import Foundation
import SQLite3

class DatabaseManager {
    var db: OpaquePointer?

    init() {
        // Assume that the database connection setup is done here
    }
    
    func findUser(username: String) {
        let queryStatementString = "SELECT * FROM Users WHERE Username = '\(username)';"
        var queryStatement: OpaquePointer? = nil
        if sqlite3_prepare_v2(db, queryStatementString, -1, &queryStatement, nil) == SQLITE_OK {
            while sqlite3_step(queryStatement) == SQLITE_ROW {
                // Assume that the fetched data is processed here
            }
        }
        sqlite3_finalize(queryStatement)
    }
}


// Log Injections
import example

class LogViewController: UIViewController { 

    func foo6(webView: WKWebView, navigationAction: WKNavigationAction) {
        let urlStr = navigationAction.request.url?.absoluteString
        let components = URLComponents(url: urlStr, resolvingAgainstBaseURL: false)
        // vuln log injection
        NSLog("Query value = %@", components.query)
    }
}

// safe XXE, doesnt trigger a FP
class XXEViewController: UIViewController, XMLParserDelegate {

    var parser: XMLParser!
    
    func parseXmlData(data: Data) {
        parser = XMLParser(data: data)
        parser.delegate = self
        // Avoid XXE by disallowing the resolution of external entities
        parser.shouldResolveExternalEntities = false
        parser.parse()
    }
    
    func foo1(rawXml: String) {
        guard let data = rawXml.data(using: .utf8) else {
            print("Failed to convert XML string to data")
            return
        }
        parseXmlData(data: data)
    }

    func foo2(rawXml: String) {
        guard let data = rawXml.data(using: .utf8) else {
            print("Failed to convert XML string to data")
            return
        }
        parseXmlData(data: data)
    }
    
    // rest of the XMLParserDelegate methods would go here...
}
// XXE x3 TP

// vuln XXE 
class XXEViewController: ViewController {

    func foo1() {
        var success: Bool
        var rawXmlConvToData: NSData = rawXml.data(using: NSUTF8StringEncoding)
        var myParser: XMLParser = NSXMLParser(data: rawXmlConvToData)
        // vuln xxe
        myParser.shouldResolveExternalEntities = true
        myParser.delegate = self
        myParser.parse()
    }
    

    func foo2(xml: String) {
        parser = NSXMLParser(data: rawXml.dataUsingEncoding(NSUTF8StringEncoding)!)
        parser.delegate = self
        // vuln xxe
        parser.shouldResolveExternalEntities = true
        parser.parse()
    }
    
}
