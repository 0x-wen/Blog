def bytes_str(data):
    """将bytes -> str"""
    if isinstance(data, bytes):
        data_string = data.decode()
        print(data_string)
    else:
        print('传入的数据类型需要为： bytes')


if __name__ == "__main__":
    bytes_data = b"\xe7\xb3\xbb\xe7\xbb\x9f\xe9\x94\x99\xe8\xaf\xaf,\xe8\xaf\xb7\xe7\xa8\x8d\xe5\x90\x8e\xe9\x87\x8d\xe8\xaf\x95~"
    bytes_str(bytes_data)
