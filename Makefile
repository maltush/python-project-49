.PHONY: 
	install brain_games build package-install
    
install:
	uv sync

brain_games:
	uv run brain_games

brain_even:
	uv run run_even

brain_calc:
	uv run run_calc

brain_gcd:
	uv run run_gcd

brain_prime:
	uv run run_prime

brain_progression:
	uv run run_progression

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

