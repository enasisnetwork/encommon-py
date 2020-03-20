#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                         Pickle Manipulation #
#==============================================================================#
# Primary Functions for Pickle Manipulation                                    #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Populate the Pickle Contents                                    savepickle #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Collect the Pickle Contents                                     loadpickle #
#==============================================================================#


#------------------------------------------------------------------------------#
# Primary Functions for Pickle Manipulation                                    #
#------------------------------------------------------------------------------#
#
#~~ Populate the Pickle Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Populate the serialized content to the pickle with provided file system path
#-----------------------------------------------------------------------------
def test_savepickle(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from os import path as os_path
    from encommon.pickles import savepickle
    from encommon.pickles import loadpickle
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"key": "value", "another": {"key": ["value1", "value2"]}}
    target = os_path.join(tmp_path, "_test_savepickle")
    #
    # Execute function being tested in a sane way consistent with normal usage
    savepickle(target, source)
    contents = loadpickle(target)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert contents == source
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Collect the Pickle Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Collects the serialized content of the pickle from provided file system path
#-----------------------------------------------------------------------------
def test_loadpickle(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from os import path as os_path
    from encommon.pickles import savepickle
    from encommon.pickles import loadpickle
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"key": "value", "another": {"key": ["value1", "value2"]}}
    target = os_path.join(tmp_path, "_test_loadpickle")
    #
    # Execute function being tested in a sane way consistent with normal usage
    savepickle(target, source)
    contents = loadpickle(target)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert contents == source
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
