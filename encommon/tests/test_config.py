#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                Configuration and Validation #
#==============================================================================#
# Primary Functions for Configuration and Validation                           #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Load the Configuration Contents                                config_load #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Validate the Configuration Contents                        config_validate #
#==============================================================================#


#------------------------------------------------------------------------------#
# Primary Functions for Configuration and Validation                           #
#------------------------------------------------------------------------------#
#
#~~ Load the Configuration Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Load the specified configuration path and optionally enumerate the directory
#-----------------------------------------------------------------------------
def test_config_load(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.config import config_load
    from encommon.readwrite import writefile
    from os import makedirs as os_makedirs
    from os import path as os_path
    from yaml import dump as yaml_dump
    #
    # Create the expected directory structure for the configuration validation
    os_makedirs(os_path.join(tmp_path, "folder"))
    #
    # Initial section for instantizing variables expected by remaining routine
    expect = {"base": {"k": "v"}, "folder": {"file": {"subset": {"k": "v"}}}}
    #
    # Write the initial content to the various files using temporary directory
    file_path = os_path.join(tmp_path, "base.yml")
    writefile(file_path, yaml_dump({"k": "v"}), truncate=True)
    file_path = os_path.join(tmp_path, "folder", "file.subset.yml")
    writefile(file_path, yaml_dump({"k": "v"}), truncate=True)
    #
    # Load and parse the YAML configuration enumerating additional directories
    config = config_load(tmp_path)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert config["base"]["k"] == "v"
    assert config["folder"]["file"]["subset"]["k"] == "v"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Validate the Configuration Contents ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate the configuration contents that were loaded by the loading function
#-----------------------------------------------------------------------------
def test_config_validate(tmp_path):
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.config import config_validate
    #
    # Initial section for instantizing variables expected by remaining routine
    config = {"base": {"k": "v"}, "folder": {"file": {"subset": {"k": "v"}}}}
    checks = [
        ("base", {"k": "v"}),
        ("base.k", 123),
        ("folder.file.subset", {"k": "v"}),
        ("folder.file.subset.k", "v"),
        ("folder.file.subset.k", '^v$')]
    #
    # Validate configuration contents that were loaded by the loading function
    validate = config_validate(config, checks)
    #
    # Assert the relevant conditions indicating either test success or failure
    assert validate["failure"] == ["base.k"]
    assert "base" in validate["success"]
    assert "folder.file.subset" in validate["success"]
    assert "folder.file.subset.k" in validate["success"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
