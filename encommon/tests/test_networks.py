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
# : Check IP Address is Valid                                 str_ipv4_isvalid #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is Public                               str_ipv4_ispublic #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is RFC1918                             str_ipv4_isrfc1918 #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is Link-Local                        str_ipv4_islinklocal #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Check IP Address is Localhost                         str_ipv4_islocalhost #
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
#~~ Check IP Address is Valid ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundary the octect values permit
#-----------------------------------------------------------------------------
def test_str_ipv4_isvalid():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ipv4_isvalid
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ipv4_isvalid("0.0.0.0") == True
    assert str_ipv4_isvalid("127.0.0.1") == True
    assert str_ipv4_isvalid("192.168.123.45") == True
    assert str_ipv4_isvalid("169.254.123.45") == True
    assert str_ipv4_isvalid("256.256.256.256") == False
    assert str_ipv4_isvalid("208.67.222.222") == True
    assert str_ipv4_isvalid("208.67.220.220") == True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Public ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundary of public IP assignments
#-----------------------------------------------------------------------------
def test_str_ipv4_ispublic():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ipv4_ispublic
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ipv4_ispublic("0.0.0.0") == True
    assert str_ipv4_ispublic("127.0.0.1") == False
    assert str_ipv4_ispublic("192.168.123.45") == False
    assert str_ipv4_ispublic("169.254.123.45") == False
    assert str_ipv4_ispublic("256.256.256.256") == False
    assert str_ipv4_ispublic("208.67.222.222") == True
    assert str_ipv4_ispublic("208.67.220.220") == True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is RFC1918 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundaries of what RFC1918 define
#-----------------------------------------------------------------------------
def test_str_ipv4_isrfc1918():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ipv4_isrfc1918
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ipv4_isrfc1918("0.0.0.0") == False
    assert str_ipv4_isrfc1918("127.0.0.1") == False
    assert str_ipv4_isrfc1918("192.168.123.45") == True
    assert str_ipv4_isrfc1918("169.254.123.45") == False
    assert str_ipv4_isrfc1918("256.256.256.256") == False
    assert str_ipv4_isrfc1918("208.67.222.222") == False
    assert str_ipv4_isrfc1918("208.67.220.220") == False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Link-Local ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for link-local address
#-----------------------------------------------------------------------------
def test_str_ipv4_islinklocal():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ipv4_islinklocal
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ipv4_islinklocal("0.0.0.0") == False
    assert str_ipv4_islinklocal("127.0.0.1") == False
    assert str_ipv4_islinklocal("192.168.123.45") == False
    assert str_ipv4_islinklocal("169.254.123.45") == True
    assert str_ipv4_islinklocal("256.256.256.256") == False
    assert str_ipv4_islinklocal("208.67.222.222") == False
    assert str_ipv4_islinklocal("208.67.220.220") == False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Localhost ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for loopback interface
#-----------------------------------------------------------------------------
def test_str_ipv4_islocalhost():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.networks import str_ipv4_islocalhost
    #
    # Assert the relevant conditions indicating either test success or failure
    assert str_ipv4_islocalhost("0.0.0.0") == False
    assert str_ipv4_islocalhost("127.0.0.1") == True
    assert str_ipv4_islocalhost("192.168.123.45") == False
    assert str_ipv4_islocalhost("169.254.123.45") == False
    assert str_ipv4_islocalhost("256.256.256.256") == False
    assert str_ipv4_islocalhost("208.67.222.222") == False
    assert str_ipv4_islocalhost("208.67.220.220") == False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
