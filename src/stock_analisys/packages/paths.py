"""
Sets the Path Variables for all files
"""

from pathlib import  Path



def set_path():

    """
    Sets paths for the most important places in my programa
    """

    cwd = Path.cwd()
    data = cwd / "data"
    bin_files = cwd / "bin"
    bastter = data / 'bastter'
    fundamentei = data / 'fundamentei'

    return (cwd, data, bin_files, bastter, fundamentei)

# =============================================================================
# Directories Setup
# =============================================================================

cwd_path, data_path, bin_path, bastter_path, fundamentei_path = set_path()
    
    
