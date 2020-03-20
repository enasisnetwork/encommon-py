#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                     Dictionary Manipulation #
#==============================================================================#
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
# Primary Functions for Dictionary Manipulation                                #
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
#~~ Flatten the Nested Dictionary ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flattens nested dictionary of dictionaries, lists, strings, and other values
#-----------------------------------------------------------------------------
def test_dictflatten():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictflatten
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"foo": {"bar": {"baz": {"bop": "beep"}}}, "boo": "bee"}
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictflatten(source)["foo_bar_baz_bop"] == "beep"
    assert dictflatten(source)["boo"] == "bee"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Get Value from Dictionary with Dot Notation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Process dictionary returning the appropriate value based on the dot notation
#-----------------------------------------------------------------------------
def test_dictnoget():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictnoget
    #
    # Initial section for instantizing variables expected by remaining routine
    source = {"foo": {"bar": {"baz": {"bop": "beep"}}}, "boo": "bee"}
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictnoget(source, "foo.bar.baz.bop") == "beep"
    assert dictnoget(source, "foo.bar.baz") == {"bop": "beep"}
    assert dictnoget(source, "boo") == "bee"
    assert dictnoget(source, "does.not.exist") == dict()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Set Value in Dictionary with Dot Notation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Update or create the dictionary structure or value based on the dot notation
#-----------------------------------------------------------------------------
def test_dictnoset():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.dicts import dictnoset
    #
    # Initial section for instantizing variables expected by remaining routine
    expect = {"key1": "value1", "key2": "value2", "key3": ["value3", "value4"]}
    expect_string = {**expect, **{"foo": {"bar": {"baz": "bop"}}}}
    expect_list = {**expect, **{"foo": {"bar": {"baz": ["bop", "beep"]}}}}
    expect_dict = {**expect, **{"foo": {"bar": {"baz": {"bop": "beep"}}}}}
    expect_bool = {**expect, **{"foo": {"bar": {"baz": {"bop": True}}}}}
    #
    # Assert the relevant conditions indicating either test success or failure
    assert dictnoset(expect, "foo", "bop") == {**expect, **{"foo": "bop"}}
    assert dictnoset(expect, "foo.bar.baz", "bop") == expect_string
    assert dictnoset(expect, "foo.bar.baz", ["bop", "beep"]) == expect_list
    assert dictnoset(expect, "foo.bar.baz", {"bop": "beep"}) == expect_dict
    assert dictnoset(expect, "foo.bar.baz.bop", True) == expect_bool
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
