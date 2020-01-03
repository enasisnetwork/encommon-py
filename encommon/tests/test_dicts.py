#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                     Dictionary Manipulation #
#==============================================================================#
# Python Functions for Dictionary Manipulation                                 #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : List of Dictionaries to Dictionary                             dictstodict #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Sort List of Dictionaries                                        dictssort #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Reorder Dictionary of Dictionaries                               dictksort #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Dictionary Value from Dot-Notation                            dictnotation #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for Dictionary Manipulation                                 #
#------------------------------------------------------------------------------#
#
#~~ List of Dictionaries to Dictionary ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Process the list of dictionaries into a single dictionary updating for merge
#-----------------------------------------------------------------------------
def test_dictstodict():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictstodict
    #
    # Initial section for instantizing variables expected by remaining routine
    source = [{"a": {"foo": "bar"}}, {"c": {"bar": "foo", "bop": "beep"}}]
    expect = {"a": {"foo": "bar"}, "c": {"bar": "foo", "bop": "beep"}}
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictstodict(source) == expect
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Sort List of Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reorder the list of dictionaries on specified keys value from the dictionary
#-----------------------------------------------------------------------------
def test_dictssort():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictssort
    #
    # Initial section for instantizing variables expected by remaining routine
    source = [{"foo": "bar", "sort": 1}, {"foo": "baz", "sort": 2}]
    expect_asc = [{"foo": "bar", "sort": 1}, {"foo": "baz", "sort": 2}]
    expect_desc = [{"foo": "baz", "sort": 2}, {"foo": "bar", "sort": 1}]
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictssort(source, ("sort", "asc")) == expect_asc
    assert dictssort(source, ("sort", "desc")) == expect_desc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Reorder Dictionary of Dictionaries ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reorder the dict of dictionaries on specified keys value from the dictionary
#-----------------------------------------------------------------------------
def test_dictksort():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictksort
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"foo": {"sort": 1}, "bar": {"sort": 2}}
    expect_asc = ["foo", "bar"]
    expect_desc = ["bar", "foo"]
    #
    # Assert the relevant conditions indicating either test success or failure
    assert list(dictksort(source, ("sort", "asc")).keys()) == expect_asc
    assert list(dictksort(source, ("sort", "desc")).keys()) == expect_desc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Dictionary Value from Dot-Notation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Process dictionary returning the appropriate value based on the dot notation
#-----------------------------------------------------------------------------
def test_dictnotation():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictnotation
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"foo": {"bar": {"baz": {"bop": "beep"}}}, "boo": "bee"}
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictnotation(source, "foo.bar.baz.bop") == "beep"
    assert dictnotation(source, "foo.bar.baz") == {"bop": "beep"}
    assert dictnotation(source, "boo") == "bee"
    assert dictnotation(source, "does.not.exist") == dict()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
