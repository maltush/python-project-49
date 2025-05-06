.PHONY: 
	install brain_games build package-install 
    
install:
	uv sync

brain-games:
	uv run brain_games

brain-even:
	uv run run_even

brain-calc:
	uv run run_calc

brain-gcd:
	uv run run_gcd

brain-prime:
	uv run run_prime

brain-progression:
	uv run run_progression

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

