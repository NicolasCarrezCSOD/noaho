
import sys

from setuptools import setup, Extension

extra_args = ["-std=c++11"]
if sys.platform == "darwin":
    extra_args.append("-stdlib=libc++")

if sys.version_info < (3, 9):
    file_source = "src/noahong_legacy.cpp"
else:
    file_source = "src/noahong.cpp"

noaho_module = Extension(
    "noahong",
    sources=[
        # Cython generated
        file_source,
        # original
        "src/array-aho.cpp",
    ],
    depends=["src/array-aho.h", "src/noahong.pyx"],
    extra_compile_args=extra_args,
    extra_link_args=extra_args,
)

version = "0.11.1"

setup(
    name="noahong",
    version=version,
    author="Jeff Donner",
    author_email="jeffrey.donner@gmail.com",
    url="https://github.com/clustree/noahong",
    description="Fast, non-overlapping simultaneous multiple keyword search",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    ext_modules=[noaho_module],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.7,<4",
)
