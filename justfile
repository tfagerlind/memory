# Build test container
build:
    docker build -t pi-matrix --progress plain .

check-python: build
    docker run -t --rm -v "${PWD}:/apps" alpine/flake8:6.0.0 py-matrix.py

# Check docker file
check-dockerfile:
    docker run --rm -i hadolint/hadolint < Dockerfile

# Run pi-matrix
run: build
    docker run --rm pi-matrix python pi-matrix.py

# Test and check everything
test: check-python check-dockerfile
