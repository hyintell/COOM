from setuptools import find_packages, setup

# Required dependencies
coom_requirements = [
    "gymnasium",
    "numpy",
    "opencv-python",
    "vizdoom",
    "scipy==1.11.4",
]

cl_requirements = [
    "tensorflow=2.11",
    "tensorflow-probability=0.19",
    "wandb",
]

results_processing_requirements = [
    "wandb",
    "matplotlib",
    "seaborn",
    'pandas',
]

setup(
    name="COOM",
    description="COOM: Benchmarking Continual Reinforcement Learning on Doom",
    packages=find_packages(),
    include_package_data=True,
    install_requires=coom_requirements,
    extras_require={
        'cl': [
            # Dependencies specific to the 'cl' component
            # These can also be read from '/cl/requirements.txt'
        ]
    },
)

setup(
    name="your_project_name",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Dependencies for the 'coom' package
        # You can also read these from '/coom/requirements.txt' if you prefer
    ],
    extras_require={
        'cl': [
            # Dependencies specific to the 'cl' component
            # These can also be read from '/cl/requirements.txt'
        ]
    },
    # Include other relevant setup parameters
)