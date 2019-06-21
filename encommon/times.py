#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                             Time Processing #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Python Functions for Time Processing                                         #
# : Standard Time Converting                                     timeformat(2) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from time import localtime as time_localtime
from time import mktime as time_mktime
from time import strftime as time_strftime
from time import strptime as time_strptime
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Python Functions for Time Processing                                         #
#------------------------------------------------------------------------------#
#
#~~ Standard Time Converting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Conditionally perform the conversions to and from epoch and timestamp string
#-----------------------------------------------------------------------------
# source [REQUIRED] [STRING|INTEGER|FLOAT]
#   Can be Unix epoch or timestamp styled string relevant for format parameter
#-----------------------------------------------------------------------------
# format [REQUIRED] [STRING]
#   Standard time flags for when deciphering or converting to source parameter
#-----------------------------------------------------------------------------
# Returns the Unix epoch and timestamp string for the provided input parameter
#-----------------------------------------------------------------------------
def timeformat(source, format):
    #
    # Convert the function source input parameter into its relevant couterpart
    excepted = "Failed to convert specified source time into a time structure"
    if isinstance(source, (int, float)):
        try: object = time_localtime(source)
        except Exception as reason: raise Exception(excepted) from reason
    elif isinstance(source, str):
        try: object = time_strptime(source, format)
        except Exception as reason: raise Exception(excepted) from reason
    #
    # Determine the Unix epoch time and format the timestamp using time object
    excepted = "Failed to calculate base Unix epoch time using time structure"
    try: epoch = round(time_mktime(object), 3)
    except Exception as reason: raise Exception(excepted) from reason
    excepted = "Failed to construct the timestamp string using time structure"
    try: timestamp = time_strftime(format, object)
    except Exception as reason: raise Exception(excepted) from reason
    #
    # Returns Unix epoch and timestamp string for the provided input parameter
    return (epoch, timestamp)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
