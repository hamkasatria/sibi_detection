from icevision.all import ClassMap,tfms, Adam, COCOMetric, COCOMetricType, models

import PIL
import torch
import gradio as gr
from  gradio.components import *
import time


# Declare
class_map = ClassMap(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
image_size = 384
valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(image_size), tfms.A.Normalize()])


def init_models(model_type, backbone):
  model = model_type.model(backbone=backbone(pretrained=True), num_classes=len(class_map)) 
  return model, model_type

def set_models(mdl, path_best_model, model_name):
  class LightModel(model_type.lightning.ModelAdapter):
    def configure_optimizers(self):
        return Adam(self.parameters(), lr=1e-4)

  metrics = [COCOMetric(metric_type=COCOMetricType.bbox)]
  light_model = LightModel(mdl, metrics=metrics)
  mdl.load_state_dict(torch.load(path_best_model + model_name))

def load_model(backbone, model_name):
  model, mdl_type = init_models(model_type, backbone)
  set_models(model, path_best_model, model_name)
  return model, mdl_type


# Just change the value of selection to try another model
# 0 -> faster rcnn resnet 50
# 1 -> faster rcnn resnet 18

selection = 0
path_best_model = ''

extra_args = {}
model_type = models.torchvision.faster_rcnn

if selection == 0:
  backbone = model_type.backbones.resnet_fpn_configs.resnet50_fpn
  model_name = 'FRCNN-R50.pth'
  
if selection == 1:
  backbone = model_type.backbones.resnet_fpn_configs.resnet18_fpn
  model_name = 'FRCNN-R18.pth'


  
model, model_type = load_model(backbone, model_name)

def pred(input_image):
  try:
    detection_threshold=0.5
    display_label = True
    display_bbox = True

    img = PIL.Image.fromarray(input_image, 'RGB')
    pred_dict  = model_type.end2end_detect(img, valid_tfms, model, class_map=class_map, detection_threshold=detection_threshold, display_label=display_label, display_bbox=display_bbox, return_img=True, font_size=16, label_color="#FF59D6")
    return pred_dict['img']
    
  except:
    raise gr.Error("Error file type ! ")


with gr.Blocks() as demo:
    gr.Markdown('<h1> <p style="text-align: center;"> Pengenalan Abjad SIBI</p></h1>')
    with gr.Tab("Image"):
        with gr.Row():
            with gr.Column():
              image_input = gr.Image(label="Input")
              with gr.Row():
                image_button = gr.Button("Submit")
            with gr.Column():
              image_output = gr.Image(label="Output")
    
        
    with gr.Tab("Webcam"):
        with gr.Row():
          with gr.Column():
            image_input_cam = gr.Image(source="webcam", streaming=True)
          with gr.Column():
            image_output_cam = gr.Image(label="Output")
        
    image_input_cam.stream(fn=pred, inputs = image_input_cam, outputs = image_output_cam)
    image_button.click(pred, inputs=image_input, outputs=image_output)




demo.launch(inline=True, debug=True, share=True, show_error= True, server_port=5100)