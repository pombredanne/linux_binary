from collections import OrderedDict

def dict_variables(rd, sv, name):
    return {
        "RELEASE_DATE": rd,
        "SHORT_STRING": "".join(sv),
        "SHORT_VERSION": ".".join(str(int(x)) for x in sv if int(x)),
        "NAME": name,
    }

VERSIONS = OrderedDict([
    ('3.14.5', dict_variables("201405311735", ("03", "14", "05"), "utopic")),
    ('3.14.6', dict_variables("201406071635", ("03", "14", "06"), "utopic")),
    ('3.14.7', dict_variables("201406111644", ("03", "14", "07"), "utopic")),
    ('3.14.8', dict_variables("201406161755", ("03", "14", "08"), "utopic")),
    ('3.14.9', dict_variables("201406261553", ("03", "14", "09"), "utopic")),
    ('3.14.10', dict_variables("201406302353", ("03", "14", "10"), "utopic")),
    ('3.14.11', dict_variables("201407062254", ("03", "14", "11"), "utopic")),
    ('3.14.12', dict_variables("201407091455", ("03", "14", "12"), "utopic")),
    ('3.14.13', dict_variables("201407171953", ("03", "14", "13"), "utopic")),
    ('3.14.14', dict_variables("201407281153", ("03", "14", "14"), "utopic")),
    ('3.14.15', dict_variables("201407311853", ("03", "14", "15"), "utopic")),
    ('3.14.16', dict_variables("201408072035", ("03", "14", "16"), "utopic")),
    ('3.14.17', dict_variables("201408132253", ("03", "14", "17"), "utopic")),
    ('3.15.1', dict_variables("201406161841", ("03", "15", "01"), "utopic")),
    ('3.15.2', dict_variables("201406261639", ("03", "15", "02"), "utopic")),
    ('3.15.3', dict_variables("201407010040", ("03", "15", "03"), "utopic")),
    ('3.15.4', dict_variables("201407062345", ("03", "15", "04"), "utopic")),
    ('3.15.5', dict_variables("201407091543", ("03", "15", "05"), "utopic")),
    ('3.15.6', dict_variables("201407172034", ("03", "15", "06"), "utopic")),
    ('3.15.7', dict_variables("201407281235", ("03", "15", "07"), "utopic")),
    ('3.15.8', dict_variables("201407091543", ("03", "15", "08"), "utopic")),
    ('3.15.9', dict_variables("201408072114", ("03", "15", "09"), "utopic")),
    ('3.15.10', dict_variables("201408132333", ("03", "15", "10"), "utopic")),
    ('3.16.1', dict_variables("201408140014", ("03", "16", "01"), "utopic")),
    ('3.16.2', dict_variables("201409052035", ("03", "16", "02"), "utopic")),
    ('3.16.3', dict_variables("201409171435", ("03", "16", "03"), "utopic")),
    ('3.17.0', dict_variables("201410060605", ("03", "17", "00"), "utopic")),
    ('3.17.1', dict_variables("201410150735", ("03", "17", "01"), "utopic")),
    ('3.17.2', dict_variables("201410301416", ("03", "17", "02"), "vivid")),
    ('3.17.3', dict_variables("201411141335", ("03", "17", "03"), "vivid")),
    ('3.17.4', dict_variables("201411211317", ("03", "17", "04"), "vivid")),
    ('3.17.5', dict_variables("201412070036", ("03", "17", "05"), "vivid")),
    ('3.17.6', dict_variables("201412071535", ("03", "17", "06"), "vivid")),
    ('3.18.0', dict_variables("201412071935", ("03", "18", "00"), "vivid")),
    ('3.18.1', dict_variables("201412170637", ("03", "18", "01"), "vivid")),
    ('3.18.2', dict_variables("201501082011", ("03", "18", "02"), "vivid")),
    ('3.18.3', dict_variables("201501161810", ("03", "18", "03"), "vivid")),
    ('3.18.4', dict_variables("201501271243", ("03", "18", "04"), "vivid")),
    ('3.18.5', dict_variables("201501292218", ("03", "18", "05"), "vivid")),
    ('3.18.6', dict_variables("201502061036", ("03", "18", "06"), "vivid")),
    ('3.18.7', dict_variables("201502110759", ("03", "18", "07"), "vivid")),
    ('3.18.8', dict_variables("201502271935", ("03", "18", "08"), "vivid")),
    ('3.18.9', dict_variables("201503080036", ("03", "18", "09"), "vivid")),
    ('3.18.10', dict_variables("201503241436", ("03", "18", "10"), "vivid")),
    ('3.18.11', dict_variables("201504041535", ("03", "18", "11"), "vivid")),
    ('3.19.0', dict_variables("201502091451", ("03", "19", "00"), "vivid")),
    ('3.19.1', dict_variables("201503080052", ("03", "19", "01"), "vivid")),
    ('3.19.2', dict_variables("201503181436", ("03", "19", "02"), "vivid")),
    ('3.19.3', dict_variables("201503261036", ("03", "19", "03"), "vivid")),
])
