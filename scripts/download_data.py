"""
scripts/download_data.py

Data acquisition and integrity verification script.
IS 477 Final Project — fuelthedata

This script:
  1. Checks that all required data files exist in the data/ directory.
  2. Computes SHA-256 checksums for each file.
  3. Compares them against the expected values in checksums.txt.
  4. Reports pass/fail for each file.

Usage:
    python scripts/download_data.py

Dataset 1 — USDA ERS Poverty Estimates (PovertyReport.xlsx):
  1. Go to https://ers.usda.gov/data-products/county-level-data-sets/
  2. Click "Poverty" → Download the Excel file
  3. Save as: data/PovertyReport.xlsx

Dataset 2 — USDA ERS Unemployment & Income (UnemploymentReport.xlsx):
  1. Go to https://ers.usda.gov/data-products/county-level-data-sets/
  2. Click "Unemployment and median household income" → Download the Excel file
  3. Save as: data/UnemploymentReport.xlsx

Dataset 3 — FBI UCR Offenses Known to Law Enforcement 2024:
  1. Go to https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads
  2. Under "Offenses Known to Law Enforcement", download Table 8 (Excel)
  3. Save as:
     data/offenses-known-to-le-2024/CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx
"""

import hashlib
import os
import sys

EXPECTED = {
    "data/PovertyReport.xlsx":
        "819b551881fae3287f030ad0d9dd78752675d534e6bc5068d6477456431fb336",
    "data/UnemploymentReport.xlsx":
        "601fe18d0e8d8f6c721f1f4a8c2dc6cf1065ee745dda8c35f0b8a6205655daa4",
    "data/offenses-known-to-le-2024/CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx":
        "0e32917c588b0ce448559b0b3666b55096688ccb252a235093ef71913d5a0fdc",
}


def sha256(filepath: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_all(generate: bool = False) -> bool:
    """Check all files exist and match expected checksums."""
    print("=" * 60)
    print("Data integrity verification — fuelthedata")
    print("=" * 60)

    all_passed = True

    for rel_path, expected_hash in EXPECTED.items():
        print(f"\nFile : {rel_path}")

        if not os.path.isfile(rel_path):
            print(f"  [MISSING] File not found.")
            print(f"  → Please download and place it at: {rel_path}")
            all_passed = False
            continue

        actual_hash = sha256(rel_path)
        print(f"  SHA-256: {actual_hash}")

        if generate:
            print(f"  [GENERATED] Add this to checksums.txt")
            continue

        if expected_hash is None:
            print(f"  [SKIP] No expected checksum recorded yet.")
            print(f"  → Run with --generate flag to compute and record it.")
        elif actual_hash == expected_hash:
            print(f"  [PASS] Checksum matches.")
        else:
            print(f"  [FAIL] Checksum mismatch!")
            print(f"  Expected : {expected_hash}")
            all_passed = False

    print("\n" + "=" * 60)
    if generate:
        print("Generated checksums printed above. Update checksums.txt.")
    elif all_passed:
        print("All checks passed. Data is ready for analysis.")
    else:
        print("One or more checks FAILED. See messages above.")
    print("=" * 60)

    return all_passed


if __name__ == "__main__":
    generate_mode = "--generate" in sys.argv
    ok = verify_all(generate=generate_mode)
    sys.exit(0 if ok else 1)
