#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                         Reading and Writing #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Python Functions for Reading and Writing                                     #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Simple File Writing                                              writefile #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Simple File Reading                                               readfile #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Locate Files and Directories                                     findfiles #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from glob import glob as glob_glob
from os import path as os_path
#-----------------------------------------------------------------------------
# Import the additional libraries which are components of the project software
#-----------------------------------------------------------------------------
from encommon.lists import listsearch
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Python Functions for Reading and Writing                                     #
#------------------------------------------------------------------------------#
#
#~~ Simple File Writing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Handle the simple file writing operations capturing and raising an exception
#-----------------------------------------------------------------------------
# file_path [REQUIRED] [STRING]
#   Complete or relative file system path to target for file writing operation
#-----------------------------------------------------------------------------
# contents [REQUIRED] [STRING]
#   Prepared and preformatted contents that written directly to specified file
#-----------------------------------------------------------------------------
# truncate [OPTIONAL] [BOOLEAN]
#   Optionally truncate the file instead of appending the contents to the last
#-----------------------------------------------------------------------------
# Returns default boolean indicating the overall success or failure of routine
#-----------------------------------------------------------------------------
def writefile(file_path, contents, truncate=False):
    #
    # Open the file path for writing optionally truncating before if specified
    excepted = "failed to open the file path specified for writing operations"
    try: file_open = open(file_path, ("a" if not truncate else "w"))
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Write provided contents to the specified file path and then safely close
    excepted = "failed when writing the specified contents to the opened file"
    try: file_open.write(str(contents))
    except Exception as reason: raise Exception(excepted) from reason
    excepted = "failed safely closing an opened file after successful writing"
    try: file_open.close()
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Returns default boolean indicating overall success or failure of routine
    return True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Simple File Reading ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Handle the simple file reading operations capturing and raising an exception
#-----------------------------------------------------------------------------
# file_path [REQUIRED] [STRING]
#   Complete or relative file system path to target for file reading operation
#-----------------------------------------------------------------------------
# Returns the complete file content from the successful file reading operation
#-----------------------------------------------------------------------------
def readfile(file_path):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    #
    # Open the file path for reading the contents that will be return upstream
    excepted = "failed to open the file path specified for reading operations"
    try: file_open = open(file_path, "r")
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Read the contents from the specified file path and perform house keeping
    excepted = "failed in reading the specified contents from the opened file"
    try: returned = file_open.read()
    except Exception as reason: raise Exception(excepted) from reason
    excepted = "failed safely closing an opened file after successful reading"
    try: file_open.close()
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Returns complete file content from the successful file reading operation
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Locate Files and Directories ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Recursively find matching files and directories using the regular expression
#-----------------------------------------------------------------------------
# find_path [REQUIRED] [STRING]
#   Base root path for where the searching will be recursively initiated using
#-----------------------------------------------------------------------------
# expression [REQUIRED] [STRING]
#   Regular expression or fnmatch value for matching list items to be returned
#-----------------------------------------------------------------------------
# Returns the matching list for files using glob patterns and match expression
#-----------------------------------------------------------------------------
def findfiles(find_path, expression):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    #
    # Normalize the input parameters for simplifying the downstream procedures
    find_path_glob = os_path.join(find_path, "**")
    #
    # Recursively find matching files and directories using regular expression
    excepted = "failed to execute glob and listsearch functions for matchings"
    try: x = listsearch(glob_glob(find_path_glob, recursive=True), expression)
    except Exception as reason: raise Exception(excepted) from reason
    else: returned.extend(x)
    #
    # Returns matching list for files using glob patterns and match expression
    return [os_path.relpath(x, find_path) for x in returned]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
