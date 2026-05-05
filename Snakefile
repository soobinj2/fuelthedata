"""
Snakefile — IS 477 Final Project: fuelthedata

Workflow automation for data verification, integration, and analysis.

Usage:
    snakemake --cores 1           # Run entire workflow (verify + merge)
    snakemake run_analysis        # Also execute the notebook
    snakemake verify_data         # Verify data integrity only
    snakemake clean_and_merge     # Create merged dataset only
    snakemake clean               # Remove generated files
"""

DATA_DIR     = "data"
SCRIPTS_DIR  = "scripts"
RESULTS_DIR  = "results"
NOTEBOOK_DIR = "data_analysis"

# Input data files
POVERTY_FILE  = f"{DATA_DIR}/PovertyReport.xlsx"
UNEMPLOY_FILE = f"{DATA_DIR}/UnemploymentReport.xlsx"
CRIME_FILE    = f"{DATA_DIR}/offenses-known-to-le-2024/CIUS_Table_8_Offenses_Known_to_Law_Enforcement_by_State_by_City_2024.xlsx"

# Output files
MERGED_DATA = f"{RESULTS_DIR}/merged_data.csv"
CHECKSUMS   = "checksums.txt"
NOTEBOOK    = f"{NOTEBOOK_DIR}/dataanalysis_1.ipynb"


rule all:
    """
    Default target: verify data integrity and produce merged dataset.

    To also execute the notebook and reproduce all figures, run:
        snakemake run_analysis --cores 1
    
    Or open the notebook manually:
        jupyter notebook data_analysis/dataanalysis_1.ipynb
    and execute all cells (Kernel → Restart & Run All).
    """
    input:
        MERGED_DATA,
        CHECKSUMS


rule verify_data:
    """
    Verify SHA-256 checksums of input data files.

    Ensures that data files have not been corrupted or altered.
    Reads expected checksums from checksums.txt and compares against
    actual file hashes.
    """
    input:
        POVERTY_FILE,
        UNEMPLOY_FILE,
        CRIME_FILE,
        CHECKSUMS
    output:
        touch(".verify_data.done")
    shell:
        """
        echo "Verifying data integrity..."
        python {SCRIPTS_DIR}/download_data.py
        echo "Data verification complete."
        """


rule clean_and_merge:
    """
    Load, clean, and merge the three datasets into a unified state-level dataset.

    Steps:
      1. Load poverty, unemployment, and crime data
      2. Clean column names and standardize formatting
      3. Aggregate city-level crime data to state level
      4. Merge datasets on State column
      5. Save to results/merged_data.csv

    For detailed documentation, see scripts/clean_and_merge.py
    """
    input:
        POVERTY_FILE,
        UNEMPLOY_FILE,
        CRIME_FILE,
        ".verify_data.done"
    output:
        MERGED_DATA
    shell:
        """
        echo "Running data integration..."
        python {SCRIPTS_DIR}/clean_and_merge.py
        echo "Merged dataset created: {output}"
        """


rule run_analysis:
    """
    Execute the analysis notebook to reproduce all visualizations and results.

    Uses jupyter nbconvert to run the notebook from its own directory
    (data_analysis/) so that relative paths (../data/) resolve correctly.

    Produces:
      - Scatter plots, regression plots, heatmap, histograms, boxplots
      - All outputs saved in results/figures/
    """
    input:
        MERGED_DATA,
        NOTEBOOK
    output:
        directory(f"{RESULTS_DIR}/figures")
    shell:
        """
        echo "Executing analysis notebook..."
        cd {NOTEBOOK_DIR} && jupyter nbconvert --to notebook --execute --inplace dataanalysis_1.ipynb
        echo "Analysis complete. Visualizations saved to {RESULTS_DIR}/figures/"
        """


rule clean:
    """
    Remove generated files to reset the workflow.

    Usage:
        snakemake clean --cores 1

    WARNING: This will delete:
      - results/merged_data.csv
      - results/figures/
      - .verify_data.done
    """
    shell:
        """
        rm -f {MERGED_DATA}
        rm -f .verify_data.done
        rm -rf {RESULTS_DIR}/figures
        echo "Cleanup complete."
        """
