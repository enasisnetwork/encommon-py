#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                     Dictionary Manipulation #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Primary Functions for Dictionary Manipulation                                #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : List of Dictionaries to Dictionary                             dictstodict #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Sort List of Dictionaries                                        dictssort #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Reorder Dictionary of Dictionaries                               dictksort #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Flatten the Nested Dictionary                                  dictflatten #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Get Value from Dictionary with Dot Notation                      dictnoget #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Set Value in Dictionary with Dot Notation                        dictnoset #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from collections import OrderedDict as collections_OrderedDict
from collections.abc import MutableMapping as collections_MutableMapping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Primary Functions for Dictionary Manipulation                                #
#------------------------------------------------------------------------------#
#
#~~ List of Dictionaries to Dictionary ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Process the list of dictionaries into a single dictionary updating for merge
#-----------------------------------------------------------------------------
# source [REQUIRED] [DICTIONARY]
#   List of dictionaries which will be populated into a single base dictionary
#-----------------------------------------------------------------------------
# Returns the newly populated dictionary using the source list of dictionaries
#-----------------------------------------------------------------------------
def dictstodict(source):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = dict()
    #
    # Process list of dictionaries into a single dictionary updating for merge
    for item in source: returned.update(item)
    #
    # Returns newly populated dictionary using the source list of dictionaries
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Sort List of Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reorder the list of dictionaries on specified keys value from the dictionary
#-----------------------------------------------------------------------------
# source [REQUIRED] [LIST]
#   Lists of dictionaries which will be sorted into a new list of dictionaries
#-----------------------------------------------------------------------------
# sortby [REQUIRED] [TUPLE]
#   Sorting parameters inside a tuple of the keyname and the sorting direction
#-----------------------------------------------------------------------------
# Returns the newly populated list of dictionaries after sorting with keyvalue
#-----------------------------------------------------------------------------
def dictssort(source, sortby):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    argsdict = dict()
    #
    # Normalize the input parameters for simplifying the downstream procedures
    argsdict.update({"key": lambda x: x[sortby[0]]})
    argsdict.update({"reverse": sortby[1].lower()[:4] == "desc"})
    #
    # Reorder list of dictionaries on specified keys value from the dictionary
    excepted = "failed to sort the dictionary list using dictionary keyvalues"
    try: x = sorted(source, **argsdict)
    except Exception as reason: raise Exception(excepted) from reason
    else: returned = x
    #
    # Returns newly populated list of dictionaries after sorting with keyvalue
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Reorder Dictionary of Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reorder the dict of dictionaries on specified keys value from the dictionary
#-----------------------------------------------------------------------------
# source [REQUIRED] [DICTIONARY]
#   Dictionary with other dictionaries for sort populating into new dictionary
#-----------------------------------------------------------------------------
# sortby [REQUIRED] [TUPLE]
#   Sorting parameters inside a tuple of the keyname and the sorting direction
#-----------------------------------------------------------------------------
# Returns the newly populated dictionary from source after sorting on keyvalue
#-----------------------------------------------------------------------------
def dictksort(source, sortby):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = dict()
    argsdict = dict()
    #
    # Normalize the input parameters for simplifying the downstream procedures
    argsdict.update({"key": lambda x: x[1][sortby[0]]})
    argsdict.update({"reverse": sortby[1].lower()[:4] == "desc"})
    #
    # Reorder dict of dictionaries on specified keys value from the dictionary
    excepted = "failed to sort dictionary preserving orders using collections"
    try: x = collections_OrderedDict(sorted(source.items(), **argsdict))
    except Exception as reason: raise Exception(excepted) from reason
    else: returned = x
    #
    # Returns newly populated dictionary from source after sorting on keyvalue
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Flatten the Nested Dictionary ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flattens nested dictionary of dictionaries, lists, strings, and other values
#-----------------------------------------------------------------------------
# source [REQUIRED] [DICTIONARY]
#   Dictionary with other dictionaries for sort populating into new dictionary
#-----------------------------------------------------------------------------
# delimiter [OPTIONAL] [STRING]
#   Delimiter for joining dictionary keys and those of the nested dictionaries
#-----------------------------------------------------------------------------
# parent [OPTIONAL] [STRING]
#   Used wehn the function is recursively calling itself to process dictionary
#-----------------------------------------------------------------------------
# lowercase [OPTIONAL] [BOOLEAN]
#   Determine when each new flattened key value will be converted to lowercase
#-----------------------------------------------------------------------------
# Returns the flattened nested dictionary in single layer form using delimiter
#-----------------------------------------------------------------------------
def dictflatten(source, delimiter="_", parent=str(), lowercase=False):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = list()
    #
    # Flattens nested dictionary of dictionaries, lists, strings, other values
    for key, value in source.items():
        key_new = '{0}{1}{2}'.format(parent, delimiter, key) if parent else key
        if lowercase: key_new = key_new.lower()
        if isinstance(value, collections_MutableMapping):
            extended = dictflatten(value, delimiter, key_new, lowercase).items()
            returned.extend(extended)
        else: returned.append((key_new, value))
    #
    # Returns flattened nested dictionary in single layer form using delimiter
    return dict(returned)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Get Value from Dictionary with Dot Notation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Process dictionary returning the appropriate value based on the dot notation
#-----------------------------------------------------------------------------
# source [REQUIRED] [DICTIONARY]
#   Dictionary that will serve as the basis for the dot notation value extract
#-----------------------------------------------------------------------------
# notation [REQUIRED] [STRING]
#   Dot notation which will be used when identifying value from the dictionary
#-----------------------------------------------------------------------------
# Returns the value using dictionary based on the dot notation parameter value
#-----------------------------------------------------------------------------
def dictnoget(source, notation):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = source
    #
    # Process dictionary returning appropriate value based on the dot notation
    excepted = "failed to select the relevant noted value from the dictionary"
    for part in notation.split("."):
        try: x = returned.get(part, {})
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Returns value using dictionary based on the dot notation parameter value
    return returned
#-----------------------------------------------------------------------------
def dictnotation(source, notation): return dictnoget(source, notation)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Set Value in Dictionary with Dot Notation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Update or create the dictionary structure or value based on the dot notation
#-----------------------------------------------------------------------------
# source [REQUIRED] [DICTIONARY]
#   Dictionary that will serve as the basis for the dot notation value updates
#-----------------------------------------------------------------------------
# notation [REQUIRED] [STRING]
#   Dot notation which will be used when populating values into the dictionary
#-----------------------------------------------------------------------------
# value [OPTIONAL] [STRING|DICTIONARY|LIST|INTEGER|BOOLEAN]
#   Value that will be set or removed from dictionary when this is not defined
#-----------------------------------------------------------------------------
# Returns the dictionary that was updated using the dot notation and its value
#-----------------------------------------------------------------------------
def dictnoset(source, notation, value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = dict(source.items())
    #
    # Update or create dictionary structure or value based on the dot notation
    if "." not in notation: returned.update({notation: value})
    else:
        dict_base = notation.split(".")[:1][0]
        dict_more = ".".join(notation.split(".")[1:])
        if dict_base not in returned:
            returned.update({dict_base: dict()})
        #
        # Recursively enumerate and populate remaining portion of dot notation
        excepted = "failed to enumerate dot notation or update the dictionary"
        try: x = dictnoset(returned[dict_base], dict_more, value)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned[dict_base].update(x)
    #
    # Returns dictionary that was updated using the dot notation and its value
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
