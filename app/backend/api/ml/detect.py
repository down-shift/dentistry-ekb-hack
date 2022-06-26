import numpy as np
import cv2
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent.absolute()


model_w_path = str(CURRENT_DIR / "yolo.weights")
wh = model_w_path
model_c_path = str(CURRENT_DIR / "cavity-yolo1.cfg")
cfg = model_c_path
net = cv2.dnn.readNetFromDarknet(cfg, wh)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
ln = net.getLayerNames()
ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]


def detect(image, conf=0.2, thresh=0.4, s=(416, 416)):
    (H, W) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, s, swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    boxes = []
    confidences = []
    classIDs = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > conf:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, conf, thresh)
    bx = []
    cids = []
    confs = []
    if len(idxs) > 0:
        for i in idxs.flatten():
            bx.append(boxes[i])
            cids.append(classIDs[i])
            confs.append(confidences[i])
    return bx, cids, confs


def pag(img):
    x, y = img.shape[:2]
    frame = cv2.resize(img, (416, 416))
    boxes, classIDs, confidences = detect(frame)
    boxes_out = [
        (
            i[0] / 416 * y // 1,
            i[1] / 416 * x // 1,
            i[2] / 416 * y // 1,
            i[3] / 416 * x // 1,
        )
        for i in boxes
    ]
    return boxes_out, confidences


def draw_boxes(img, boxes, ids, confs):
    CLASSES = ["caries"]
    COLORS = [[47, 157, 98]]

    for i in range(len(boxes)):
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        color = (0, 255, 150)
        if COLORS is not None:
            color = [int(c) for c in COLORS[ids[i]]]

        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        # text = "{}: {:.4f}".format(CLASSES[ids[i]], confs[i])
        # cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return img
