import nmap

scans = {}

def start_scan(scan_id, target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p-')
    scans[scan_id] = nm.csv()

def get_scan_status(scan_id):
    if scan_id in scans:
        return "Completed"
    return "Not found"

def get_scan_results(scan_id):
    return scans.get(scan_id, "No results")
