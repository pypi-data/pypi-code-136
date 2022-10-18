import os
import argparse
import cv2


def draw_box_on_img(img_file, output_file, bbox_list, bbox_color=(0xff, 0x00, 0x66),
                    labels=None):
    img = cv2.imread(img_file)
    for bbox in bbox_list:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(img, (x1, y1), (x2, y2), bbox_color)
    cv2.imwrite(output_file, img)


def deal_with_draw_box(args):
    """实现画框的功能"""
    if args.src_file is None:
        print("must specify parameter : src_file")
        return
    if args.dst_file is None:
        print("must specify parameter : dst_file")
        return
    if args.box is None:
        print("must specify parameter : box")
        return
    src_file = args.src_file
    dst_file = args.dst_file
    box = args.box
    bbox_list = [[int(e) for e in one_box.split(',')] for one_box in box.split('_')]
    draw_box_on_img(src_file, dst_file, bbox_list)


def calc_iou(box1, box2):
    """
    :param box1: = [xmin1, ymin1, xmax1, ymax1]
    :param box2: = [xmin2, ymin2, xmax2, ymax2]
    :return: 
    """
    xmin1, ymin1, xmax1, ymax1 = box1
    xmin2, ymin2, xmax2, ymax2 = box2
    # 计算每个矩形的面积
    s1 = (xmax1 - xmin1) * (ymax1 - ymin1)  # b1的面积
    s2 = (xmax2 - xmin2) * (ymax2 - ymin2)  # b2的面积
 
    # 计算相交矩形
    xmin = max(xmin1, xmin2)
    ymin = max(ymin1, ymin2)
    xmax = min(xmax1, xmax2)
    ymax = min(ymax1, ymax2)
 
    w = max(0, xmax - xmin)
    h = max(0, ymax - ymin)
    a1 = w * h  # C∩G的面积
    a2 = s1 + s2 - a1
    iou = a1 / a2 #iou = a1/ (s1 + s2 - a1)
    return iou

def deal_with_calc_iou(box):
    """实现计算iou的功能"""
    if box is None:
        print("must specify parameter : box")
        return
    if '-' in box:
        bbox_list = [[int(e) for e in one_box.split(',')] for one_box in box.split('-')]
        for bbox in bbox_list:
            bbox[2] = bbox[0] + bbox[2]
            bbox[3] = bbox[1] + bbox[3]
    else:
        bbox_list = [[int(e) for e in one_box.split(',')] for one_box in box.split('_')]
    
    iou = calc_iou(bbox_list[0], bbox_list[1])
    print(f"iou : {iou}")
    

def main():
    """主处理函数"""
    parser = argparse.ArgumentParser(description="many tools easily to use for computer vision")
    parser.add_argument('tool_name', type=str, help='tool names : draw_box, calc_iou')
    parser.add_argument('-s', '--src_file', type=str, help='source file of image')
    parser.add_argument('-d', '--dst_file', type=str, help='destination file of image')
    parser.add_argument('-b', '--box', type=str, help='box info e.g. 100,100,200,200_300,300,400,400 for x1x2y1y2 format and 100,100,200,200-300,300,400,400 for xywh format')
    args = parser.parse_args()
    tool_name = args.tool_name
    if tool_name == 'draw_box':
        deal_with_draw_box(args)
    elif tool_name == 'calc_iou':
        deal_with_calc_iou(args.box)
    else:
        print(f"{tool_name} has not supported ~")


def test_calc_iou():
    box = "1028,1326,175,55-1028,1333,174,54"
    deal_with_calc_iou(box)

if __name__ == "__main__":
    main()
    # test_calc_iou()
    
