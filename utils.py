import os
from datetime import datetime


def create_files_metadata():
    data = []
    files = os.listdir('files/')
    if len(files) > 0:
        for file in files:
            stat = os.stat('files/' + file)
            data.append({
                f"{file.split('.')[0]}": {
                    'path': "files/" + file,
                    'extension': f"{file.split('.')[1]}",
                    'size': f"{stat.st_size}" + ' B',
                    'created_at': f"{datetime.fromtimestamp(stat.st_ctime)}",
                    'modified_at': f"{datetime.fromtimestamp(stat.st_mtime)}"
                }
            })
        return data
