def analyze_directory(directory):
    """
    Analyzes the given directory and returns a summary of its contents.

    Args:
        directory (str): The path to the directory to be analyzed.

    Returns:
        dict: A dictionary containing the summary of the directory.
    """
    summary = {
        'directory': directory,
        'total_files': 0,
        'total_folders': 0,
        'file_types': {},
    }

    for root, dirs, files in os.walk(directory):
        summary['total_folders'] += len(dirs)
        for file in files:
            summary['total_files'] += 1
            file_type = os.path.splitext(file)[1]
            if file_type in summary['file_types']:
                summary['file_types'][file_type] += 1
            else:
                summary['file_types'][file_type] = 1

    return summary