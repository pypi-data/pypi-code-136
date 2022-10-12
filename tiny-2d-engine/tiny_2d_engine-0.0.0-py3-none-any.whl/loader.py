# """Module to handle the loading of data into the AcquisitionCanvas"""

# from tiny_2d_engine.acquisition_canvas import (AcquisitionCanvas,)

# def update_canvas_from_dict(canvas: AcquisitionCanvas, data: dict):
#     """Load a memory into the widget"""
#     metadata = data.get("metadata", {})
#     width = metadata.get("width", 800)
#     height = metadata.get("height", 600)

#     canvas.width = width
#     canvas.height = height

#     # calibrate
#     calibration_info = data.get("calibration", None)
#     if calibration_info is not None:
#         canvas.calibrate(**calibration_info)
#     else:
#         return canvas

#     # add image
#     image_info = data.get("image", None)
#     if image_info is not None:
#         canvas.add_image(**image_info)

#     # add objects
#     objects_info = data.get("objects", None)
#     if objects_info is not None:
#         for obj_type in ["Line", "Slider", "Point"]:  # because order matters
#             #_add_objects_by_type(canvas, objects_info, obj_type)
#             canvas.add_object_by_type(objects_info, obj_type)
