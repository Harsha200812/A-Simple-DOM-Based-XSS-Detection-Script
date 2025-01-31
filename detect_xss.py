import re
import ast
from typing import List

def find_xss_vulnerabilities(js_code: str) -> List[str]:
    """
    Analyzes JavaScript code to detect potential DOM-Based XSS vulnerabilities.
    """
    vulnerabilities = []
    
    # Common untrusted sources in JavaScript
    sources = ["document.URL", "document.location", "document.referrer", "window.name", "localStorage.getItem"]
    
    # Dangerous sinks where XSS could occur
    sinks = ["innerHTML", "document.write", "eval", "setTimeout", "setInterval", "location.href", "window.postMessage"]
    
    # Look for dangerous patterns
    for line in js_code.split("\n"):
        for source in sources:
            for sink in sinks:
                pattern = rf"{source}.*{sink}"
                if re.search(pattern, line, re.IGNORECASE):
                    vulnerabilities.append(f"Potential XSS: {line.strip()}")
    
    return vulnerabilities

# Example JavaScript code to analyze
js_example = """
var userInput = document.location.hash.substring(1);
document.getElementById("output").innerHTML = userInput;
"""

# Run analysis
vulns = find_xss_vulnerabilities(js_example)

if vulns:
    print("Potential DOM-Based XSS vulnerabilities detected:")
    for v in vulns:
        print("-", v)
else:
    print("No vulnerabilities found.")
