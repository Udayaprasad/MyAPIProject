git clone https://github.com/Udayaprasad/MyAPIProject.git
cd MyAPIProject
python -m venv mypyenv
source mypyenv/bin/activate
pip install pybuilder
pyb install_dependencies
python src/main/python/WebServiceExercise.py &
pyb -v
python src/unittest/python/webservice_tests.py &