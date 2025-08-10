import cv2 as cv

img = cv.imread("data/screenshot.png")
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

print(f"image shape is {img.shape}")
print(f"image size is {img.size} pixels")

for x in range(25):
    for y in range(25):
        img[x, y, 0] = 0

chunk = img[90:115, 65:160]
img[200:225, 150:245] = chunk

cv.imwrite("data/screenshot.png", img)


img = cv.imread("data/seal.jpg")
img[:, :, [0, 2]] = 0


cv.imwrite("data/seal_mod.jpg", img)
