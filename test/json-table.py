import json
import ast
import pandas as pd

json_output = """
[
    {
        "auto_close": true,
        "auto_open": false,
        "auto_start": false,
        "drawing_grid_size": 25,
        "filename": "Test_Network.gns3",
        "grid_size": 75,
        "name": "Test_Network",
        "path": "/home/sa_gns3/GNS3/projects/38b076b2-f632-47a9-90d5-4df5a586ade7",
        "project_id": "38b076b2-f632-47a9-90d5-4df5a586ade7",
        "scene_height": 1000,
        "scene_width": 2000,
        "show_grid": false,
        "show_interface_labels": false,
        "show_layers": false,
        "snap_to_grid": false,
        "status": "closed",
        "supplier": null,
        "variables": null,
        "zoom": 100
    },
    {
        "auto_close": true,
        "auto_open": false,
        "auto_start": false,
        "drawing_grid_size": 25,
        "filename": "untitled.gns3",
        "grid_size": 75,
        "name": "untitled",
        "path": "/home/sa_gns3/GNS3/projects/41292e7d-061b-4859-86cf-c44f4bd63fbd",
        "project_id": "41292e7d-061b-4859-86cf-c44f4bd63fbd",
        "scene_height": 1000,
        "scene_width": 2000,
        "show_grid": false,
        "show_interface_labels": false,
        "show_layers": false,
        "snap_to_grid": false,
        "status": "closed",
        "supplier": null,
        "variables": null,
        "zoom": 100
    },
    {
        "auto_close": true,
        "auto_open": false,
        "auto_start": false,
        "drawing_grid_size": 25,
        "filename": "daan.gns3",
        "grid_size": 75,
        "name": "daan",
        "path": "/home/sa_gns3/GNS3/projects/72951813-0405-0607-0809-0a0b0c0d0e0f",
        "project_id": "72951813-0405-0607-0809-0a0b0c0d0e0f",
        "scene_height": 1000,
        "scene_width": 2000,
        "show_grid": false,
        "show_interface_labels": false,
        "show_layers": false,
        "snap_to_grid": false,
        "status": "opened",
        "supplier": null,
        "variables": null,
        "zoom": 100
    }
]
"""

val = ast.literal_eval(json_output)
val1 = json.loads(json.dumps(val))
val2 = val1['name'][0]['project_id'][0]['auto_open']
print (pd.DataFrame(val2, columns=["name", "project_id", "auto_open"]))