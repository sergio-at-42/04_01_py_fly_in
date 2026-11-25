# Virtual Environment
VENV = venv_flyin
# Python3 in virtual environment
PYTHON = $(VENV)/bin/python3
# PIP in virtual environment
PIP = $(VENV)/bin/pip
# application
APP = flyin.py

# maps
MAPS00 = maps/00_test_map.txt
MAPS11 = maps/easy/01_linear_path.txt
MAPS12 = maps/easy/02_simple_fork.txt
MAPS13 = maps/easy/03_basic_capacity.txt
MAPS21 = maps/medium/01_dead_end_trap.txt
MAPS22 = maps/medium/02_circular_loop.txt
MAPS23 = maps/medium/03_priority_puzzle.txt
MAPS31 = maps/hard/01_maze_nightmare.txt
MAPS32 = maps/hard/02_capacity_hell.txt
MAPS33 = maps/hard/03_ultimate_challenge.txt
MAPS41 = maps/challenger/01_the_impossible_dream.txt


# Execute the main script of Pac-Man with config.json.
help :
	@echo "make / make help : display this page."
	@echo "make install : install application and dependencies."
	@echo "make run : run application, with test map."
	@echo "make runall : run application, with all the tests maps."
	@echo "make runXX : run application, with XX test map (replace XX. First X for Difficulty (1-3), and second X for Level(1-3))."
	@echo "make clean : delete pycache and mypy_cache."
	@echo "make fclean : delete venv, dist and build directory, .spec files, pycache, mypy_cache."
	@echo "make exe : create application's exe file."

# create virtual envornement for python.
$(VENV):
	python3 -m venv $(VENV)

# Execute the main script of Pac-Man with config.json.
run :$(VENV)
	$(PYTHON) $(APP) $(MAPS00)
	make clean

runall : run11 run12 run13 run21 run22 run23 run31 run32 run33 run41

run11 : $(VENV)
	$(PYTHON) $(APP) $(MAPS11)
run12 : $(VENV)
	$(PYTHON) $(APP) $(MAPS12)
run13 : $(VENV)
	$(PYTHON) $(APP) $(MAPS13)
run21 : $(VENV)
	$(PYTHON) $(APP) $(MAPS21)
run22 : $(VENV)
	$(PYTHON) $(APP) $(MAPS22)
run23 : $(VENV)
	$(PYTHON) $(APP) $(MAPS23)
run31 : $(VENV)
	$(PYTHON) $(APP) $(MAPS31)
run32 : $(VENV)
	$(PYTHON) $(APP) $(MAPS32)
run33 : $(VENV)
	$(PYTHON) $(APP) $(MAPS33)
run41 : $(VENV)
	$(PYTHON) $(APP) $(MAPS41)


# Install activity dependencies using pip, uv, pipx, or any other package manager of your choice.
install : $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install --requirement requirements.txt

# Remove temporary files or caches (e.g., __pycache__, .mypy_cache) to keep the activity environment clean.
clean :
	find . -type d -name "__pycache__" -exec rm --force --recursive {} +
	find . -type d -name ".mypy_cache" -exec rm --force --recursive {} +

# Remove temporary files or caches and python virtual environment.
fclean : clean
	rm --force --recursive $(VENV)
	rm --force --recursive dist
	rm --force --recursive build
	rm --force *.spec

# flake8 . and mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
lint :
	flake8 .
	mypy . --warn-return-any --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# flake8 . and mypy .
lint-strict :
	flake8 .
	mypy . --strict

# create package
exe : $(VENV)
	$(PIP) install pyinstaller
	rm --force --recursive build dist
	$(VENV)/bin/pyinstaller \
		--onefile \
		--name flyin \
		--add-data "lib_pacman:./lib_pacman" \
		--add-data "config.json:./config.json" \
		--noconfirm \
		flyin.py
	rm --force --recursive build
	rm --force flyin.spec
	@echo "Exec file ready in dist directory (launch with : ./dist/flyin config.json)"

# Run the main script in debug mode using Python’s built-in debugger (e.g., pdb).
debug : $(VENV)
	$(PYTHON) -m pdb $(APP)
