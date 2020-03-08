#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                          Network Addressing #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
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
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from netaddr import IPNetwork as netaddr_ipnetwork
from netaddr import IPAddress as netaddr_ipaddress
from re import match as re_match
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Python Functions for Network Addressing                                      #
#------------------------------------------------------------------------------#
#
#~~ Manipulate an IPv4 Network Address ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert the specified IPv4 network address using the intended network format
#-----------------------------------------------------------------------------
# source [REQUIRED] [STRING]
#  Network address in the IPv4 format that will be converted to desired format
#-----------------------------------------------------------------------------
# format [REQUIRED] [STRING]
#  Desired target converted format that includes several options which include
#    * address       12.34.56.7           * network       12.34.56.0
#    * address_cidr  12.34.56.7/24        * network_cidr  12.34.56.0/24
#    * address_host  12.34.56.7/32        * network_zero  12.34.56.0
#    * broadcast     12.34.56.255         * netmask       255.255.255.0
#    * address_mac   01:20:34:05:60:07    * reversed      7.56.34.12
#-----------------------------------------------------------------------------
# Returns the newly converted addressing for source and desired address format
#-----------------------------------------------------------------------------
def ipv4format(source, format):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = str()
    #
    # Convert specified IPv4 network address using the intended network format
    excepted = "failed to convert and format the source address into intended"
    if format == "address":
        try: x = str(netaddr_ipnetwork(source).ip)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if format == "address_cidr":
        try: x = str(netaddr_ipnetwork(source).prefixlen)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = "{0}/{1}".format(ipv4format(source, "address"), x)
    if format == "address_host":
        try: x = "{0}/32".format(str(netaddr_ipnetwork(source).ip))
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Convert specified IPv4 network address using the intended network format
    excepted = "failed to convert and format the source address into intended"
    if format == "network":
        try: x = str(netaddr_ipnetwork(source).network)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if format == "network_cidr":
        try: x = str(netaddr_ipnetwork(source).prefixlen)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = "{0}/{1}".format(ipv4format(source, "network"), x)
    if format == "network_zero":
        try: x = str(netaddr_ipnetwork(source).network)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Convert specified IPv4 network address using the intended network format
    excepted = "failed to convert and format the source address into intended"
    if format == "broadcast":
        try: x = str(netaddr_ipnetwork(source).broadcast)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if format == "netmask":
        try: x = str(netaddr_ipnetwork(source).netmask)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Convert specified IPv4 network address using the intended network format
    excepted = "failed to convert and format the source address into intended"
    if format == "address_mac":
        address = ipv4format(source, "address")
        try:
            x = str().join([str(x.zfill(3)) for x in address.split(".")])
            y = '{0}:{1}:{2}:{3}:{4}:{5}'
            x = y.format(x[0:2], x[2:4], x[4:6], x[6:8], x[8:10], x[10:12])
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Convert specified IPv4 network address using the intended network format
    if format == "reversed":
        address = ipv4format(source, "address")
        try:
            x = address.split(".")
            x = ".".join([x[3], x[2], x[1], x[0]])
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Returns newly converted addressing for source and desired address format
    return returned
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
# value [REQUIRED] [STRING]
#   String based value that is parsed and processed determining when validated
#-----------------------------------------------------------------------------
# Returns the correct boolean indicating whether or not the value is validated
#-----------------------------------------------------------------------------
def str_ipv4_isvalid(value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    matching = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
    matching += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    #
    # Validate that IP address is within the boundary the octect values permit
    if re_match(matching, str(value)): returned = True
    else: returned = False
    #
    # Returns correct boolean indicating whether or not the value is validated
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Public ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundary of public IP assignments
#-----------------------------------------------------------------------------
# value [REQUIRED] [STRING]
#   String based value that is parsed and processed determining when validated
#-----------------------------------------------------------------------------
# Returns the correct boolean indicating whether or not the value is validated
#-----------------------------------------------------------------------------
def str_ipv4_ispublic(value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    #
    # Validate that IP address is within the boundary of public IP assignments
    if not str_ipv4_isvalid(value): returned = False
    elif str_ipv4_isrfc1918(value): returned = False
    elif str_ipv4_islinklocal(value): returned = False
    elif str_ipv4_islocalhost(value): returned = False
    else: returned = True
    #
    # Returns correct boolean indicating whether or not the value is validated
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is RFC1918 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within the boundaries of what RFC1918 define
#-----------------------------------------------------------------------------
# value [REQUIRED] [STRING]
#   String based value that is parsed and processed determining when validated
#-----------------------------------------------------------------------------
# Returns the correct boolean indicating whether or not the value is validated
#-----------------------------------------------------------------------------
def str_ipv4_isrfc1918(value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    matching = r'^(10\.\d+\.\d+\.\d+)|(192\.168\.\d+\.\d+)'
    matching += r'|(172\.((1[6-9])|(2[0-9])|(3[0-1]))\.\d+\.\d+)$'
    #
    # Validate that IP address is within the boundaries of what RFC1918 define
    if not str_ipv4_isvalid(value): returned = False
    elif re_match(matching, str(value)): returned = True
    else: returned = False
    #
    # Returns correct boolean indicating whether or not the value is validated
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Link-Local ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for link-local address
#-----------------------------------------------------------------------------
# value [REQUIRED] [STRING]
#   String based value that is parsed and processed determining when validated
#-----------------------------------------------------------------------------
# Returns the correct boolean indicating whether or not the value is validated
#-----------------------------------------------------------------------------
def str_ipv4_islinklocal(value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    matching = r'^(169\.254\.\d+\.\d+)$'
    #
    # Validate that IP address is within specifications for link-local address
    if not str_ipv4_isvalid(value): returned = False
    elif re_match(matching, str(value)): returned = True
    else: returned = False
    #
    # Returns correct boolean indicating whether or not the value is validated
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#~~ Check IP Address is Localhost ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Validate that the IP address is within specifications for loopback interface
#-----------------------------------------------------------------------------
# value [REQUIRED] [STRING]
#   String based value that is parsed and processed determining when validated
#-----------------------------------------------------------------------------
# Returns the correct boolean indicating whether or not the value is validated
#-----------------------------------------------------------------------------
def str_ipv4_islocalhost(value):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = None
    matching = r'^(127\.\d+\.\d+\.\d+)$'
    #
    # Validate that IP address is within specifications for link-local address
    if not str_ipv4_isvalid(value): returned = False
    elif re_match(matching, str(value)): returned = True
    else: returned = False
    #
    # Returns correct boolean indicating whether or not the value is validated
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
