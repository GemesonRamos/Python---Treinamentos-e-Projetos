#impotando biblioteca opencv
import cv2 as cv
#lendo a imgem no disco
imagem = cv.imread("kratos.jpg")
#apresentando a imgam
cv.imshow("lendo imagem", imagem)
#Definindo tecla de fechar a janela
cv.waitKey(0)
#fechando a janela
cv.destroyAllWindows()