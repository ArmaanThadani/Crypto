#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """

    slug_list = [key[0]]

    for i in range(1,len(key)):
        found = False
        for k in range(0,len(slug_list)):
            if slug_list[k] == key[i]:
                found = True
        if not found:
            slug_list.append(key[i].lower())

    for i in range(0,len(ALPHABET)):
        found = False
        for k in range(0,len(slug_list)):
            if ALPHABET[i] == slug_list[k]:
                found = True
        if not found:
            slug_list.append(ALPHABET[i])

    return slug_list




def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise
    return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'd')
    'c'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, '\\n')
    '\\n'
    """

    index = 0

    if ch != '\\n' and ch != '\n':
        while index < len(source):
            if ch.lower() == source[index]:
                return slug[index]
            else:
                index = index + 1

    return ch


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.\\n')
    'Zmc khjd z sgtmcdqanks gd ezkkr.\\n'
    """
    final = ""
    for i in range(0, len(s)):

        final = final + encrypt_char(source, slug, s[i])

    return final




def decrypt_str(source, slug, s):
    """
    Given source and slug lists, and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """

    final = ""
    for i in range(0, len(s)):
        final = final + encrypt_char(slug, source, s[i])

    return final

def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    f = open(filename, 'r')

    slug = compute_slug(key)
    output = f.readline()
    final = encrypt_str(ALPHABET, slug, output)

    while output != "":
        output = f.readline()
        final = final + encrypt_str(ALPHABET, slug, output)

    f.close()

    return final


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    f = open(filename, 'r')

    slug = compute_slug(key)
    output = f.readline()
    final = decrypt_str(ALPHABET, slug, output)

    while output != "":
        output = f.readline()
        final = final + decrypt_str(ALPHABET, slug, output)

    f.close()

    return final


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.

    if args[0] == "-encrypt":
        print(encrypt_file(args[2], args[1]))

    if args[0] == "-decrypt":
        print(decrypt_file(args[2], args[1]))
