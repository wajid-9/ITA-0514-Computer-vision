import cv2
input_img = cv2.imread(r"C:\Users\shaik\OneDrive\Pictures\Picture3.png")
if input_img is not None:
    resized_img = cv2.resize(input_img, (500, 400))
    watermark_img = cv2.imread(r"C:\Users\shaik\OneDrive\Pictures\Picture3.png")
    if watermark_img is not None:
        resized_wm = cv2.resize(watermark_img, (100, 80))
        h_img, w_img, _ = resized_img.shape
        h_wm, w_wm, _ = resized_wm.shape
        center_y = int(h_img/2)
        center_x = int(w_img/2)
        top_y = center_y - int(h_wm/2)
        left_x = center_x - int(w_wm/2)
        bottom_y = top_y + h_wm
        right_x = left_x + w_wm
        roi = resized_img[top_y:bottom_y, left_x:right_x]
        result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
        resized_img[top_y:bottom_y, left_x:right_x] = result
        filename = "path/to/save/result/image.png"
        cv2.imwrite(filename, resized_img)
        cv2.imshow("Resized Input Image with Watermark", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the watermark image.")
else:
    print("Error: Unable to load the input image.")
