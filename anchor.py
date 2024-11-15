import utils.autoanchor as autoAC

# 对数据集重新计算 anchors
new_anchors = autoAC.kmean_anchors('/media/deep507/4tb/DR/yolov7-sandwich/data/VisDrone.yaml',12, 640, 5.0, 1000, True)
print(new_anchors)




