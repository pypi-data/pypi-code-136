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

def main():
    parser = argparse.ArgumentParser(description="many tools easily to use for computer vision")
    parser.add_argument('tool_name', type=str, help='tool names : draw_box')
    parser.add_argument('-s', '--src_file', type=str, help='source file of image')
    parser.add_argument('-d', '--dst_file', type=str, help='destination file of image')
    parser.add_argument('-b', '--box', type=str, help='box info e.g. 100,100,200,200_300,300,400,400')
    args = parser.parse_args()
    tool_name = args.tool_name
    if tool_name == 'draw_box':
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
        # print(src_file)
        # print(dst_file)
        # print(box)
        bbox_list = [[int(e) for e in one_box.split(',')] for one_box in box.split('_')]
        draw_box_on_img(src_file, dst_file, bbox_list)
    else:
        print(f"{tool_name} has not supported ~")


if __name__ == "__main__":
    main()
    
