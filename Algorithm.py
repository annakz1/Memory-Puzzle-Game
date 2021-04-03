import cv2
import pickle
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageDraw


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define a list of images the way you like
imageList = ["img1.jpeg", "img2.jpeg", "img3.jpeg", "img4.jpeg", "img5.jpeg", "img6.jpeg", "img7.jpeg", "img8.jpeg",
             "img9.jpeg", "img10.jpeg", "img11.jpeg", "img12.jpeg"]


class Algorithm:
    def __init__(self):
        self.scores = []

    def run_algorithm(self):
        self.keypoints_descriptors(imageList)
        self.scores = self.scores_matrix(imageList)
        self.find_best_pairs(imageList)
        return "success"

    # The keypoints are generated on the grayscale images
    def imagesBW(self, imageList):
        images_BW = []
        for imageName in imageList:
            imagePath = os.path.join(FILE_DIR, "WEB-app\data\images\\" + str(imageName))
            images_BW.append(self.imageResize(cv2.imread(imagePath, 0)))
        return images_BW

    # all images are being resized so we will focus on relevant keypoints
    def imageResize(self, image):
        maxD = 1024
        height, width = image.shape
        aspectRatio = width / height
        if aspectRatio < 1:
            newSize = (int(maxD * aspectRatio), maxD)
        else:
            newSize = (maxD, int(maxD / aspectRatio))
        image = cv2.resize(image, newSize)
        return image

    # all images are being resized so we will focus on relevant keypoints
    def imageResizeBW(self, image):
        maxD = 1024
        height, width, channel = image.shape
        aspectRatio = width / height
        if aspectRatio < 1:
            newSize = (int(maxD * aspectRatio), maxD)
        else:
            newSize = (maxD, int(maxD / aspectRatio))
        image = cv2.resize(image, newSize)
        return image

    def computeSIFT(self, image):
        sift = cv2.xfeatures2d.SIFT_create()
        return sift.detectAndCompute(image, None)

    # compute keypoints and descriptors based on sift
    # we save them, so we will be able to use the results in a loop without computing every time
    def keypoints_descriptors(self, imageList):
        images_BW = self.imagesBW(imageList)
        keypoints = []
        descriptors = []
        i = 0
        for image in images_BW:
            keypointTemp, descriptorTemp = self.computeSIFT(image)
            keypoints.append(keypointTemp)
            descriptors.append(descriptorTemp)
            i += 1

        i = 0
        for keypoint in keypoints:
            deserializedKeypoints = []
            filepath = os.path.join(FILE_DIR, "WEB-app\data\keypoints\\" + str(imageList[i].split('.')[0]) + ".txt")
            for point in keypoint:
                temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id)
                deserializedKeypoints.append(temp)
            with open(filepath, 'wb') as fp:
                pickle.dump(deserializedKeypoints, fp)
            i += 1

        i = 0
        for descriptor in descriptors:
            filepath = os.path.join(FILE_DIR, "WEB-app\data\descriptors\\" + str(imageList[i].split('.')[0]) + ".txt")
            with open(filepath, 'wb') as fp:
                pickle.dump(descriptor, fp)
            i += 1

    def fetchKeypointFromFile(self, i):
        filepath = os.path.join(FILE_DIR, "WEB-app\data\keypoints\\" + str(imageList[i].split('.')[0]) + ".txt")
        keypoint = []
        file = open(filepath, 'rb')
        deserializedKeypoints = pickle.load(file)
        file.close()
        for point in deserializedKeypoints:
            temp = cv2.KeyPoint(x=point[0][0], y=point[0][1], _size=point[1], _angle=point[2], _response=point[3],
                                _octave=point[4], _class_id=point[5])
            keypoint.append(temp)
        return keypoint

    def fetchDescriptorFromFile(self, i):
        filepath = os.path.join(FILE_DIR, "WEB-app\data\descriptors\\" + str(imageList[i].split('.')[0]) + ".txt")
        file = open(filepath, 'rb')
        descriptor = pickle.load(file)
        file.close()
        return descriptor

    # calculating the basic matching score for 2 specific images
    def calculateScore(self, matches, keypoint1, keypoint2):
        return 100 * (matches / min(keypoint1, keypoint2))

    # Calculating the Results for any pair
    def calculateResultsFor(self, i, j):
        keypoint1 = self.fetchKeypointFromFile(i)
        descriptor1 = self.fetchDescriptorFromFile(i)
        keypoint2 = self.fetchKeypointFromFile(j)
        descriptor2 = self.fetchDescriptorFromFile(j)
        matches = self.calculateMatches(descriptor1, descriptor2)
        score = self.calculateScore(len(matches), len(keypoint1), len(keypoint2))
        plot = self.getPlotFor(i, j, keypoint1, keypoint2, matches)
        return score, plot

    def showplot(plot):
        plt.imshow(plot), plt.show()

    def getPlotFor(self, i, j, keypoint1, keypoint2, matches):
        image1_path = os.path.join(FILE_DIR, "WEB-app\data\images\\" + imageList[i])
        image1 = self.imageResizeBW(cv2.imread(image1_path))
        image2_path = os.path.join(FILE_DIR, "WEB-app\data\images\\" + imageList[j])
        image2 = self.imageResizeBW(cv2.imread(image2_path))
        return self.getPlot(image1, image2, keypoint1, keypoint2, matches)

    # resize the images for the gui
    def changeImageSize(self, i, basewidth=90):
        img = Image.open(os.path.join(FILE_DIR, "WEB-app\data\images\\" + imageList[i]))
        img = img.resize((90, 90), Image.ANTIALIAS)
        return img

    # resize and save the pairs with the relevant name
    def pairOutput(self, i, j, pair_num):
        image1 = self.changeImageSize(i)
        image2 = self.changeImageSize(j)

        image1_name = os.path.join(FILE_DIR, "WEB-app\data\\results\pair" + str(pair_num) + "_1.jpeg")
        image2_name = os.path.join(FILE_DIR, "WEB-app\data\\results\pair" + str(pair_num) + "_2.jpeg")

        image1.save(image1_name)
        image2.save(image2_name)

        image1_open = Image.open(image1_name)
        image2_open = Image.open(image2_name)
        number_text = str(pair_num)
        black = 'rgb(0, 0, 0)'  # black color
        image_editable = ImageDraw.Draw(image1_open)
        image_editable.text((14, 14), number_text, fill=black)
        image_editable.text((14, 16), number_text, fill=black)
        image_editable.text((16, 14), number_text, fill=black)
        image_editable.text((16, 16), number_text, fill=black)
        image_editable.text((15, 15), number_text)
        image1_open.save(image1_name)

        image_editable = ImageDraw.Draw(image2_open)
        image_editable.text((14, 14), number_text, fill=black)
        image_editable.text((14, 16), number_text, fill=black)
        image_editable.text((16, 14), number_text, fill=black)
        image_editable.text((16, 16), number_text, fill=black)
        image_editable.text((15, 15), number_text)
        image2_open.save(image2_name)

        # self.showplot(image1_open)
        # self.showplot(image2_open)

        return (image1, image2)

    #  matching descriptors by knn
    def calculateMatches(self, des1, des2):
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        topResults1 = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                topResults1.append([m])

        matches = bf.knnMatch(des2, des1, k=2)
        topResults2 = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                topResults2.append([m])

        topResults = []
        for match1 in topResults1:
            match1QueryIndex = match1[0].queryIdx
            match1TrainIndex = match1[0].trainIdx

            for match2 in topResults2:
                match2QueryIndex = match2[0].queryIdx
                match2TrainIndex = match2[0].trainIdx

                if (match1QueryIndex == match2TrainIndex) and (match1TrainIndex == match2QueryIndex):
                    topResults.append(match1)
        return topResults

    def getPlot(self, image1, image2, keypoint1, keypoint2, matches):
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        matchPlot = cv2.drawMatchesKnn(image1, keypoint1, image2, keypoint2, matches, None, [255, 255, 255],
                                       flags=2)
        return matchPlot

    # building the score matrix
    def scores_matrix(self, imageList):
        length = len(imageList)
        scores = np.zeros([length, length])
        for i in range(length):
            for j in range(i):
                # print("i: ",i,"j: ", j)
                score, plot = self.calculateResultsFor(i, j)
                scores[i, j] = score
        scores = scores.tolist()
        return scores

    # finding all possible pairs
    def all_pairs(self, lst):
        if len(lst) < 2:
            yield []
            return
        if len(lst) % 2 == 1:
            # Handle odd length list
            for i in range(len(lst)):
                for result in self.all_pairs(lst[:i] + lst[i + 1:]):
                    yield result
        else:
            a = lst[0]
            for i in range(1, len(lst)):
                pair = (a, lst[i])
                for rest in self.all_pairs(lst[1:i] + lst[i + 1:]):
                    yield [pair] + rest

    # compare the score of all pairs' combinations
    def find_best_pairs(self, imageList):
        images_len = len(imageList)
        images_len_list = list(range(images_len))
        all_comb_scores = []
        combinations = self.all_pairs(images_len_list)
        for combination in combinations:
            combination_score = 0
            # print(combination)
            for pair in combination:
                pair_score = (self.scores[pair[0]][pair[1]] + self.scores[pair[1]][pair[0]])
                #    print(pair)
                combination_score += pair_score
            all_comb_scores.append(combination_score)
        # print(all_comb_scores)

        best_pairs_index = all_comb_scores.index(max(all_comb_scores))

        combinations = self.all_pairs(images_len_list)

        for combination_num, combination in enumerate(combinations):

            if combination_num == best_pairs_index:
                print(combination_num)
                print(combination)
                for pair_num, pair in enumerate(combination):
                    score, plot = self.calculateResultsFor(pair[0], pair[1])
                    print("score: ", score)
                    # self.showplot(plot)
                    self.pairOutput(pair[0], pair[1], pair_num)
