#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                         Pickle Manipulation #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Primary Functions for Pickle Manipulation                                    #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Populate the Pickle Contents                                    savepickle #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Collect the Pickle Contents                                     loadpickle #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from os import path as os_path
from pickle import dump as pickle_dump
from pickle import load as pickle_load
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Primary Functions for Pickle Manipulation                                    #
#------------------------------------------------------------------------------#
#
#~~ Populate the Pickle Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Populate the serialized content to the pickle with provided file system path
#-----------------------------------------------------------------------------
# file_path [REQUIRED] [STRING]
#   Complete or relative file system path for writing out the provided content
#-----------------------------------------------------------------------------
# contents [REQUIRED] [DICTIONARY|LIST]
#   Content in either dictionary or list format thay will be written to pickle
#-----------------------------------------------------------------------------
# Returns default boolean indicating the overall success or failure of routine
#-----------------------------------------------------------------------------
def savepickle(file_path, contents):
    #
    # Populate serialized content to the pickle with provided file system path
    excepted = "failed to save the contents provided to pickle on file system"
    try: pickle_dump(contents, open(file_path, "wb"))
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Returns default boolean indicating overall success or failure of routine
    return True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Collect the Pickle Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Collects the serialized content of the pickle from provided file system path
#-----------------------------------------------------------------------------
# file_path [REQUIRED] [STRING]
#   Complete or relative file system path for reading in the provided contents
#-----------------------------------------------------------------------------
# Returns the complete deserialized content of the pickle from the file system
#-----------------------------------------------------------------------------
def loadpickle(file_path):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    #
    # Collects serialized content of the pickle from provided file system path
    excepted = "failed to load the content from the pickle on the file system"
    try: x = pickle_load(open(file_path, "rb"))
    except Exception as reason: raise Exception(excepted) from reason
    else: returned = x
    #
    # Returns complete deserialized content of the pickle from the file system
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
