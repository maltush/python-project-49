.PHONY: 
	install brain_games build package-install
    
install:
	uv sync

brain_games:
	uv run brain_games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
