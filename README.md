# A simple encryption programe using python OOP

## how to use

---

<details>
<summary>Initializing</summary>
<code lang="lang-py">
encrypter = encryption()
</code>

</details>
<details>
<summary>Getting the encryption key</summary>
<code lang="lang-py">
encrypter.generate_key()

#returns the key
</code>

</details>
<details>
<summary>Encrypting</summary>

<code lang="lang-py">
encrypter.encrypt(<"key">, <"string">)

#here this will return the encrypted text
</code>

</details>

<details>
<summary>Decrypting</summary>

<code lang="lang-py">
encrypter.decrypt(<"key">, <"encrypted text">)

#returns decrypted text
</code>

</details>
