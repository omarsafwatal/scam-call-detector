import pandas as pd

# Load dataset
df = pd.read_csv("scam_call_transcripts.csv")

# Define suspicious keywords
scam_keywords = ["free", "gift", "OTP", "KYC", "invest", "crypto", "card details", "win", "payment"]

# Function to check for keywords in transcript
def is_scam(transcript):
    transcript = transcript.lower()
    return any(keyword in transcript for keyword in scam_keywords)

# Apply function to flag potential scams
df["Detected_Scam"] = df["Transcript"].apply(is_scam)

# Save the flagged data
df.to_csv("scam_call_transcripts_flagged.csv", index=False)
print(df[["Call_ID", "Detected_Scam"]])
