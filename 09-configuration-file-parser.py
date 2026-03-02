import configparser

def LOAD_CONFIG(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    
    if "DATABASE" not in config:
        raise ValueError("Missing 'database' section")

    db_config = {
        "host":     config.get("DATABASE", "host"),
        "port":     config.getint("DATABASE", "port"),
        "user":     config.get("DATABASE", "user"),
        "password": config.get("DATABASE", "password"),
    }

    return db_config

if __name__ == "__main__":
    settings = LOAD_CONFIG("config.ini")
    print(f"DATABASE SETTINGS: {settings}")
    
    """_output_
        DATABASE SETTINGS: {
            'host': 'localhost', 
            'port': 5432, 
            'user': 'admin', 
            'password': 'secret'
        }
    """