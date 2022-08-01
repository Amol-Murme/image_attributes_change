import cv2 
import gradio as gr
import numpy as np


def img_attributes_adjust(img,brightness=255,contrast=127,sharpen=0):


	brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

	contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

	if brightness != 0: 

		if brightness > 0:

			shadow = brightness

			max = 255

		else:

			shadow = 0
			max = 255 + brightness

		al_pha = (max - shadow) / 255
		ga_mma = shadow

		# The function addWeighted calculates
		# the weighted sum of two arrays
		cal = cv2.addWeighted(img, al_pha,
							img, 0, ga_mma)

	else:
		cal = img

	if contrast != 0:
		Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
		Gamma = 127 * (1 - Alpha)

		cal = cv2.addWeighted(cal, Alpha,
							cal, 0, Gamma)

	if sharpen!=0:
		kernel = np.array([[-1,-1,-1],[-1, sharpen,-1],[-1,-1,-1]])
		cal = cv2.filter2D(img, -1, kernel)

	return cal

demo = gr.Interface(
    fn=img_attributes_adjust,
    inputs=[gr.Image(), gr.Slider(0, 510), gr.Slider(0, 254), gr.Slider(0,10)],
    outputs='image',
	live=True)
demo.launch()
if cv2.waitKey(0):
	demo.close()

if __name__ == '__main__':
	demo.launch()
