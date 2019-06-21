#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                          Network Addressing #
#==============================================================================#
# Python Functions for Network Addressing                                      #
# : Manipulate an IPv4 Network Address                           ipv4format(2) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for Network Addressing                                      #
#------------------------------------------------------------------------------#
#
#~~ Manipulate an IPv4 Network Address ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert the specified IPv4 network address using the intended network format
#-----------------------------------------------------------------------------
def test_ipv4format():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import ipv4format
    #
    # Assert the relevant conditions indicating either test success or failure
    assert ipv4format("12.34.56.7/24", "address") == "12.34.56.7"
    assert ipv4format("12.34.56.7/24", "address_cidr") == "12.34.56.7/24"
    assert ipv4format("12.34.56.7/24", "address_host") == "12.34.56.7/32"
    assert ipv4format("12.34.56.7/24", "network") == "12.34.56.0"
    assert ipv4format("12.34.56.7/24", "network_cidr") == "12.34.56.0/24"
    assert ipv4format("12.34.56.7/24", "network_zero") == "12.34.56.0"
    assert ipv4format("12.34.56.7/24", "broadcast") == "12.34.56.255"
    assert ipv4format("12.34.56.7/24", "netmask") == "255.255.255.0"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
