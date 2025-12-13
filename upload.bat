 python -m black ".\src\swiftlog/__init__.py"
 python -m isort ".\src\swiftlog/__init__.py"
 python -m build
 python -m twine upload dist/*