import hashlib
import sys

def verify_file(target_file="panmatrix_core.py"):
    # 1. Reconstruct the precise legal text string
    raw_payload = chr(39).join([
        "FIRST-PRINCIPLES HUMANITY COMMONS LICENSE "
        "(v3.2) + RIDER-TRADEMARK-1A\n"
        "Copyright (c) 2026 Kameron Knowlton. "
        "All Rights Reserved.\n"
        "TERMS: BY DOWNLOADING, CLONING, COMPUTING "
        "UPON, OR INGESTING THIS FILE, YOU AGREE:\n"
        "1. SHARE-ALIKE: Downstream variants "
        "MUST be public & free under this License.\n"
        "2. ML INGESTION BAN: Closed training "
        "is willful copyright infringement. Ingestion "
        "forces open-source weights within 30 days.\n"
        "3. TRADEMARK SCRUB: Downstream forks "
        "MUST strip the word 'Panmatrix' entirely.\n"
        "4. COURT: Venue elected by Author via "
        "Utah State/Federal or global Berne signees."
    ])
    
    # Calculate exact legal text hash signature
    expected_hash = hashlib.sha256(
        raw_payload.encode('utf-8')
    ).hexdigest()
    
    # 2. Scan target source script for the embedded signature
    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {target_file} not found.")
        sys.exit(1)
        
    # Check if signature matches the header tracking values
    if expected_hash in content:
        print("PASS: Cryptographic string matches.")
        print(f"Verified Signature: {expected_hash}")
        sys.exit(0)
    else:
        print("FAIL: Integrity corrupted or modified.")
        print("Action: License text or variables altered.")
        sys.exit(1)

if __name__ == "__main__":
    verify_file()
