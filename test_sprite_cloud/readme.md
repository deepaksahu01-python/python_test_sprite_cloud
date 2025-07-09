# Readme to run the automated tests
From the terminal navigate to the workspace folder "python_test_sprite_cloud"
Install python in the system
1. Setup python virtual environment:
    python -m venv .venv_python
2. Install python packages by:
    python -m pip install -r requirements.txt

3. Run the ui tests by:
    PYTHONPATH:<PATH TO python_test_sprite_cloud>/sprite_cloud python -m behave ./sauce_labs_ui/

4. Run the api tests by:
    PYTHONPATH:<PATH TO python_test_sprite_cloud>/sprite_cloud python -m behave ./reqres_api/
