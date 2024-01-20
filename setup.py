from setuptools import find_packages, setup

# Required dependencies
required = [
    "tensorflow=2.11",
    "tensorflow-probability=0.19",
    "matplotlib",
    "seaborn",
    "wandb",
    "gym",
    "gymnasium",
    "numpy",
    "moviepy",
    "opencv-python",
    "imageio-ffmpeg",
    "promise",
    "scipy==1.11.4",
    "vizdoom",
]

setup(
    name="COOM",
    description="COOM: Benchmarking Continual Reinforcement Learning on Doom",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)
