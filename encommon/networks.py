#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                          Network Addressing #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Python Functions for Network Addressing                                      #
# : Manipulate an IPv4 Network Address                           ipv4format(2) #
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
#-----------------------------------------------------------------------------
# Returns the newly converted addressing for source and desired address format
#-----------------------------------------------------------------------------
def ipv4format(source, format):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = str()
    #
    # Convert specified IPv4 network address using the intended network format
    excepted = "Failed to convert and format the source address into intended"
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
    excepted = "Failed to convert and format the source address into intended"
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
    excepted = "Failed to convert and format the source address into intended"
    if format == "broadcast":
        try: x = str(netaddr_ipnetwork(source).broadcast)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if format == "netmask":
        try: x = str(netaddr_ipnetwork(source).netmask)
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Returns newly converted addressing for source and desired address format
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
