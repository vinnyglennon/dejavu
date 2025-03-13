import sys
import json
import numpy as np
from dejavu import Dejavu

# Convert NumPy types to Python native types
def convert_numpy_types(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (list, tuple)):
        return [convert_numpy_types(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    return obj

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python get_fingerprinter.py <file_path> [limit]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    fingerprints, file_hash = Dejavu.get_file_fingerprints(
        file_name=file_path,
        limit=None,
        print_output=False
    )
    
    # Convert fingerprints to a list of tuples and handle NumPy types
    fingerprints_list = convert_numpy_types(list(fingerprints))
    
    # Create result dictionary
    result = {
        "file_hash": file_hash,
        "fingerprints": fingerprints_list
    }
    
    # Output JSON to stdout
    print(json.dumps(result))