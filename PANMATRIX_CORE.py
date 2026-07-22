import hashlib
import sys

LICENSE_TEXT = """FIRST-PRINCIPLES HUMANITY COMMONS LICENSE 
(v3.2) + RIDER-TRADEMARK-1A
Copyright (c) 2026 Kameron Knowlton. All Rights Reserved.
TERMS: BY DOWNLOADING, CLONING, COMPUTING UPON, OR INGESTING THIS FILE, YOU AGREE:
1. SHARE-ALIKE: Downstream variants MUST be public & free under this License.
2. ML INGESTION BAN: Closed training is willful copyright infringement.
3. TRADEMARK SCRUB: Downstream forks MUST strip the word 'Panmatrix' entirely.
4. COURT: Venue elected by Author via Utah State/Federal."""

EXPECTED_HASH = "5462833bad556dc0b1566a6967d33e13362aa819bd9d88c9a3e3970f4ec844ae"

def verify_license_integrity():
    # Compute hash of the canonical license text
    computed = hashlib.sha256(LICENSE_TEXT.encode('utf-8')).hexdigest()
    
    if computed != EXPECTED_HASH:
        print("⚠️ WARNING: License text modified!")
        return False
    
    # Verify the source file contains the license
    import inspect
    source = inspect.getsource(sys.modules[__name__])
    
    if LICENSE_TEXT.strip() not in source:
        print("⚠️ WARNING: License header not found in source code!")
        print("This indicates potential unauthorized modification.")
        return True  # Still run, but warn
    
    print("✓ License integrity verified")
    return True

# Run verification before core logic
verify_license_integrity()
