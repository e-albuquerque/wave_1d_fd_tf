from setuptools import setup, Extension
import numpy.distutils.core

numpy.distutils.core.setup(
        name='wave_1d_fd_tf',
        version='0.0.1',
        description='1D finite difference wave propagation implemented using TensorFlow',
        url='https://github.com/ar4/wave_1d_fd_tf',
        author='Alan Richardson',
        author_email='alan@ausargeo.com',
        license='MIT',
        packages=['wave_1d_fd_tf'],
        install_requires=['numpy', 'pandas', 'tensorflow'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ]
)
