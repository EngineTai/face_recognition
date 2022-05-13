import os

import face_recognition

picture_of_me = face_recognition.load_image_file("TaiEnzhi-2.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# print("Face in picture{}".format(my_face_encoding))

# my_face_encoding now contains a universal 'encoding' of my facial features that
# can be compared to any other picture of a face!

pic_suffix = ["jpg", "png", "bmp"]


def listPicturesInFolder(_sPath, _pic_list):
    itemsInDir = os.listdir(_sPath)
    for item in itemsInDir:
        index = item.find(".")
        suffix = item[index + 1:]
        if suffix.lower() in pic_suffix:
            _pic_list.append(item)


working_folder = "E:\\Github\\face_recognition\\mytest"
print("Working Folder is", working_folder)

unknown_picture_list = []
#     "IMG_2429.JPG",
#     "family-1.jpg",
#     "Couple-1.jpg",
#     "大庆2-1.png"
# ]

listPicturesInFolder(working_folder, unknown_picture_list)

i = 0
while i < len(unknown_picture_list):
    unknown_picture = face_recognition.load_image_file(unknown_picture_list[i])
    try:
        unknown_face_encoding_list = face_recognition.face_encodings(unknown_picture, model='large')
        face_count = len(unknown_face_encoding_list)
        if face_count > 1:
            print(unknown_picture_list[i], "has", face_count, "faces in this picture!")

        unknown_face_encoding = unknown_face_encoding_list[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0]:
            print(unknown_picture_list[i], "is a picture of me!")
        else:
            print(unknown_picture_list[i], "is NOT a picture of me!")

    except IndexError:
        print(unknown_picture_list[i], "is not able to locate any faces in it")
    i += 1

print(i, "pictures have been analyzed!")
