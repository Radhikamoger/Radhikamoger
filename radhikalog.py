{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7fb2fb69",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# In[12]:\n",
    "\n",
    "\n",
    "import cv2\n",
    "import math\n",
    "\n",
    "#img = cv2.imread(\"pas_grey.jpg\")\n",
    "img = cv2.imread(\"praveen.jpg\")\n",
    "cv2.imshow('original_img',img)\n",
    "#cv2.waitKey()\n",
    "#cv2.destroyAllWindows()\n",
    "\n",
    "height, width, channels = img.shape\n",
    "max_pixel_value = max_pixel(img)\n",
    "\n",
    "for i in range(height):\n",
    "    for j in range(width):\n",
    "        for k in range(channels):\n",
    "            #new_col = 255 - img[i][j][k]\n",
    "            new_col = log_transform(img[i][j][k], max_pixel_value)\n",
    "            #new_col = powertrans(255, 0.4, img[i][j][k])\n",
    "            img[i][j][k] = new_col\n",
    "\n",
    "cv2.imshow('processed_img',img)\n",
    "cv2.waitKey()\n",
    "cv2.destroyAllWindows()\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3d15807",
   "metadata": {},
   "outputs": [],
   "source": [
    "def log_transform(col, max_pixel_value):\n",
    "    c = 255/(math.log(1+max_pixel_value))\n",
    "    new_col = c * math.log(1+col)\n",
    "    return new_col\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c19237ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def max_pixel(img):\n",
    "    max_pixel = 0\n",
    "    height, width, channels = img.shape\n",
    "    \n",
    "    for i in range(height):\n",
    "        for j in range(width):\n",
    "            for k in range(channels):\n",
    "                if(max_pixel < img[i][j][k]):\n",
    "                    max_pixel = img[i][j][k]\n",
    "    \n",
    "    return max_pixel\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a02f9952",
   "metadata": {},
   "outputs": [],
   "source": [
    "def powertrans(c, gamma, r):\n",
    "    #  = C*r^gamma\n",
    "    new_col = c*((r/c)**gamma)\n",
    "    return new_col\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d25f1a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
