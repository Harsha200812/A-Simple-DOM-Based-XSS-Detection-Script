# LLM-Powered DOM-Based XSS Detection Agent

## Overview

This project introduces an intelligent security agent designed to detect **DOM-Based Cross-Site Scripting (XSS)** vulnerabilities in JavaScript code. The agent leverages **AI-driven static analysis** to identify untrusted user inputs flowing into dangerous JavaScript functions (sinks), mimicking how a security researcher approaches XSS detection.

## Features

- **Analyzes JavaScript code statically** using Abstract Syntax Tree (AST) parsing.
- **Identifies vulnerable sinks** such as `innerHTML`, `document.write()`, `eval()`, etc.
- **Traces user-controlled inputs** from `document.URL`, `location.hash`, etc.
- **Provides detailed vulnerability reports** with risk classification.
- **Designed to be LLM-compatible**, allowing integration with AI models for reasoning-based security analysis.

## Installation

### Prerequisites

- Python 3.8+
- `js2py` (for JavaScript parsing in Python)
- `esprima` (JavaScript parser for AST analysis)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/llm-xss-detector.git
cd llm-xss-detector

# Install dependencies
pip install js2py esprima
```

## Usage

### Running the Detection Script

```bash
python detect_xss.py example.js
```

This will analyze `example.js` and output any detected **DOM-Based XSS vulnerabilities**.

### Example Output

```
Potential DOM-Based XSS found: User-controlled input from 'document.location' flows into 'innerHTML' without sanitization.
```

## How It Works

1. **AST Parsing**: Converts JavaScript code into an AST for structured analysis.
2. **Source Identification**: Detects untrusted user input sources.
3. **Sink Detection**: Identifies dangerous JavaScript functions.
4. **Data Flow Analysis**: Traces input flows and checks for sanitization.
5. **Report Generation**: Outputs vulnerabilities with risk classification.

## Example Vulnerable Code

```javascript
var userInput = document.location.hash.substring(1);
document.getElementById("output").innerHTML = userInput; // Vulnerable
```

## Future Enhancements

- **Integrate with AI models** for improved detection accuracy.
- **Support dynamic analysis** using browser automation.
- **Enhance reporting** with mitigation suggestions.

## Contributing

We welcome contributions! Feel free to submit issues or pull requests.

## License

MIT License

## Contact

For any questions, reach out via harshamanchala28@gmail.com 

