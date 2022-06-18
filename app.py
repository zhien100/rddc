import streamlit as st
from PIL import Image, ImageDraw

def load_image(image_file):
	img = Image.open(image_file)
	return img

def yolo_to_xml_bbox(bbox, w, h):
    # x_center, y_center width heigth
    w_half_len = (bbox[2] * w) / 2
    h_half_len = (bbox[3] * h) / 2
    xmin = int((bbox[0] * w) - w_half_len)
    ymin = int((bbox[1] * h) - h_half_len)
    xmax = int((bbox[0] * w) + w_half_len)
    ymax = int((bbox[1] * h) + h_half_len)
    return [xmin, ymin, xmax, ymax]

def draw_image(img, bboxes):
    draw = ImageDraw.Draw(img)
    for bbox in bboxes:
        draw.rectangle(bbox, outline="red", width=2)
    img.save("example.jpg")
    img = Image.open("example.jpg")
    #img.show()
    return img


st.write("""
# Road Defects Detection and Classification System
\n\n
""")

image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if image_file is not None:

    # To See details
    file_details = {"filename":image_file.name, "filetype":image_file.type,"filesize":image_file.size}
    #st.write(file_details)
    st.write("Image Uploaded")

    # To View Uploaded Image
    st.image(load_image(image_file),width=250)

    result = st.button("Run")

    image_filename = "dataset/train/Japan/images/"+image_file.name
    label_filename = "dataset/train/Japan/labels/"+str(image_file.name)[:-4] + ".txt"
    bboxes = []
    img = Image.open(image_filename)
    with open(label_filename, 'r', encoding='utf8') as f:
        for line in f:
            data = line.strip().split(' ')
            bbox = [float(x) for x in data[1:]]
            bboxes.append(yolo_to_xml_bbox(bbox, img.width, img.height))


    if result:
        st.write("Original Image")
        st.image(load_image(image_file),width=250)
        st.write("\nResult")
        draw_image(img, bboxes)
        st.image('example.jpg',width = 250)