#qpy:console
'''for QPy can usage normal system python , gen. all need Adnorid /etc/profile
usage:
    - upload this script into mobile
    - normal in /storage/sdcard0/com.hipipal.qpyplus/projects/YouProject
    - call in QPython "My QPython->projects->YouProject->gen_qpy_env.py"
config as default env:
# mount -o remount,rw /dev/block/mtdblock3 /system
# ln -s /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profil /etc/profile
# mount -o remount,ro /dev/block/mtdblock3 /system
so every time restart SSH in Android, will load the /etc/profile
can test every thing is good now:
# python
Python 2.7.2 (default, Dec 27 2013, 23:19:48)
[GCC 4.6 20120106 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
'''
from os import environ as env
_exp = "/storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profile"
_pre = "export"

fd = open(_exp, "w")
fd.write("%s PATH=%s\n" % (_pre, env.get("PATH") ))

fd.write("%s PYTHONHOME=%s\n" % (_pre, env.get("PYTHONHOME") ))
fd.write("%s PYTHONPATH=%s\n" % (_pre, env.get("PYTHONPATH") ))
fd.write("%s PYTHONOPTIMIZE=%s\n" % (_pre, env.get("PYTHONOPTIMIZE") ))

fd.write("%s AP_HOST=%s\n" % (_pre, env.get("AP_HOST") ))
fd.write("%s AP_PORT=%s\n" % (_pre, env.get("AP_PORT") ))
fd.write("%s AP_HANDSHAKE=%s\n" % (_pre, env.get("AP_HANDSHAKE") ))

fd.write("%s ANDROID_PUBLIC=%s\n" % (_pre, env.get("ANDROID_PUBLIC") ))
fd.write("%s ANDROID_PRIVATE=%s\n" % (_pre, env.get("ANDROID_PRIVATE") ))
fd.write("%s ANDROID_ARGUMENT=%s\n" % (_pre, env.get("ANDROID_ARGUMENT") ))
fd.write("%s LD_LIBRARY_PATH=%s\n" % (_pre, env.get("LD_LIBRARY_PATH") ))
fd.write("%s TERM=%s\n" % (_pre, env.get("TERM") ))
fd.write("%s TMPDIR=%s\n" % (_pre, env.get("TMPDIR") ))

print '''gen all nedd env in qpy:console
exp. as %s
enjoy it ;-)
'''% _exp