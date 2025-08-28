import pymysql

# Infos de ta base Railway
my_host = "yamabiko.proxy.rlwy.net"
my_user = "root"
my_password = "VorbxjEDuMCnUqxIDOLrHvNjWiSQDFoX"
my_db = "railway"
my_port = 33943

# Connexion à Railway
conn = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_db,
    port=my_port,
    cursorclass=pymysql.cursors.DictCursor
)

cur = conn.cursor()

# Lire le fichier SQL
with open("medijutsu_data_export.sql", "r", encoding="utf8") as f:
    sql_commands = f.read().split(';')  # Sépare chaque commande

# Exécuter les commandes
for command in sql_commands:
    if command.strip():
        cur.execute(command)

conn.commit()
conn.close()

print("Import terminé ✅")
