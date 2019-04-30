# python code resizeAndPaste.py
# LR Mayer
# 08/17/2018
#
# Resize an image

import sys
sys.path.append(r'C:\Users\mdeeds\Documents\Mayer\NASA\CatalogImages\CatalogImages\Modules/')

# import numpy as np
# import argparse
#import imutils  # importing my imutils
import cv2
#import xlrd  # for reading the excel file
import pandas as pd


# ap = argparse.ArgumentParser()
#
# ap.add_argument("-i", "--image", required = True,help = "Path to the image")
#
# args = vars(ap.parse_args())
#
# print "Name of original image is :  {} ".format(args["image"])

# Assign spreadsheet filename to `file`
excel_file = r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\CreatedMaps.xlsx'

maps = pd.read_excel(excel_file)

print maps.head()
print maps.shape

#print maps["Directory"][1]

#C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-artwork-mockup
#C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-mockup-with-many-plants


# Stock Images
# dictionary : filename, image size, prefix for output image
verStocks = {r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\picture-leaning-against-brick-wall\1350.jpg':([293, 302, 890, 1077],'brick'),
             r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-leaning-against-wall-with-flower-pot\147916-OTSPQK-928.jpg':([2056, 653, 4020, 3302],'flower'),
             r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-mockup-with-poster_2%3\poster.jpg':([81, 68, 418, 561],'verposter')}
horStocks = {r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-artwork-mockup\horizontal_wallwoodtable.jpg':([451, 542, 1044, 986],'horwood'),
             r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Frame-mockup-with-many-plants\horizontal_plantstable.jpg':([1347,1050, 2670, 2012],'horplants' ),
             r'C:\Users\mdeeds\Documents\Mayer\MapDaVinci\StockFrames\Decorative-quote-and-frame-mockup-concept\PFKB9R0.jpg':([459, 444, 3542, 2885], 'horchalk')}


#---------------------------------------------------------------------------
# resize the image according to sizes in the verStocks/horStocks dictionary
#---------------------------------------------------------------------------


# iterate thru excel rows
for index, row in maps.iterrows():
    if row['Convert']:
        print row['Directory'], row['MapFileName'], row['Convert']

        # use cv2.imread to read the original image
        image = cv2.imread(row['Directory'] + '/' + row['MapFileName'])

        if row['Aspect'] == 'Vertical':  # then use vertical stock photos
            dict = verStocks
        else:
            dict = horStocks

        for stockName, specs in dict.items():
            upperX = specs[0][0]
            upperY = specs[0][1]
            lowerX = specs[0][2]
            lowerY = specs[0][3]
            prefix = specs[1]

            # use cv2.imread to read the original image
            print 'stockName = {}'.format(stockName)
            original = cv2.imread(stockName)
            #cv2.imshow('original stock', original)

            print upperX, upperY, lowerX, lowerY, prefix

            dim = (lowerX - upperX, lowerY - upperY)

            #quit()

            #cv2.imshow("Image to resize", image)

            # use cv2.imread to read the original image
            #image = cv2.imread(args["image"])

            # new resized image : old image, dimension, interpolation method for resizing
            # From openCV book (pdf) : I find that using cv2.INTER_AREA obtains the best results when resizing; how-
            # ever, other appropriate choices include cv2.INTER_LINEAR,
            # cv2.INTER_CUBIC, and cv2.INTER_NEAREST.
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

            # show the resized image
            #cv2.imshow("Resized (Width)", resized)

            #cv2.waitKey(0)

            #print "x, x+h, y, y+h : {}{}{}{} ".format(x, x+h, y, y+h)

            #original[x:x+h, y:y+w] = mapResized
            #original[upperX:lowerX, upperY:lowerY] = resized
            original[upperY:lowerY, upperX:lowerX] = resized

            #cv2.imshow('pip', original)

            cv2.waitKey(0)

            # Write out the final picture in picure image :
            cv2.imwrite(row['Directory'] + '/' + prefix + '_' + row['MapFileName'], original)

        # Make detail of image
        # Get size of image
        height, width = image.shape[:2]
        detail = image[(height/2)-500:(height/2)+500, (width/2)-500:(width/2)+500]
        #cv2.imshow("Detail", detail)
        cv2.waitKey(0)

        #write out the detail
        cv2.imwrite(row['Directory'] + '/detail_' + row['MapFileName'], detail)
