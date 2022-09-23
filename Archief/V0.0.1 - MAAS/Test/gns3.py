from gns3fy import Node, Link, Gns3Connector
from tabulate import tabulate
import gns3fy

server = gns3fy.Gns3Connector("http://192.168.219.220:3080")
PROJECT_ID = "439938d2-4529-419d-8f55-9d40521261c5"
alpine1 = Node(project_id=PROJECT_ID, name="AlpineLinux", connector=server)
