#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Packaging                                            Setup Parameters #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Setup Parameters for Python Packaging                                        #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Distribution Setup Properties                                              #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from distutils.core import setup as distutils_core_setup
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Setup Parameters for Python Packaging                                        #
#------------------------------------------------------------------------------#
#
#~~ Distribution Setup Properties ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Expected and required minimal parameters for installing the project software
#-----------------------------------------------------------------------------
distutils_core_setup(
    #
    # Information regarding the project including name version and description
    name="encommon",
    version="1.9.1",
    description="Enasis Network Common Libraries",
    author="Enasis Network",
    url="https://github.com/enasisnetwork/encommon-py",
    #
    # Additional dependency packages that must be installed for the operations
    install_requires=["netaddr"],
    #
    # Additional setup option and configuration parameters expected at install
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
