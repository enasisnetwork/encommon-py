#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                          Network Addressing #
#==============================================================================#
# Python Functions for Network Addressing                                      #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Manipulate an IPv4 Network Address                              ipv4format #
#------------------------------------------------------------------------------#
# Simplistic Utilities for Network Addressing                                  #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is RFC1918                               str_ip_isrfc1918 #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is Link-Local                          str_ip_islinklocal #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is Localhost                           str_ip_islocalhost #
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
    assert ipv4format("12.34.56.7/24", "address_mac") == "01:20:34:05:60:07"
    assert ipv4format("12.34.56.7/24", "reversed") == "7.56.34.12"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Simplistic Utilities for Network Addressing                                  #
#------------------------------------------------------------------------------#
#
#~~ Check IP Address is RFC1918 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundaries of what RFC1918 define
#-----------------------------------------------------------------------------
def test_str_ip_isrfc1918():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ip_isrfc1918
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ip_isrfc1918("127.0.0.1") ==  False
    assert str_ip_isrfc1918("192.168.123.45") == True
    assert str_ip_isrfc1918("169.254.123.45") == False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Link-Local ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for link-local address
#-----------------------------------------------------------------------------
def test_str_ip_islinklocal():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ip_islinklocal
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ip_islinklocal("127.0.0.1") ==  False
    assert str_ip_islinklocal("192.168.123.45") == False
    assert str_ip_islinklocal("169.254.123.45") == True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Localhost ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for loopback interface
#-----------------------------------------------------------------------------
def test_str_ip_islocalhost():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ip_islocalhost
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ip_islocalhost("127.0.0.1") == True
    assert str_ip_islocalhost("192.168.123.45") == False
    assert str_ip_islocalhost("169.254.123.45") == False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
