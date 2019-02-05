import os

import numpy as np
import cv2

#D:\Documents\School work\Cegep\Session 6\europilot-win\data\session-1.npy
def main():
    path = input("Path to session file?: ")

    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, path)

    train_data = np.load(file_name)
    for data_point in train_data:
        cv2.imshow('window', cv2.resize(data_point[0], (640, 360)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
