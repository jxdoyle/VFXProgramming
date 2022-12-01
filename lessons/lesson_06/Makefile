# Basic Build
# build:
#	blender -b automation.blend -P integration.py
#	blender -b automation.blend -o //render//frame_ -F PNG -f 65..140

# File Paramaters
BLENDER_BIN		:= blender					# name and location of blender binary // exe
# e.g. on windows blender is located in 'C://Program Files//Blender Foundation//Blender 3.3//blender' 
BLEND_FILE		:= vfx_production.blend		# Name of Blender File (Project file)
BLEND_SCRIPT	:= integration.py			# Python Script to run
# render directory
RENDER_DIR		:= render
# output frame image name prefix
FRAMES			:= frame_			
IMG_OUT			:= PNG						# output frame image type
RENDER_FRMS		:= 65..140					# edit frames required
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

	# Run Python script, creates the meshes adds keyframes
	${BLENDER_BIN} -b ${BLEND_FILE} -P ${BLEND_SCRIPT}

	@echo ${RENDER_TARGET}

	# Renders each frame of the animation
	${BLENDER_BIN} -b ${BLEND_FILE} -o ${RENDER_TARGET} -F ${IMG_OUT} -f ${RENDER_FRMS}

	@echo ${MSG_END}

.PHONY: clean

clean:
	@echo ${MSG_CLEAN}
	rm -rf ${RENDER_DIR} || true
