# Scam Call Detection Flow

This mini project simulates how a simple logic-based system could flag potentially scammy call transcripts based on known fraud indicators.

### 🔍 What it does:
- Reads a CSV file of sample call transcripts
- Checks each transcript for specific scam keywords (like "OTP", "invest", "gift", etc.)
- Flags whether the call contains suspicious content

### 🛠️ Tech Used:
- Python
- Pandas

### 📁 Files:
- `scam_call_transcripts.csv` – input dataset
- `scam_call_detector.py` – main script
- `scam_call_transcripts_flagged.csv` – output with results

### ✅ How to Run:
```bash
python scam_call_detector.py
```

### 📌 Note:
This is a prototype to demonstrate fraud detection logic—not a production-ready tool.
