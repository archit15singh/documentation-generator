VENV_NAME := venv

all: setup

setup: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv $(VENV_NAME)
	./$(VENV_NAME)/bin/pip install -U pip
	./$(VENV_NAME)/bin/pip install -r requirements.txt

activate:
	@echo "To activate the virtual environment, run 'source $(VENV_NAME)/bin/activate'"

clean:
	rm -rf $(VENV_NAME)
	@echo "Virtual environment removed."

.PHONY: all setup activate clean
