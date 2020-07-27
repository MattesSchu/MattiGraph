init:
	pip install -r requirements.txt
test:
	python -m unittest -v tests.test_hello_world
	python -m unittest -v tests.test_dijkstra
	python -m unittest -v tests.test_graph
.PHONY: init test