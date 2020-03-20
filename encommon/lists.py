#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                           List Manipulation #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Primary Functions for List Manipulation                                      #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Search List with Expressions                                    listsearch #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Deduplicate Redundant List Contents                              listdedup #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Flatten Multiple Depths of Lists                               listflatten #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from re import match as re_match
from fnmatch import fnmatch as fnmatch_fnmatch
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Primary Functions for List Manipulation                                      #
#------------------------------------------------------------------------------#
#
#~~ Search List with Expressions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filter the specified source list contents using provided regular expressions
#-----------------------------------------------------------------------------
# source [REQUIRED] [LIST]
#   List which will be filtered using a provided regular expression or fnmatch
#-----------------------------------------------------------------------------
# expression [REQUIRED] [STRING]
#   Regular expression or fnmatch value for matching list items to be returned
#-----------------------------------------------------------------------------
# Returns the newly populated list of list items which matched with expression
#-----------------------------------------------------------------------------
def listsearch(source, expression):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    #
    # Filter specified source list contents using provided regular expressions
    for item in source:
        try: x = re_match(expression, item)
        except Exception as reason: pass
        else: returned.extend([item] if x else list())
        try: x = fnmatch_fnmatch(item, expression)
        except Exception as reason: pass
        else: returned.extend([item] if x else list())
    #
    # Returns newly populated list of list items which matched with expression
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Deduplicate Redundant List Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove any case sensitivite duplicative and redundant items from source list
#-----------------------------------------------------------------------------
# source [REQUIRED] [LIST]
#   List which will be processed in a new list of unique items from the source
#-----------------------------------------------------------------------------
# Returns the newly populated list of case sensitive unique values from source
#-----------------------------------------------------------------------------
def listdedup(source):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    #
    # Remove case sensitivite duplicative and redundant items from source list
    for item in source:
        if item not in returned: returned.append(item)
    #
    # Returns newly populated list of case sensitive unique values from source
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Flatten Multiple Depths of Lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert the multiple lists of varying depths into a unique single depth list
#-----------------------------------------------------------------------------
# source [REQUIRED] [LIST]
#   List that will be processed and deduplicated into new list of single depth
#-----------------------------------------------------------------------------
# Returns the newly populated list of single depth using the multidepth source
#-----------------------------------------------------------------------------
def listflatten(source):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    #
    # Convert multiple lists of varying depths into a unique single depth list
    for item in source:
        if not isinstance(item, list): returned.append(item)
        else: returned.extend(listflatten(item))
    #
    # Returns newly populated list of single depth using the multidepth source
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
