import bpy
from mathutils import Vector

freestyle_settings = bpy.context.scene.view_layers["View Layer"].freestyle_settings

def lineset0():
  freestyle_settings.linesets['LineSet'].select_crease = False
  freestyle_settings.linesets['LineSet'].select_suggestive_contour = False
  freestyle_settings.linesets['LineSet'].select_ridge_valley = False

def lineset1():
  freestyle_settings.linesets['LineSet'].select_crease = True

def lineset2():
  freestyle_settings.linesets['LineSet'].select_suggestive_contour = True

def lineset3():
  freestyle_settings.linesets['LineSet'].select_suggestive_contour = False
  freestyle_settings.linesets['LineSet'].select_ridge_valley= True

def lineset4():
  freestyle_settings.linesets['LineSet'].select_suggestive_contour = True

for i in range(248):
# for i in range(1):
  # body
  body_path = f"D:/HarvardCamlab/code/smplparameter2mesh/testDFault/testobjs/trueobj_{i}.obj"
  bpy.ops.import_scene.obj(filepath=body_path)
  #body_obj = bpy.context.selected_objects[0]
  # body_obj.location = Vector((0.126892, 8.78048, -0.939054))
#  body_obj.data.materials[0] = bpy.data.materials.get("emit")
 # lineset0()
  s="%03d" % i
  bpy.context.scene.render.filepath = f"D:/HarvardCamlab/code/smplparameter2mesh/testDFault/restrueimages/frame_{s}.png" 
  bpy.ops.render.render(write_still=True)
#  lineset1()
#  bpy.context.scene.render.filepath = "D:/HarvardCamlab/code/smplparameter2mesh/images/%07d_sbc.png" % i
#  bpy.ops.render.render(write_still=True)   
#  lineset2()
#  bpy.context.scene.render.filepath = "D:/HarvardCamlab/code/smplparameter2mesh/images/%07d_sbcsc.png" % i
#  bpy.ops.render.render(write_still=True)
#  lineset3()
#  bpy.context.scene.render.filepath = "D:/HarvardCamlab/code/smplparameter2mesh/images/%07d_sbcrv.png" % i
#  bpy.ops.render.render(write_still=True)
#  lineset4()
#  bpy.context.scene.render.filepath = "D:/HarvardCamlab/code/smplparameter2mesh/images/%07d_sbcscrv.png" % i
 # bpy.ops.render.render(write_still=True)
  #bpy.ops.object.delete()
  # # garment
  # garment_path = "mesh_seq/garment/%07d.obj" % i
  # bpy.ops.import_scene.obj(filepath=garment_path)
  # garment_obj = bpy.context.selected_objects[0]
  # # garment_obj.location = Vector((0.126892, 8.78048, -0.939054))
  # garment_obj.data.materials[0] = bpy.data.materials.get("emit")
  # lineset0()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/garment/%07d_sb.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset1()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/garment/%07d_sbc.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset2()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/garment/%07d_sbcsc.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset3()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/garment/%07d_sbcrv.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset4()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/garment/%07d_sbcscrv.png" % i
  # bpy.ops.render.render(write_still=True)
  # # both
  # bpy.ops.import_scene.obj(filepath=body_path)
  # body_obj = bpy.context.selected_objects[0]
  # # body_obj.location = Vector((0.126892, 8.78048, -0.939054))
  # body_obj.data.materials[0] = bpy.data.materials.get("emit")
  # lineset0()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/both/%07d_sb.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset1()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/both/%07d_sbc.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset2()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/both/%07d_sbcsc.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset3()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/both/%07d_sbcrv.png" % i
  # bpy.ops.render.render(write_still=True)
  # lineset4()
  # bpy.context.scene.render.filepath = "E:/#Internships/Adobe2021/NPRWorkflow/freestyle/both/%07d_sbcscrv.png" % i
  # bpy.ops.render.render(write_still=True)
  # bpy.ops.object.delete()
  bpy.data.objects[2].select_set(True)
  bpy.ops.object.delete()
