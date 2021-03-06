import random

string = """0¶1¶2¶3¶4¶5¶6¶7¶8¶9¶a¶b¶c¶d¶e¶f¶g¶h¶i¶j¶k¶l¶m¶n¶o¶p¶q¶r¶s¶t¶u¶v¶w¶x¶y¶z¶A¶B¶C¶D¶E¶F¶G¶H¶I¶J¶K¶L¶M¶N¶O¶P¶Q¶R¶S¶T¶U¶V¶W¶X¶Y¶Z¶`¶~¶!¶@¶#¶$¶%¶^¶&¶*¶(¶)¶-¶_¶=¶+¶[¶]¶\¶{¶}¶|¶;¶'¶:¶"¶,¶.¶/¶<¶>¶?¶ """
keywords = string.split("¶")


class Encryption:

    def generate_key(self):
        seed = (random.randint(0, 2000000000))
        random.seed(seed)
        encrypted = []
        for i in range(94):
            key = str(random.randint(0, 10000000))
            if key in encrypted:
                def redo():
                    key = str(random.randint(0, 10000000))
                    if key in encrypted:
                        redo()
                    else:
                        encrypted.append(key)
                redo()
            else:
                encrypted.append(key)
        return [seed, encrypted]

    def encrypt(self, encryption_key: int, text: str) -> str:
        random.seed(encryption_key)
        key = []
        for i in range(94):
            key.append(str(random.randint(0, 10000000)))
        for i in range(94):
            text = str(text.replace(keywords[i], key[i]))
        return text

    def decrypt(self, encryption_key: int, encrypted_text: str) -> str:
        random.seed(encryption_key)
        key = []
        for i in range(94):
            key.append(str(random.randint(0, 10000000)))
        for i in range(94):
            encrypted_text = encrypted_text.replace(key[i], keywords[i])
        return encrypted_text
