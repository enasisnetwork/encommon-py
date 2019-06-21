#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                           Generating Hashes #
#==============================================================================#
# Required Libraries and Configuration                                         #
# : Library Import and Global Variables                                        #
#------------------------------------------------------------------------------#
# Python Functions for Generating Hashes                                       #
# : Generate Hashes from Values                                    makehash(2) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Required Libraries and Configuration                                         #
#------------------------------------------------------------------------------#
#
#~~ Library Import and Global Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Import libraries that should be present in the virtual or system environment
#-----------------------------------------------------------------------------
from base64 import b64encode as base64_b64encode
from hashlib import sha1 as hashlib_sha1
from hashlib import sha256 as hashlib_sha256
from hashlib import sha512 as hashlib_sha512
from uuid import uuid3 as uuid_uuid3
from uuid import NAMESPACE_DNS as uuid_NAMESPACE_DNS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# Python Functions for Generating Hashes                                       #
#------------------------------------------------------------------------------#
#
#~~ Generate Hashes from Values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generate a new hash in the desired format using the specified value for seed
#-----------------------------------------------------------------------------
# source [RETURNED] [STRING]
#   String that will be used in seeding the hash generation procedure function
#-----------------------------------------------------------------------------
# convert [RETURNED] [STRING]
#   Which type of manipulation or conversion to be performed and sources value
#     * sha256  * sha256_crypt  * sha512  * sha512_crypt  * uuid  * apache
#-----------------------------------------------------------------------------
# Returns appropriately generated hash using the content from source parameter
#-----------------------------------------------------------------------------
def makehash(source, convert):
    #
    # Initial section for instantizing variables expected by remaining routine
    returned = str()
    #
    # Normalize the input parameters for simplifying the downstream procedures
    source_encoded = source.encode("utf-8")
    #
    # Generate a new hash in desired format using the specified value for seed
    excepted = "Failed when generating specified hash from input source value"
    if convert == "sha256":
        try: x = hashlib_sha256(source_encoded).hexdigest()
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if convert == "sha256_crypt":
        try: x = "$1${0}".format(hashlib_sha256(source_encoded).hexdigest())
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Generate a new hash in desired format using the specified value for seed
    excepted = "Failed when generating specified hash from input source value"
    if convert == "sha512":
        try: x = hashlib_sha512(source_encoded).hexdigest()
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if convert == "sha512_crypt":
        try: x = "$6${0}".format(hashlib_sha512(source_encoded).hexdigest())
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    #
    # Generate a new hash in desired format using the specified value for seed
    excepted = "Failed when generating specified hash from input source value"
    if convert == "uuid":
        try: x = str(uuid_uuid3(uuid_NAMESPACE_DNS, source))
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x
    if convert == "apache":
        try: x = base64_b64encode(hashlib_sha1(source_encoded).digest())
        except Exception as reason: raise Exception(excepted) from reason
        else: returned = x.decode("utf-8")
    #
    # Returns appropriately generated hash using content from source parameter
    return returned
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
