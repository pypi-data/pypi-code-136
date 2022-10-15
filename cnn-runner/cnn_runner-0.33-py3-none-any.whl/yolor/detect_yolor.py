import argparse
import os
import platform
import shutil
import time
from pathlib import Path

import cv2
import sys
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from cnn_runner.yolor.utils_yolor.google_utils import attempt_load
from cnn_runner.yolor.utils_yolor.datasets import LoadStreams, LoadImages
from cnn_runner.yolor.utils_yolor.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, strip_optimizer)
from cnn_runner.yolor.utils_yolor.plots import plot_one_box
from cnn_runner.yolor.utils_yolor.torch_utils import select_device, load_classifier, time_synchronized

from cnn_runner.yolor.models_yolor.models import *
from cnn_runner.yolor.utils_yolor.datasets import *
from cnn_runner.yolor.utils_yolor.general import *
from yolov5.utils.plots import Annotator, save_one_box

def load_classes(path):
    # Loads *.names file at 'path'
    with open(path, 'r') as f:
        names = f.read().split('\n')
    return list(filter(None, names))  # filter removes empty strings (such as last line)


class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hex = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
               '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        self.palette = [self.hex2rgb('#' + c) for c in hex]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))


colors = Colors()  # create instance for 'from utils.plots import colors'

class YoloRDetector():
    def __init__(self, source_img_path, cfg="", out="", weights=""):
        self.source_img_path = source_img_path
        self.cfg = cfg
        self.out = out
        self.weights = weights


    @torch.no_grad()
    def run(self,
            imgsz=1280,  # inference size (height, width)
            conf_thres=0.25,  # confidence threshold
            iou_thres=0.25,  # NMS IOU threshold
            device='0',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
            view_img=False,  # show results
            save_txt=True,  # save results to *.txt
            save_img=True,
            save_crop=False,  # save cropped prediction boxes
            save_conf=True,  # save confidences in --save-txt labels
            classes=None,  # filter by class: --class 0, or --class 0 2 3
            agnostic_nms=False,  # class-agnostic NMS
            augment=False,  # augmented inference
            update=False,  # update all models
            hide_labels=False,  # hide labels
            hide_conf=False,  # hide confidences
            classes_names=None,
            colors=None
            ):

        source = self.source_img_path
        weights = self.weights
        cfg = self.cfg
        out = self.out
        print("cfg file: ", cfg)

        webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')

        # Initialize
        device = select_device(device)
        if os.path.exists(out):
            shutil.rmtree(out)  # delete output folder
        os.makedirs(out)  # make new output folder
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = Darknet(cfg, imgsz).cuda()
        model.load_state_dict(torch.load(weights, map_location=device)['model'])
        # model = attempt_load(weights, map_location=device)  # load FP32 model
        # imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
        model.to(device).eval()
        if half:
            model.half()  # to FP16

        # Second-stage classifier
        classify = False
        if classify:
            modelc = load_classifier(name='resnet101', n=2)  # initialize
            modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
            modelc.to(device).eval()

        # Set Dataloader
        vid_path, vid_writer = None, None
        if webcam:
            view_img = True
            cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=imgsz)
        else:
            save_img = True
            dataset = LoadImages(source, img_size=imgsz, auto_size=64)

        # Get names and colors
        # names = load_classes(names)
        if not classes_names:
            names = ['реактор', 'реактор кв', 'градирня', 'градирня вент кв', 'градирня вент', 'РУ',
                                       'ВНС', 'турбина', 'БСС', 'машинный зал', 'парковка']
        else:
            names = classes_names

        if not colors:
            colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        # Run inference
        t0 = time.time()
        img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
        _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            t1 = time_synchronized()
            pred = model(img, augment=augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes,
                                       agnostic=agnostic_nms)
            t2 = time_synchronized()

            # Apply Classifier
            if classify:
                pred = apply_classifier(pred, modelc, img, im0s)

            # Process detections
            for i, det in enumerate(pred):  # detections per image
                if webcam:  # batch_size >= 1
                    p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
                else:
                    p, s, im0 = path, '', im0s

                p = Path(p)  # to Path
                save_path = os.path.join(out, p.name)
                txt_path = os.path.join(out, "labels")
                if not os.path.exists(txt_path):
                    os.mkdir(txt_path)
                txt_path = os.path.join(txt_path, p.stem)
                print(txt_path)
                s += '%gx%g ' % img.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += '%g %ss, ' % (n, names[int(c)])  # add to string

                    # Write results
                        # Write results
                    if os.path.exists(txt_path + '.txt'):
                        file_txt = open(txt_path + '.txt', 'w')
                        file_txt.close()

                    for *xyxy, conf, cls in det:
                        if save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            # with open(txt_path + '.txt', 'a') as f:
                            #     f.write(('%g ' * 5 + '\n') % (cls, *xywh))  # label format

                            line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
                            with open(txt_path + '.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')

                        if save_img or view_img:  # Add bbox to image
                            label = '{0:s} {1:.2f}'.format(names[int(cls)], conf)
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)])

                # Print time (inference + NMS)
                print('%sDone. (%.3fs)' % (s, t2 - t1))

                # Stream results
                if view_img:
                    cv2.imshow(p, im0)
                    if cv2.waitKey(1) == ord('q'):  # q to quit
                        raise StopIteration

                # Save results (image with detections)
                if save_img:
                    if dataset.mode == 'images':
                        cv2.imwrite(save_path, im0)
                    else:
                        if vid_path != save_path:  # new video
                            vid_path = save_path
                            if isinstance(vid_writer, cv2.VideoWriter):
                                vid_writer.release()  # release previous video writer

                            fourcc = 'mp4v'  # output video codec
                            fps = vid_cap.get(cv2.CAP_PROP_FPS)
                            w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                            h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                        vid_writer.write(im0)

            # # # Process predictions
            # seen = 0
            # s=""
            # for i, det in enumerate(pred):  # per image
            #     seen += 1
            #     if webcam:  # batch_size >= 1
            #         p, im0, frame = path[i], im0s[i].copy(), dataset.count
            #         s += f'{i}: '
            #     else:
            #         p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
            #
            #     p = Path(p)  # to Path
            #     save_path = out  # im.jpg
            #     txt_path = out
            #     s += '%gx%g ' % img.shape[2:]  # print string
            #     gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            #     imc = im0.copy() if save_crop else im0  # for save_crop
            #     annotator = Annotator(im0, example=str(names))
            #     if len(det):
            #         # Rescale boxes from img_size to im0 size
            #         det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
            #
            #         # Print results
            #         for c in det[:, -1].unique():
            #             n = (det[:, -1] == c).sum()  # detections per class
            #             s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
            #
            #         # Write results
            #         for *xyxy, conf, cls in reversed(det):
            #             if save_txt:  # Write to file
            #                 xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(
            #                     -1).tolist()  # normalized xywh
            #                 line = (cls, *xywh, conf) if save_conf else (cls, *xywh)  # label format
            #                 with open(txt_path + '.txt', 'a') as f:
            #                     f.write(('%g ' * len(line)).rstrip() % line + '\n')
            #
            #             if save_img or save_crop or view_img:  # Add bbox to image
            #                 c = int(cls)  # integer class
            #                 label = None if hide_labels else (
            #                     names[c] if hide_conf else f'{names[c]} {conf:.2f}')
            #                 annotator.box_label(xyxy, label, color=colors(c, True))
            #                 if save_crop:
            #                     save_one_box(xyxy, imc,
            #                                  file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)
            #
            #     # Stream results
            #     im0 = annotator.result()
            #     if view_img:
            #         cv2.imshow(str(p), im0)
            #         cv2.waitKey(1)  # 1 millisecond
            #
            #     # Save results (image with detections)
            #     if save_img:
            #         if dataset.mode == 'image':
            #             cv2.imwrite(save_path, im0)
            #         else:  # 'video' or 'stream'
            #             if vid_path[i] != save_path:  # new video
            #                 vid_path[i] = save_path
            #                 if isinstance(vid_writer[i], cv2.VideoWriter):
            #                     vid_writer[i].release()  # release previous video writer
            #                 if vid_cap:  # video
            #                     fps = vid_cap.get(cv2.CAP_PROP_FPS)
            #                     w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            #                     h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            #                 else:  # stream
            #                     fps, w, h = 30, im0.shape[1], im0.shape[0]
            #                 save_path = str(
            #                     Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
            #                 vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps,
            #                                                 (w, h))
            #             vid_writer[i].write(im0)
            #
            #     img_tek_num += 1
            #     self.pb.setValue(int(percent_base + (100 - percent_base) * img_tek_num / pred_num))
            # # Print time (inference-only)
            # LOGGER.info(f'{s}Done. ({t3 - t2:.3f}s)')
        if save_txt or save_img:
            print('Results saved to %s' % Path(out))
            if platform == 'darwin' and not update:  # MacOS
                os.system('open ' + save_path)

        print('Done. (%.3fs)' % (time.time() - t0))



def detect(save_img=False):
    out, source, weights, view_img, save_txt, imgsz, cfg, names = \
        opt.output, opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size, opt.cfg, opt.names
    webcam = source == '0' or source.startswith('rtsp') or source.startswith('http') or source.endswith('.txt')

    # Initialize
    device = select_device(opt.device)
    if os.path.exists(out):
        shutil.rmtree(out)  # delete output folder
    os.makedirs(out)  # make new output folder
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = Darknet(cfg, imgsz).cuda()
    model.load_state_dict(torch.load(weights[0], map_location=device)['model'])
    #model = attempt_load(weights, map_location=device)  # load FP32 model
    #imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    model.to(device).eval()
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
        modelc.to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = True
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz)
    else:
        save_img = True
        dataset = LoadImages(source, img_size=imgsz, auto_size=64)

    # Get names and colors
    names = load_classes(names)
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

    # Run inference
    t0 = time.time()
    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Apply NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
            else:
                p, s, im0 = path, '', im0s

            save_path = str(Path(out) / Path(p).name)
            txt_path = str(Path(out) / Path(p).stem) + ('_%g' % dataset.frame if dataset.mode == 'video' else '')
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, names[int(c)])  # add to string

                # Write results
                for *xyxy, conf, cls in det:
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * 5 + '\n') % (cls, *xywh))  # label format

                    if save_img or view_img:  # Add bbox to image
                        label = '%s %.2f' % (names[int(cls)], conf)
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

            # Print time (inference + NMS)
            print('%sDone. (%.3fs)' % (s, t2 - t1))

            # Stream results
            if view_img:
                cv2.imshow(p, im0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'images':
                    cv2.imwrite(save_path, im0)
                else:
                    if vid_path != save_path:  # new video
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()  # release previous video writer

                        fourcc = 'mp4v'  # output video codec
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        print('Results saved to %s' % Path(out))
        if platform == 'darwin' and not opt.update:  # MacOS
            os.system('open ' + save_path)

    print('Done. (%.3fs)' % (time.time() - t0))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='yolor_p6.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='inference/output', help='output folder')  # output folder
    parser.add_argument('--img-size', type=int, default=1280, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.4, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--cfg', type=str, default='cfg/yolor_p6.cfg', help='*.cfg path')
    parser.add_argument('--names', type=str, default='data/coco.names', help='*.cfg path')
    opt = parser.parse_args()
    print(opt)

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()
