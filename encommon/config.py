#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                Configuration and Validation #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Primary Functions for Configuration and Validation                           #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Load the Configuration Contents                                config_load #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Validate the Configuration Contents                        config_validate #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Standard Initialization for Logging                         config_logging #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from glob import glob as glob_glob
from logging import basicConfig as logging_basicConfig
from logging import getLogger as logging_getLogger
from logging import StreamHandler as logging_StreamHandler
from logging import Formatter as logging_Formatter
from os import path as os_path
from re import sub as re_sub
from re import match as re_match
from yaml import load as yaml_load
from yaml import Loader as yaml_Loader
#-----------------------------------------------------------------------------
# Import the additional libraries which are components of the project software
#-----------------------------------------------------------------------------
from encommon.dicts import dictnoset
from encommon.dicts import dictnoget
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Primary Functions for Configuration and Validation                           #
#------------------------------------------------------------------------------#
#
#~~ Load the Configuration Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Load the specified configuration path and optionally enumerate the directory
#-----------------------------------------------------------------------------
# config_path [REQUIRED] [STRING]
#   Complete or relative file system path for the configuration file or folder
#-----------------------------------------------------------------------------
# enumerate [OPTIONAL] [BOOLEAN]
#   Determines when directory where configuration is stored will be enumerated
#-----------------------------------------------------------------------------
# Returns the global configuration dictionary populated with the specifed file
#-----------------------------------------------------------------------------
def config_load(config_path, enumerate=False):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = dict()
    iterated = list()
    #
    # Determine the base directory path while raising exception when not exist
    if os_path.isfile(config_path): base_path = os_path.dirname(config_path)
    elif os_path.isdir(config_path): base_path = config_path
    else: raise Exception('Not found or unreadable ({0})'.format(config_path))
    #
    # Advanced isolated helper functions for simplifying the remaining routine
    def _notaget(path): return re_sub(r'/', ".", re_sub(r'\.yml$', "", path))
    #
    # Normalize the input parameters for simplifying the downstream procedures
    enumerate = True if os_path.isdir(config_path) else enumerate
    #
    # Load and parse the YAML configuration file specified capturing exception
    if os_path.isfile(config_path):
        excepted = 'Cannot load or parse the config ({0})'.format(config_path)
        try: x = yaml_load(open(config_path, "r"), Loader=yaml_Loader)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned.update(x if x is not None and len(x) >= 1 else dict())
    #
    # Walking expected configuration directory structure loading configuration
    if isinstance(enumerate, bool) and enumerate:
        file_glob = glob_glob(os_path.join(base_path, "*.yml"))
        file_glob.extend(glob_glob(os_path.join(base_path, "*", "*.yml")))
        for file in file_glob:
            config = config_load(os_path.join(base_path, file))
            key = _notaget(re_sub('^{0}/?'.format(base_path), str(), file))
            returned.update(dictnoset(returned, key, config))
    #
    # Returns the global configuration dictionary populated with specifed file
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Validate the Configuration Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate the configuration contents that were loaded by the loading function
#-----------------------------------------------------------------------------
# config [REQUIRED] [DICTIONARY]
#   Complete parsed dictionary populated by the configuration loading function
#-----------------------------------------------------------------------------
# validation [REQUIRED] [LIST]
#   List of simple key value dictionary with dot notation keys and expressions
#-----------------------------------------------------------------------------
# Returns the lists of failures and successful dictionary notation validations
#-----------------------------------------------------------------------------
def config_validate(config, validation):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = {"success": list(), "failure": list()}
    #
    # Iterate the validations populating into the relevant dictionary sub list
    for check in validation:
        value = str(dictnoget(config, check[0]))
        if str(check[1]) == value: returned["success"].append(check[0])
        elif re_match(str(check[1]), value): returned["success"].append(check[0])
        else: returned["failure"].append(check[0])
    #
    # Returns lists of failures and successful dictionary notation validations
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Standard Initialization for Logging ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Initialize the logging configuration using provided configuration dictionary
#-----------------------------------------------------------------------------
# config [REQUIRED] [DICTIONARY]
#   Complete dictionary for the Security Alpha configuration including logging
#-----------------------------------------------------------------------------
# console_mode [OPTIONAL] [BOOLEAN]
#   Sends the logging standard output to the console in addition with log file
#-----------------------------------------------------------------------------
# level [OPTIONAL] [INTEGER]
#   Define parameter value for passing to the built in Python logging function
#-----------------------------------------------------------------------------
# file_path [OPTIONAL] [STRING]
#   Define parameter value for passing to the built in Python logging function
#-----------------------------------------------------------------------------
# format [OPTIONAL] [STRING]
#   Define parameter value for passing to the built in Python logging function
#-----------------------------------------------------------------------------
# Returns the constructed logging resource handler defined using configuration
#-----------------------------------------------------------------------------
def config_logging(config, console_mode=False, level=20, file_path=None,
  format='[%(asctime)s] [%(levelname)s] %(message)s'):
    #
    # Define the logging configuration parameters with the basic configuration
    loggered = logging_getLogger()
    logging_basicConfig(level=level, filename=file_path, format=format)
    #
    # Creates logging handler for console debug output when argument specified
    if isinstance(console_mode, bool) and console_mode:
        consoled = logging_StreamHandler()
        template = logging_Formatter(format)
        consoled.setFormatter(template)
        loggered.addHandler(consoled)
    #
    # Returns constructed logging resource handler defined using configuration
    return loggered
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
