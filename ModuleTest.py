# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 13:40
# @Author  : 郑梓斌

import core

if __name__ == '__main__':
    src = 'images/model.jpg'
    dst = 'images/20171030175254.jpg'
    output = 'images/output.jpg'
    src_points, _ = core.face_points(src)
    dst_points, _ = core.face_points(dst)

    core.face_merge(src_img='images/model.jpg',
                    src_points=src_points,
                    dst_img='images/20171030175254.jpg',
                    out_img='images/output.jpg',
                    dst_points=dst_points,
                    face_area=[250, 150, 270, 250],
                    alpha=0.75,
                    k_size=(15, 10),
                    mat_multiple=0.95)
