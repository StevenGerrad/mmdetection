_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

num_classes=6,#类别数+1
img_scale=(1024,1024), #输入图像尺寸的最大边与最小边（train、val、test这三处都要修改）
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) #当gpu数量为8时,lr=0.02；当gpu数量为4时,lr=0.01；我只要一个gpu，所以设置lr=0.0025