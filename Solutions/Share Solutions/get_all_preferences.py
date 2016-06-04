loadModule('/System/Scripting')
include('workspace://Utilities/java_array.py')
Platform = org.eclipse.core.runtime.Platform

# Make a copy of all preferences to a Java Properties
prefService = Platform.getPreferencesService()
baos = java.io.ByteArrayOutputStream()
prefService.exportPreferences(prefService.getRootNode(), baos, None)

bais = java.io.ByteArrayInputStream(baos.toByteArray())
properties = java.util.Properties()
properties.load(bais)

# get the last saved value
last_properties = getSharedObject("all_prefs_cache")

# save it again as a shared object, permanently so other script engines can access
# and writeable so it can overridden later
setSharedObject("all_prefs_cache", properties, True, True)

if last_properties:
    was = dict(last_properties)
    now = dict(properties)

    # use unique sentinel rather than default of None as value of dict could be None
    sentinel = object()
    for k, now_v in now.items():
        was_v = was.pop(k, sentinel)
        if was_v is sentinel:
            print("Added: {} now {}".format(k, now_v))
        elif was_v != now_v:
            print("Change: {} was {} now {}".format(k, was_v, now_v))
    for k, was_v in was.items():
        print("Removed: {} was {}".format(k, was_v))
    print("Done showing changes in preferences")
else:
    print("Make some changes to properties and run again to see the differences")
