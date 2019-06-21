#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                           List Manipulation #
#==============================================================================#
# Python Functions for List Manipulation                                       #
# : Search List with Expressions                                 listsearch(2) #
# : Deduplicate Redundant List Contents                           listdedup(1) #
# : Flatten Multiple Depths of Lists                            listflatten(1) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for List Manipulation                                       #
#------------------------------------------------------------------------------#
#
#~~ Search List with Expressions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Filter the specified source list contents using provided regular expressions
#-----------------------------------------------------------------------------
def test_listsearch():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.lists import listsearch
    #
    # Initial section for instantizing variables expected by remaining routine
    source = ["foo", "foo", "bar", "bork", "beep", "bop"]
    regexp = "^((foo)|(bar)|(bop))$"
    expect = ["bar", "bop", "foo", "foo"]
    #
    # Assert the relevant conditions indicating either test success or failure
    assert sorted(listsearch(source, regexp)) == expect
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Deduplicate Redundant List Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove any case sensitivite duplicative and redundant items from source list
#-----------------------------------------------------------------------------
def test_listdedup():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.lists import listdedup
    #
    # Initial section for instantizing variables expected by remaining routine
    source = ["foo", "foo", "bar", "bork", "beep", "bop"]
    expect = ["bar", "beep", "bop", "bork", "foo"]
    #
    # Assert the relevant conditions indicating either test success or failure
    assert sorted(listdedup(source)) == expect
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Flatten Multiple Depths of Lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert the multiple lists of varying depths into a unique single depth list
#-----------------------------------------------------------------------------
def test_listflatten():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.lists import listflatten
    #
    # Initial section for instantizing variables expected by remaining routine
    source = [["foo", "foo"], ["bar", ["bork", ["beep"]], "bop"]]
    expect = ["bar", "beep", "bop", "bork", "foo", "foo"]
    #
    # Assert the relevant conditions indicating either test success or failure
    assert sorted(listflatten(source)) == expect
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
