type1 = {
    'libjiagu.so': ('Description: use obfuscator 360 jiagu'+'\n'+'malicious functions: int32_t _Z9__arm_a_2PcjS_Rii(int32_t a1, int32_t a2, int32_t a3, int32_t a4)'+'\n'+'int32_t _Z10__arm_a_20v(int32_t a1, int32_t a2, int32_t a3, int32_t a4, int32_t a5)'),
    'libdxarq.so': ('Description: allows anti-analysis operations'+'\n'+'malicious functions: public native int vxeg (Object [] p0)'),
    'libSecShell.so': ('Description: allows anti-debug operations, injects and hides a second dex file'+'\n'+'malicious functions: int __fastcall sub_7518394C(int result, _BYTE *a2, int a3)'),
    'libsec.so': ('Description: allows anti-debug operations')
}

type2 = {
    'libdaemon_api21.so': ('Description: creates a daemon process that collects information and sends it to a remote server'+'\n'+'malicious functions: int32_t get_name_by_pid(int32_t a1)'+'\n'+'int32_t lock_file(int32_t path)'),
    'libbackground_api.so': ('Description: libdaemon_api21 with a different name'),
    'libdaemon_new.so': ('Description: add to library libdaemon_api21 audio, video and camera management functions'),
    'libsoon.so': ('Description: performs remote operations (sending illegal sms, push notifications)'+'\n'+'malicious functions: _android_log_print(3, “INJECT”, “[+] Injecting process: %d\n”, a1)'),
    'libbinder.so': ('Description: keylogger'),
    'libdmv.so': ('Description: performs SQL injection and receives commands from a C&C'+'\n'+'malicious functions: _Z30dvmHeapSourceStartupBeforeForkv()'),
    'libTitaniumCore.so': ('Description: illegal sending of sms'+'\n'+'malicious functions: Java_com_Titanium_Synchronous_adipiscing_nativeadipiscing'),
    'libart.so': ('malicious functions: ZNK3art100atDexFile11GetOatClassEt+EDù'),
    'libAudio3.0.so': ('Description: takes complete control of the device'+'\n'+'malicious functions: _aebi_memcpy '),
    'librealtalk-jni.so': ('Description: opens a fake Google Play screen and gets credit card information'+'\n'+'malicious functions: nt _cdecl Java_com_abbamoney_Realtalk:getStartWebUrl(int a1)'),
    'libcsn.so': ('Description: get information about IMEI, phone number and contact list'+'\n'+'malicious functions: initDexOptDexLoad'),
    'libsharek.so': ('Description: get information'),
    'libMyGame.so': ('Description: get root permissions'+'\n'+'malicious functions: strcpy(&v32, "http://oymg.themdspts.")'+'\n'+'v18=strcat(&v32, "com/xyl/ji028/t.html")v19=curl_easy_init(v18)'),
    'libaddk.so': ('Description: keylogger'+'\n'+'malicious functions: ZNKandroid6Parcel4dataEv'),
    'libk.so': ('Description: keylogger')
}

type3 = {
    'liblocSDK7a.so': ('Description: obtains the geographical position and collects information on the device'+'\n'+'malicious functions: int32_t Java_com_baidu_location_Jni_a(int32_t a1, int32_t a2, int32_t a3, int32_t a4)'),
    'liblocSDK7b.so': ('Description: obtains the geographical position and collects information on the device'+'\n'+'malicious functions: int32_t Java_com_baidu_location_fused_sdk_Jni_b(int32_t a1, int32_t a2, int32_t a3, int32_t a4)'),
    'libindoor.so': ('Description: obtains the geographical position and collects information on the device'+'\n'+'malicious functions: int32_t Java_com_baidu_location_indoor_mapversion_IndoorJni_getVdrPfRes(int32_t a1)')
}