_base_ = [
    '../../_base_/models/faster-rcnn_r50-dc5.py',
    '../../_base_/datasets/imagenet_vid_dff_style.py',
    '../../_base_/default_runtime.py'
]
model = dict(
    type='DFF',
    detector=dict(
        train_cfg=dict(
            rpn_proposal=dict(max_per_img=1000),
            rcnn=dict(sampler=dict(num=512)))),
    motion=dict(
        type='FlowNetSimple',
        img_scale_factor=0.5,
        init_cfg=dict(
            type='Pretrained',
            checkpoint=  # noqa: E251
            'https://download.openmmlab.com/mmtracking/pretrained_weights/flownet_simple.pth'  # noqa: E501
        )),
    train_cfg=None,
    test_cfg=dict(key_frame_interval=10))

# training schedule
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=7, val_interval=7)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

# learning rate
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=1.0 / 3,
        by_epoch=False,
        begin=0,
        end=500),
    dict(
        type='MultiStepLR',
        begin=0,
        end=7,
        by_epoch=True,
        milestones=[2, 5],
        gamma=0.1)
]

# optimizer
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001),
    clip_grad=dict(max_norm=35, norm_type=2))

visualizer = dict(type='DetLocalVisualizer')
