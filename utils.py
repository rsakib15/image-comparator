import cv2
from skimage.metrics import structural_similarity as ssim


def load_and_resize(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        raise ValueError("One of the images could not be loaded. Check paths.")

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    return img1, img2


def compare_images(img1_path, img2_path, threshold=0.99, save_diff=False):
    img1, img2 = load_and_resize(img1_path, img2_path)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, diff = ssim(gray1, gray2, full=True)
    print(f"Similarity Score: {score:.4f}")

    if score < threshold:
        print("Images are different!")
        if save_diff:
            diff = (diff * 255).astype("uint8")
            cv2.imwrite("diff.png", diff)
            print("Saved difference image as diff.png")
        return False
    else:
        print("Images are the same (or very close).")
        return True
