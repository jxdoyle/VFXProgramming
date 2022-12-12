# Basic Build
# build:
#	blender -b automation.blend -P integration.py
#	blender -b automation.blend -o //render//frame_ -F PNG -f 0..180

# File Paramaters
BLENDER_BIN		:= 'C://Program Files/Blender Foundation/Blender 3.1/blender'	# name and location of blender binary // exe
BLEND_FILE		:= integration.blend											# name of Blender File (Project file)
BLEND_SCRIPT	:= integration.py												# python Script to run
# render directory
RENDER_DIR		:= render
# output frame image name prefix
FRAMES			:= frame_			
IMG_OUT			:= PNG						# output frame image type
RENDER_FRMS		:= 0..180					# edit frames required
# Render Target
RENDER_TARGET	:= //${RENDER_DIR}//${FRAMES}

# Progress Messages
MSG_START	:= "Scene Build Started"
MSG_END		:= "Scene Build Complete"
MSG_CLEAN	:= "Cleaning up Render Directory"

build:
	@echo ${MSG_START}
	# Remove directory if it exits and then create directory
	rm -rf ${RENDER_DIR} || true

	# Create render directory
	mkdir ${RENDER_DIR}

	# Run python script, create meshes and add keyframes
	${BLENDER_BIN} -b ${BLEND_FILE} -P ${BLEND_SCRIPT}

	@echo ${RENDER_TARGET}

	# Render each frame of the animation
	${BLENDER_BIN} -b ${BLEND_FILE} -o ${RENDER_TARGET} -F ${IMG_OUT} -f ${RENDER_FRMS}

	@echo ${MSG_END}

.PHONY: clean

clean:
	@echo ${MSG_CLEAN}
	rm -rf ${RENDER_DIR} || true
