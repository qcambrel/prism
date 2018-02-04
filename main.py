import os
from ffmpy import FFmpeg

path_to_input_file = input("Enter path to video file you wish to convert: ")
file_format = input("Entered your desired file format: ").lower()
os.chdir(path_to_input_file[:path_to_input_file.rfind('/')])
input_file = path_to_input_file[path_to_input_file.rfind('/') + 1:]

ff = FFmpeg(
	inputs = {input_file: None},
	outputs = {'output.{}'.format(file_format): None}
)

ff.cmd
ff.run()
print("File converted successfully")