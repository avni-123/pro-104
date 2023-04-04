import cv2

solar=cv2.imread('solar-system.jpg')
cv2.putText(solar,'Sun',(15,300),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,255,255))
cv2.imshow('output', solar)
cv2.waitKey(0)

cv2.putText(solar,'Mercury',(110,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Venus',(190,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Earth',(290,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Moon',(310,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Mars',(380,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Jupiter',(560,60),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Saturn',(760,305),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Uranus',(960,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.putText(solar,'Neptune',(1110,285),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',solar)
cv2.waitKey(0)

cv2.imwrite('solar_systemwithname.jpg',solar)
