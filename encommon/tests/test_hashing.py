#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                           Generating Hashes #
#==============================================================================#
# Python Functions for Generating Hashes                                       #
# : Generate Hashes from Values                                    makehash(2) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for Generating Hashes                                       #
#------------------------------------------------------------------------------#
#
#~~ Generate Hashes from Values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generate a new hash in the desired format using the specified value for seed
#-----------------------------------------------------------------------------
def test_makehash():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.hashing import makehash
    from re import match as re_match
    #
    # Initial section for instantizing variables expected by remaining routine
    string = "String which will be used for seeding the makehash function"
    expect_sha256 = r"218bc7800a2491fdeca0da24a8.+?d440a2324d32d9b18fb0953836"
    expect_sha256_crypt = r"\$1\${0}".format(expect_sha256)
    expect_sha512 = r"fb61f41be93de0eab9fd66b079.+?c1533cb5858a484554f1b13745"
    expect_sha512_crypt = r"\$6\${0}".format(expect_sha512)
    expect_uuid = "a00e35e0-552d-3d8c-be56-666a2f755e4c"
    expect_apache = "F6UGJCxulUMvPz7PxX625XcqfZs="
    #
    # Assert the relevant conditions indicating either test success or failure
    assert re_match(expect_sha256, makehash(string, "sha256"))
    assert re_match(expect_sha256_crypt, makehash(string, "sha256_crypt"))
    assert re_match(expect_sha512, makehash(string, "sha512"))
    assert re_match(expect_sha512_crypt, makehash(string, "sha512_crypt"))
    assert makehash(string, "uuid") == expect_uuid
    assert makehash(string, "apache") == expect_apache
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
