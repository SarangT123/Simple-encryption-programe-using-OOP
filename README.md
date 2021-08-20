# A simple encryption programe using python OOP

## how to use

---

<details>
<summary>Initializing</summary>
```py
encrypter = encryption()
```

</details>
<details>
<summary>Getting the encryption key</summary>
```py
encrypter.generate_key()
#returns the key
```
</details>
<details>
<summary>Initializing</summary>

<code lang="lang-py">
encrypter.encrypt(<"key">, <"string">)

#here this will return the encrypted text
</code>

</details>

<details>
<summary>Decrypting</summary>

<code lang="lang-py">
encrypter.decrypt(<key>, <encrypted text>)
#returns decrypted text
</code>
</details>
