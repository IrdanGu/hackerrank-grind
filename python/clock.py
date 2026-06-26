def timeConversion(s):
    # Extract the AM/PM modifier (last two characters)
    modifier = s[-2:]
    
    # Extract the hour, minute, and second components
    hh = s[:2]
    mm_ss = s[2:8] # This keeps the ":MM:SS" part intact
    
    if modifier == "AM":
        if hh == "12":
            hh = "00"
    else: # If it is PM
        if hh != "12":
            # Convert to int, add 12, and format back to 2 digits with a leading zero if needed
            hh = str(int(hh) + 12)
            
    # Concatenate the updated hour with the rest of the time string
    return hh + mm_ss
