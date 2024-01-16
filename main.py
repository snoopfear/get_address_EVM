from eth_keys import keys

def get_ethereum_addresses_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        private_keys_hex = file.read().splitlines()

    with open(output_file, 'w') as file:
        for private_key_hex in private_keys_hex:
            try:
                # Удаление префикса '0x', если он присутствует
                if private_key_hex.startswith("0x"):
                    private_key_hex = private_key_hex[2:]
                    
                # Преобразование приватного ключа из шестнадцатеричного формата в байты
                private_key_bytes = bytes.fromhex(private_key_hex)

                # Создание объекта приватного ключа
                private_key = keys.PrivateKey(private_key_bytes)

                # Получение публичного ключа
                public_key = private_key.public_key

                # Получение адреса Ethereum
                eth_address = public_key.to_checksum_address()

                file.write(eth_address + '\n')
            except Exception as e:
                print(f"Ошибка обработки ключа {private_key_hex}: {e}")

# Использование функции
input_file = 'private_keys.txt'  # Путь к файлу с приватными ключами
output_file = 'addresses.txt' # Путь к файлу для записи адресов Ethereum
get_ethereum_addresses_from_file(input_file, output_file)
