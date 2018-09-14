import cv2
from matplotlib import pyplot as plt
import numpy as np


class Image:

    def __init__(self, img):
        self.image = cv2.imread(img)
        self.kernel = np.ones((6, 6), np.float32) / 25  # definição do KERNEL/MÁSCARA

    def print_pixels(self):
        print("Altura: %d pixels" % (self.image.shape[0]))  # shape é um vetor --> índice p extrair o necessario
        print("Largura: %d pixels" % (self.image.shape[1]))
        # print("Canais: %d" % (self.img.shape[2]))

    def media_filter(self):  # aplicar o filtro da MÉDIA
        image = cv2.imread(self.image)
        cv2.blur(image, (5, 5))

    def median_filter(self):  # aplicar o filtro da MEDIANA
        # elimina eficientemento o ruído (sal e pimenta)
        image = cv2.imread(self.image)
        cv2.medianBlur(image, 5)

    def filter2d(self):  # CONVOLUÇÃO DISCRETA 2D
        # toma como base a imagem e o valor definido no KERNEL
        image = cv2.imread(self.image)
        cv2.filter2D(image, -1, self.kernel)

    def histogram(self):
        image = cv2.imread(self.image)
        cv2.calcHist(image, [0], None, [256], [0, 256])
        plt.hist(image.ravel(), 256, [0, 256])
        plt.title('Histograma')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        plt.show()

    def histogram_bgr(self):
        image = cv2.imread(self.image)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histograma = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histograma, color=col)
            plt.xlim([0, 256])
        plt.title('Histograma: escala BGR')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        plt.show()

    def contours(self):
        # CONTORNOS - Detector de Bordas
        im = cv2.imread(self.image)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        im_o, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contours --> é uma lista em Python de todos os contornos da imagem (contorno = matriz)
        # Desenhando os CONTORNOS na Imagem:
        img_cont = cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        # parametros: (imagem_origem, lista_contornos, índice (-1), cor, espessura...)
        # cv2.imwrite("D:\imagem_cont.jpg", img_cont) SALVAR A IMAGEM

    def contours_canny(self):
        # Detecção de contornos pelo MÉTODO CANNY
        image = cv2.imread(self.image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        suave = cv2.GaussianBlur(gray, (7, 7), 0)
        canny = cv2.Canny(suave, 10, 30)  # 20, 120 - menos mais bordas
        result = np.vstack(canny)
        # cv2.imwrite("D:\imagem_bordasCanny.jpg", result) SALVAR A IMAGEM

    def equalize(self):
        # EQUALIZAÇÃO DO HISTOGRAMA --> "esticar" o hist, evitar que fique concentrado apenas em um ponto alto
        # Melhorar o contraste da imagem --> aumentar detalhes
        img = cv2.imread(self.image)
        equa = cv2.equalizeHist(img)
        cv2.calcHist(equa, [0], None, [256], [0, 256])
        plt.hist(equa.ravel(), 256, [0, 256])
        plt.title('Histograma Equalizado')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        plt.show()
        # res = np.hstack((img, equa))  # colocar imagem original e equa lado a lado
        # cv2.imwrite("D:\imagem_equalizada.jpg", res)