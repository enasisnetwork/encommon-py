#==============================================================================#
# Enasis Network Common Libraries                                              #
# Python Functions                                             Time Processing #
#==============================================================================#
# Python Functions for Time Processing                                         #
# : Standard Time Converting                                     timeformat(2) #
#==============================================================================#


#------------------------------------------------------------------------------#
# Python Functions for Time Processing                                         #
#------------------------------------------------------------------------------#
#
#~~ Standard Time Converting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Conditionally perform the conversions to and from epoch and timestamp string
#-----------------------------------------------------------------------------
def test_timeformat():
    #
    # Import the module and functions relevant to this particular set of tests
    from encommon.times import timeformat
    #
    # Initial section for instantizing variables expected by remaining routine
    epoch = 1558763424
    stamp = "2019-05-25T05:50:24"
    #
    # Assert the relevant conditions indicating either test success or failure
    assert timeformat(epoch, "%Y-%m-%dT%H:%M:%S")[1] == stamp
    assert timeformat(stamp, "%Y-%m-%dT%H:%M:%S")[0] == epoch
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#------------------------------------------------------------------------------#
