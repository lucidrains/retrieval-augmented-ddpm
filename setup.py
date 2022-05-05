from setuptools import setup, find_packages

setup(
  name = 'retrieval-augmented-ddpm',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Retrieval-Augmented Denoising Diffusion Probabilistic Models',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/retrieval-augmented-ddpm',
  keywords = [
    'artificial intelligence',
    'deep learning',    
    'denoising diffusion',
    'retrieval'
  ],
  install_requires=[
    'clip-retrieval',
    'einops>=0.4',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
