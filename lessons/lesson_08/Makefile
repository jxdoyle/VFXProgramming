# File Paramaters
BLENDER_BIN		:= blender					# name and location of blender binary // exe
BLEND_FILE		:= vfx_production.blend		# Name of Blender File (Project file)
BLEND_SCRIPT	:= load_script.py			# Python Script to run

# Progress Messages
MSG_START	:= "Scene Build Started"
MSG_END		:= "Scene Build Complete"
MSG_CLEAN	:= "Cleaning up Directory"

build:
	@echo ${MSG_START}

	# Show Meshes
	${BLENDER_BIN} ${BLEND_FILE} -P ${BLEND_SCRIPT}

	@echo ${MSG_END}

.PHONY: clean

clean:
	@echo ${MSG_CLEAN}
	rm -rf ${RENDER_DIR} || true
