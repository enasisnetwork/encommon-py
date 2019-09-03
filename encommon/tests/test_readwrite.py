#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                         Reading and Writing #
#==============================================================================#
# Python Functions for Reading and Writing                                     #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Simple File Writing                                              writefile #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Simple File Reading                                               readfile #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Locate Files and Directories                                     findfiles #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for Reading and Writing                                     #
#------------------------------------------------------------------------------#
#
#~~ Simple File Writing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Handle the simple file writing operations capturing and raising an exception
#-----------------------------------------------------------------------------
def test_writefile(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.readwrite import writefile
    from encommon.readwrite import readfile
    from os import path as os_path
    from os import remove as os_remove
    #
    # Initial section for instantizing variables expected by remaining routine
    string = "String which will be used for seeding the writefile function"
    target = os_path.join(tmp_path, "_test_writeout")
    #
    # Execute function being tested in a sane way consistent with normal usage
    writefile(target, string, truncate=True)
    contents = readfile(target)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert contents == string
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Simple File Reading ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Handle the simple file reading operations capturing and raising an exception
#-----------------------------------------------------------------------------
def test_readfile(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.readwrite import writefile
    from encommon.readwrite import readfile
    from os import path as os_path
    from os import remove as os_remove
    #
    # Initial section for instantizing variables expected by remaining routine
    string = "String which will be used for seeding the readfile function"
    target = os_path.join(tmp_path, "_test_readfile")
    #
    # Execute function being tested in a sane way consistent with normal usage
    writefile(target, string, truncate=True)
    contents = readfile(target)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert contents == string
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Locate Files and Directories ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Recursively find matching files and directories using the regular expression
#-----------------------------------------------------------------------------
def test_findfiles(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.readwrite import findfiles
    from encommon.readwrite import writefile
    from os import makedirs as os_makedirs
    from os import path as os_path
    #
    # Initial section for instantizing variables expected by remaining routine
    string = "String which will be used for seeding the findfiles function"
    expect = ["test.txt", "folder/test.txt"]
    #
    # Create an initial directory structure for parsing for various assertions
    os_makedirs(os_path.join(tmp_path, "folder", "another"), exist_ok=True)
    writefile(os_path.join(tmp_path, "test.txt"), string)
    writefile(os_path.join(tmp_path, "test.yml"), string)
    writefile(os_path.join(tmp_path, "folder", "test.txt"), string)
    writefile(os_path.join(tmp_path, "folder", "test.yml"), string)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert findfiles(tmp_path, r"\S+\/test.txt$") == expect
    assert findfiles(tmp_path, "*.txt") == expect
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
