import os
import sys
from pathlib import Path

def create_mdedonno_pth_file(venv_path, nist3_relative_path):
    # Find the site-packages directory within the virtual environment
    site_packages_path = next(Path(venv_path).rglob('site-packages'))
    
    # Construct the full path for the NIST3 directory
    project_root = Path(__file__).parent  # Adjust this if your script is not in the project root
    nist3_path = project_root / nist3_relative_path
    
    # Construct the paths to include in the .pth file
    paths_to_include = [str(directory.resolve()) for directory in nist3_path.iterdir() if directory.is_dir()]
    
    # Path for the mdedonno.pth file inside the site-packages directory
    mdedonno_pth_path = site_packages_path / 'mdedonno.pth'
    
    # Write the paths to the mdedonno.pth file
    with open(mdedonno_pth_path, 'w') as file:
        file.write('\n'.join(paths_to_include))
    
    print(f"mdedonno.pth created at {mdedonno_pth_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_venv> <relative_path_to_NIST3_directory>")
        sys.exit(1)
    
    venv_path = sys.argv[1]
    nist3_relative_path = sys.argv[2]
    create_mdedonno_pth_file(venv_path, nist3_relative_path)
