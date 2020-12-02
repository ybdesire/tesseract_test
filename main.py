# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont,ImageEnhance
import json
import re
from pdf2image import convert_from_path
import os
#import cutimg
import pytesseract
#import cutimg
import cv2
import numpy

#from  remove_seal import remove_seal_Image
def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)
def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])


class run_ocr():
    def getfromimg(self,filepath,clearseal='0',needcut='0'):
        img_pil = Image.open(filepath)
        #cv2img_pre=cv2.cvtColor(numpy.asarray(img_pil),cv2.COLOR_RGB2BGR)
        #cv2img_done=cutimg.clear_cut(cv2img_pre,clearseal,needcut)
        #img_pil=Image.fromarray(cv2.cvtColor(cv2img_done,cv2.COLOR_BGR2RGB))
        gray_pil=img_pil.convert("L")
        text = pytesseract.image_to_boxes(gray_pil,lang='chi_sim') #使用简体中文解析图片
        allresult=[]
        textresult=[]
        result=text.split('\n')
        for r in result:
            tempr=r.split(' ')
            if len(tempr)==6:
                if tempr[0]=='~':
                    continue
                allresult.append((tempr[0],(int(tempr[1]),int(tempr[2]),int(tempr[3]),int(tempr[4]))))
                textresult.append(tempr[0])
        return  allresult ,textresult



testword=run_ocr()
allreturn=testword.getfromimg("sm1.png")
print(allreturn)

