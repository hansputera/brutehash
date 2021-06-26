import asyncio
import hashlib
import string
import itertools
import hashlib
import time
import bcrypt

# Decrypt: aaaaa
target = "f368a29b71bd201a7ef78b5df88b1361fbe83f959756d33793837a5d7b2eaf660f2f6c7e2fbace01965683c4cfafded3ff28aab34e329aa79bc81e7703f68b86"

def getElapsed(st: float):
    return time.strftime("%H:%M:%S", time.gmtime(time.monotonic() - st))

def allAplhabets():
    for size in itertools.count(1):
        for s in itertools.product(string.ascii_lowercase, repeat=size):
            yield "".join(s)

async def executeAll(tr):
    st = time.monotonic()
    for s in allAplhabets():
        md5 = hashlib.md5(bytes(s, encoding="utf-8")).hexdigest()
        sha256 = hashlib.sha256(bytes(s, encoding="utf-8")).hexdigest()
        sha384 = hashlib.sha384(bytes(s, encoding="utf-8")).hexdigest()
        sha224 = hashlib.sha224(bytes(s, encoding="utf-8")).hexdigest()
        sha1 = hashlib.sha1(bytes(s, encoding="utf-8")).hexdigest()
        sha512 = hashlib.sha512(bytes(s, encoding="utf-8")).hexdigest()
        
        bcrySalt = bcrypt.gensalt()
        bcry = bcrypt.hashpw(bytes(s, encoding="utf-8"), bcrySalt)
        print(f"{s} | [MD5: {md5}] [SHA256: {sha256}] [SHA384: {sha384}] [SHA224: {sha224}] [SHA1: {sha1}] [SHA512: {sha512}] [BCRYPT: {bcry.decode('utf-8')}]")
        if bcry.decode("utf-8") == target:
            print(f"'{target}' is Bcrypt algorithm | result: {s}")
            break
        elif md5 == tr:
            print(f"'{target}' is MD5 algorithm | result: {s}")
            break
        elif sha256 == tr:
            print(f"'{target}' is SHA256 algorithm | result: {s}")
            break
        elif sha384 == tr:
            print(f"'{target}' is SHA384 algorithm | result: {s}")
            break
        elif sha224 == tr:
            print(f"'{target}' is SHA224 algorithm | result: {s}")
            break
        elif sha1 == tr:
            print(f"'{target}' is SHA1 algorithm | result: {s}")
            break
        elif sha512 == tr:
            print(f"'{target}' is SHA512 algorithm | result: {s}")
    elapsed = getElapsed(st)
    print(f"Took: {elapsed}")

# MD5
async def md5Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.md5(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"MD5 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break
# SHA
async def SHA256Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.sha256(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"SHA256 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break

async def SHA384Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.sha384(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"SHA384 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break

async def SHA224Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.sha224(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"SHA224 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break

async def SHA1Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.sha1(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"SHA1 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break

async def SHA512Check(tr):
    st = time.monotonic()
    for s in allAplhabets():
        hash = hashlib.sha512(bytes(s, encoding="utf-8")).hexdigest()
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"SHA512 Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break

# Bcrypt check
async def bcryptCheck(tr):
    st = time.monotonic()
    for s in allAplhabets():
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes(s, encoding="utf-8"), salt).decode("utf-8")
        print(f"- {s} | {hash}")
        if hash == tr:
            elapsed = getElapsed(st)
            print(f"Bcrypt Found | {s} = {hash}")
            print(f"Took: {elapsed}")
            break
    
#asyncio.run(SHA512Check(target))
asyncio.run(executeAll(target))