!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="vaM4RHzwClfjvociYsdG")
"project = rf.workspace("team-roboflow").project("coco-128")"
"dataset = project.version(2).download("yolov8")"
