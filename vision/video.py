import cv2


def load_video_writer(path, output_resolution):
	writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, output_resolution)
	return writer
