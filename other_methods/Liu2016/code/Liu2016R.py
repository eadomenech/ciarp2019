# -*- coding: utf-8 -*-
from block_tools.blocks_class import BlocksImage
from image_tools.ImageTools import ImageTools
from helpers import utils

from PIL import Image
from scipy import misc
import numpy as np
import pywt
import math


class Liu2016R():
    """
    Método de marca de agua digital robusta
    """
    def __init__(self, key, k=1.0):
        self.key = key
        # Hash of key
        self.binary_hash_key = utils.md5Binary(self.key)

        # Strength of the watermark
        self.k = k

        # Quantification matrix
        self.Q = np.asarray([
            [16, 11, 10, 16, 24, 40, 51, 61],
            [12, 12, 14, 19, 26, 58, 60, 55],
            [14, 13, 16, 24, 40, 57, 69, 56],
            [14, 17, 22, 29, 51, 87, 80, 62],
            [18, 22, 37, 56, 68, 109, 103, 77],
            [24, 35, 55, 64, 81, 104, 113, 92],
            [49, 64, 78, 87, 103, 121, 120, 101],
            [72, 92, 95, 98, 112, 100, 103, 99]
        ])

        # Cargando watermark
        self.watermark = Image.open("static/Watermarking.png").convert("1")

        # Obteniendo array de la watermark
        watermark_array = np.asarray(self.watermark)

        # Datos de la watermark como lista
        watermark_as_list = watermark_array.reshape(
            (1, watermark_array.size))[0]
        
        # Tomando solo los valores correspondientes a los datos
        self.watermark_list = []
        for p in watermark_as_list:
            if p:
                self.watermark_list.append(255)
            else:
                self.watermark_list.append(0)
        
        # Calculando datos iniciales
        self.len_watermark_list = len(self.watermark_list)

    def insert(self, cover_image):        
        # Instancia
        itools = ImageTools()

        print("Convirtiendo a YCbCr")
        # Convirtiendo a modelo de color YCbCr
        cover_ycbcr_array = itools.rgb2ycbcr(cover_image)

        # Obteniendo componente Y
        cover_array = cover_ycbcr_array[:, :, 0]

        print("DWT")
        # DWT
        LL, [LH, HL, HH] = pywt.dwt2(cover_array, 'haar')
        
        # Dividiendo LL en bloques de 8x8
        bt_of_LL = BlocksImage(LL)
        bt_of_HH = BlocksImage(HH)

        print("Re-asignando subbanda HH")
        for i in range(bt_of_LL.max_num_blocks()):
            # Cuantificado
            QLL = utils.quantification(bt_of_LL.get_block(i), self.Q)
            # replaced directly by the resulting Q-LL
            bt_of_HH.set_block(QLL, i)
        
        print("Modificando LL")
        for i in range(self.len_watermark_list + 1):
            colums = len(LL[0])
            # Marcado
            if i > 0:
                px = i // colums
                py = i - (px * colums)
                LL[px, py] += self.watermark_list[i-1]/255 * self.k
        
        # Inverse transform
        print("IDWT")
        cover_ycbcr_array[:, :, 0] = pywt.idwt2((LL, (LH, HL, HH)), 'haar')

        print("Convirtiendo a RGB")
        image_rgb_array = itools.ycbcr2rgb(cover_ycbcr_array)               
        
        return Image.fromarray(image_rgb_array)

    def extract(self, watermarked_image):
        # Instancias necesarias
        itools = ImageTools()

        # Convirtiendo a modelo de color YCbCr
        watermarked_ycbcr_array = itools.rgb2ycbcr(watermarked_image)

        # Tomando componente Y
        watermarked_array = watermarked_ycbcr_array[:, :, 0]

        # Wavelet Transform
        LL, [LH, HL, HH] = pywt.dwt2(watermarked_array, 'haar')

        colums = len(LL[0])

        extract = []
        
        # Extracting
        # Dividiendo LL en bloques de 8x8
        bt_of_LL = BlocksImage(LL)

        for i in range(bt_of_LL.max_num_blocks()):
            # Cuantificado
            QLL = utils.quantification(bt_of_LL.get_block(i), self.Q)
            # replaced directly by the resulting Q-LL
            bt_of_LL.set_block(QLL, i)
        
        for i in range(self.len_watermark_list + 1):
            # Marcado
            if i > 0:
                px = i // colums
                py = i - (px * colums)
                extract.append(abs(round((HH[px, py] - LL[px, py])/self.k)))
        
        wh = int(math.sqrt(self.len_watermark_list))
        extract_image1 = Image.new("1", (wh, wh), 255)
        array_extract_image = misc.fromimage(extract_image1)

        for i in range(wh):
            for y in range(wh):
                if extract[wh*i+y] == 0:
                    array_extract_image[i, y] = 0

        watermark_extracted = misc.toimage(array_extract_image)        
        
        return watermark_extracted