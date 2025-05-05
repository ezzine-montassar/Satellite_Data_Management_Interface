from flask import Flask, render_template, request, flash, jsonify, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
#clé secréte
app.secret_key = 's3cr3tP@ssw0rd_DB_Project_2025'

def get_db_connection():
    conn = sqlite3.connect('DB_Project.db')
    conn.row_factory = sqlite3.Row  # Pour accéder avec des clés
    return conn



@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    data = {}
    tables = [
        "Agences_Spatiales", "Satellites", "Instrument_Embarqués", "Anomalie",
        "Missions", "Données_Satellites", "Zones", "Observation",
        "Stations_terrestres", "Communication", "Sat_Telecom_Navigation",
        "Observation_De_Donnees", "Sat_Recherche", "Sat_Militaire"
    ]

    for table in tables:
        try:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(f"SELECT * FROM {table}").fetchall()
            data[table] = rows
        except Exception as e:
            data[table] = f"Erreur: {e}"

    conn.close()
    return render_template("index.html", data=data)


@app.route("/filtrer", methods=["POST"])
def filtrer():
    filtered_result = None
    sql_query = request.form.get("sql_query")
    if sql_query:
        try:
            conn = get_db_connection()
            conn.row_factory = sqlite3.Row
            if sql_query.strip().lower().startswith("select"):
                filtered_result = conn.execute(sql_query).fetchall()
            else:
                filtered_result = "Seules les requêtes SELECT sont autorisées."
            conn.close()
        except Exception as e:
            filtered_result = f"Erreur dans la requête : {e}"

    return render_template("index.html", filtered_result=filtered_result)






@app.route('/insertion/AS', methods=['POST'])
def insertion_AS():
    ID = request.form.get('ID_agence_insert')
    nom = request.form.get('nom_agence_insert')
    pays = request.form.get('pays_agence_insert')

    conn = get_db_connection()
    cursor = conn.cursor()
    # Insertion
    cursor.execute("""
	INSERT INTO Agences_Spatiales (agence_id,nom, pays)
	VALUES (?, ?, ?)
	""", (ID, nom, pays))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/insertion/Sat', methods=['POST'])
def insertion_Sat():
    ID = request.form.get('ID_sat_insert')
    parent_id = request.form.get('parent_id_sat_insert')
    agence_id = request.form.get('agence_id_sat_insert')
    type_orbite = request.form.get('type_orbite_sat_insert')
    statut = request.form.get('statut_sat_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Satellites (satellite_id,parent_id, agence_id, type_orbite, statut )
	VALUES (?, ?, ?, ?, ?)
	""", (ID, parent_id, agence_id,type_orbite, statut))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/insertion/IE', methods=['POST'])
def insertion_IE():
    ID = request.form.get('ID_instrument_insert')
    satellite_id = request.form.get('satellite_id_instrument_insert')
    type = request.form.get('type_instrument_insert')
    resolution = request.form.get('resolution_instrument_insert')
    statut = request.form.get('statut_instrument_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Instrument_Embarqués (instrument_id,satellite_id, type, resolution, statut )
	VALUES (?, ?, ?, ?, ?)
	""", (ID, satellite_id, type,resolution , statut))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/insertion/AN', methods=['POST'])
def insertion_AN():
    ID = request.form.get('ID_anomalie_insert')
    satellite_id = request.form.get('satellite_id_anomalie_insert')
    instrument_id = request.form.get('instr_id_anomalie_insert')
    type = request.form.get('type_anomalie_insert')
    description = request.form.get('desc_anomalie_insert')
    date_detct = request.form.get('date_detect_anomalie_insert')
    statut = request.form.get('statut_instrument_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Anomalie (anomalie_id, satellite_id, instrument_id, type, description, date_détection, statut )
	VALUES (?, ?, ?, ?, ?, ?, ?)
	""", (ID, satellite_id, instrument_id, type,description, date_detct , statut))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))





@app.route('/insertion/MIS', methods=['POST'])
def insertion_MIS():
    ID = request.form.get('ID_mission_insert')
    satellite_id = request.form.get('satellite_id_mission_insert')
    type_data = request.form.get('type_data_mission_insert')
    date_deb = request.form.get('date_deb_mission_insert')
    date_fin = request.form.get('date_fin_mission_insert')
    pri = request.form.get('pri_mission_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Missions (mission_id, satellite_id, type_donnée, date_début, date_fin, priorité )
	VALUES (?, ?, ?, ?, ?, ?)
	""", (ID, satellite_id, type_data, date_deb, date_fin , pri))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))




@app.route('/insertion/DS', methods=['POST'])
def insertion_DS():
    ID = request.form.get('ID_donnée_insert')
    mission_id = request.form.get('id_mission_donnée_insert')
    fname = request.form.get('fname_data_insert')
    fpath = request.form.get('path_data_insert')
    date_ajout = request.form.get('date_ajout_data_insert')


    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Données_Satellites (donnée_id, mission_id, nom_fichier, chemin_stockage ,date_ajout )
	VALUES (?, ?, ?, ?, ?)
	""", (ID, mission_id, fname, fpath, date_ajout))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/insertion/Z', methods=['POST'])
def insertion_Z():
    ID = request.form.get('ID_zone_insert')
    nom = request.form.get('nom_zone_insert')
    pays = request.form.get('pays_zone_insert')
    lat = request.form.get('lat_zone_insert')
    long = request.form.get('long_zone_insert')


    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Zones (zone_id, nom, pays, latitude ,longitude )
	VALUES (?, ?, ?, ?, ?)
	""", (ID, nom, pays, lat, long))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/insertion/OBS', methods=['POST'])
def insertion_OBS():
    sat_ID = request.form.get('ID_sat_obs_insert')
    zone_ID = request.form.get('ID_zone_obs_insert')


    conn = get_db_connection()
    cursor = conn.cursor()
    # Insertion
    cursor.execute("""
	INSERT INTO Observation (satellite_id,zone_id)
	VALUES (?, ?)
	""", (sat_ID, zone_ID))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/insertion/STR', methods=['POST'])
def insertion_STR():
    ID = request.form.get('ID_station_insert')
    nom = request.form.get('nom_station_insert')
    pays = request.form.get('pays_station_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Stations_terrestres (station_id, nom, pays)
	VALUES (?, ?, ?)
	""", (ID, nom, pays))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/insertion/COM', methods=['POST'])
def insertion_COM():
    sat_ID = request.form.get('sat_id_com_insert')
    station_ID = request.form.get('station_id_com_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Communication (satellite_id, station_id)
	VALUES (?, ?)
	""", (sat_ID, station_ID))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/insertion/STN', methods=['POST'])
def insertion_STN():
    sat_id = request.form.get('sat_id_stn_insert')
    bande_freq = request.form.get('bf_stn_insert')
    cp_trn = request.form.get('ctr_stn_insert')
    prec = request.form.get('prloc_stn_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Anomalie (satellite_id, bande_frequence, capacite_transmission, precision_localisation )
	VALUES (?, ?, ?, ?)
	""", (sat_id, bande_freq, cp_trn, prec))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))





@app.route('/insertion/ODD', methods=['POST'])
def insertion_ODD():
    sat_id = request.form.get('sat_id_odd_insert')
    res = request.form.get('res_spc_odd_insert')
    freq = request.form.get('freq_pass_odd_insert')
    type_img = request.form.get('type_img_odd_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Observation_De_Donnees (satellite_id, resolution_spectrale, frequence_passage, type_image )
	VALUES (?, ?, ?, ?)
	""", (sat_id, res, freq, type_img))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))




@app.route('/insertion/SR', methods=['POST'])
def insertion_SR():
    sat_ID = request.form.get('id_sat_SR_insert')
    domain = request.form.get('dom_SR_insert')
    type_instr = request.form.get('type_instr_SR_insert')
    prec = request.form.get('prec_mes_SR_insert')

    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Sat_Recherche (satellite_id, domaine_recherche, type_instrumentation, precision_mesure )
	VALUES (?, ?, ?, ?)
	""", (sat_ID, domain, type_instr, prec))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/insertion/SM', methods=['POST'])
def insertion_SM():
    sat_ID = request.form.get('sat_id_SM_insert')
    niv_sec = request.form.get('niv_sec_SM_insert')
    crypt = request.form.get('crypt_SM_insert')
    type_miss = request.form.get('type_miss_SM_insert')



    conn = get_db_connection()
    cursor = conn.cursor()

    #  Insertion

    cursor.execute("""
	INSERT INTO Sat_Militaire (satellite_id, niveau_securite, cryptage, type_mission_militaire )
	VALUES (?, ?, ?, ?)
	""", (sat_ID, niv_sec, crypt, type_miss))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))




#Suppression
@app.route('/supprimer', methods=['POST'])
def supprimer():
    tables = [
        "Agences_Spatiales", "Satellites", "Instrument_Embarqués", "Anomalie",
        "Missions", "Données_Satellites", "Zones", "Observation",
        "Stations_terrestres", "Communication", "Sat_Telecom_Navigation",
        "Observation_De_Donnees", "Sat_Recherche", "Sat_Militaire"
    ]

    id_columns = {
        "Agences_Spatiales": "agence_id",
        "Satellites": "satellite_id",
        "Instrument_Embarqués": "instrument_id",
        "Anomalie": "anomalie_id",
        "Missions": "mission_id",
        "Données_Satellites": "donnée_id",
        "Zones": "zone_id",
        "Observation": ["satellite_id", "zone_id"],
        "Stations_terrestres": "station_id",
        "Communication": ["satellite_id", "station_id"],
        "Sat_Telecom_Navigation": "satellite_id",
        "Observation_De_Donnees": "satellite_id",
        "Sat_Recherche": "satellite_id",
        "Sat_Militaire": "satellite_id"
    }

    # Récupération des champs du formulaire
    table = request.form.get('type-suppression')
    identifiant = request.form.get('ID_Suppression')
    id1 = request.form.get('ID1_Suppression')
    id2 = request.form.get('ID2_Suppression')

    if table not in tables:
        abort(400, description="Type de suppression non valide")

    id_col = id_columns.get(table)
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        if isinstance(id_col, list):
            # Cas avec clé primaire composée
            if not id1 or not id2:
                abort(400, description="Deux identifiants sont requis pour cette table.")
            ids = (id1, id2)
            condition = " AND ".join(f"{col} = ?" for col in id_col)
            cursor.execute(f"SELECT * FROM {table} WHERE {condition}", ids)
            row = cursor.fetchone()

            if row:
                cursor.execute(f"DELETE FROM {table} WHERE {condition}", ids)

        else:
            # Cas avec clé primaire simple
            if not identifiant:
                abort(400, description="Un identifiant est requis pour cette table.")
            cursor.execute(f"SELECT * FROM {table} WHERE {id_col} = ?", (identifiant,))
            row = cursor.fetchone()

            if row:
                cursor.execute(f"DELETE FROM {table} WHERE {id_col} = ?", (identifiant,))

        conn.commit()

    except Exception as e:
        conn.rollback()
        abort(500, description=f"Erreur lors de la suppression : {e}")

    finally:
        conn.close()

    return redirect(url_for('index'))




#Partie de la Modification

@app.route('/modification/AS', methods=['POST'])
def modifier_AS():
    agence_id = request.form.get("ID_agence_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "nom": "nom_agence_mod",
        "pays": "pays_agence_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(agence_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Agences_Spatiales SET {', '.join(updates)} WHERE agence_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/modification/Sat', methods=['POST'])
def modifier_Sat():
    satellite_id= request.form.get("ID_sat_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "parent_id": "parent_id_sat_mod",
        "agence_id": "agence_id_sat_mod",
        "type_orbite": "type_orbite_sat_mod",
        "statut": "statut_sat_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(satellite_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Satellites SET {', '.join(updates)} WHERE satellite_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/IE', methods=['POST'])
def modifier_IE():
    instrument_id= request.form.get("ID_instrument_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "satellite_id": "satellite_id_instrument_mod",
        "type": "type_instrument_mod",
        "resolution": "resolution_instrument_mod",
        "statut": "statut_instrument_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(instrument_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Instrument_Embarqués SET {', '.join(updates)} WHERE instrument_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/AN', methods=['POST'])
def modifier_AN():
    anomalie_id= request.form.get("ID_anomalie_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "satellite_id": "satellite_id_anomalie_mod",
        "instrument_id": "instr_id_anomalie_mod",
        "type": "type_anomalie_mod",
        "description": "desc_anomalie_mod",
        "date_détection": "date_detect_anomalie_mod",
        "statut": "statut_anomalie_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(anomalie_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Anomalie SET {', '.join(updates)} WHERE anomalie_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/MIS', methods=['POST'])
def modifier_MIS():
    mission_id= request.form.get("ID_mission_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "satellite_id": "satellite_id_mission_mod",
        "type_donnée": "type_data_mission_mod",
        "date_début": "date_deb_mission_mod",
        "date_fin": "date_fin_mission_mod",
        "priorité": "pri_mission_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(mission_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Missions SET {', '.join(updates)} WHERE mission_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/DS', methods=['POST'])
def modifier_DS():
    donnée_id= request.form.get("ID_donnée_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "mission_id": "id_mission_donnée_mod",
        "nom_fichier": "fname_data_mod",
        "chemin_stockage": "path_data_mod",
        "date_ajout": "date_ajout_data_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(donnée_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Données_Satellites SET {', '.join(updates)} WHERE donnée_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/modification/Z', methods=['POST'])
def modifier_Z():
    zone_id= request.form.get("ID_zone_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "nom": "nom_zone_mod",
        "pays": "pays_zone_mod",
        "latitude": "lat_zone_mod",
        "longitude": "long_zone_mod"
    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(zone_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Zones SET {', '.join(updates)} WHERE zone_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/modification/STR', methods=['POST'])
def modifier_STR():
    station_id= request.form.get("ID_station_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "nom": "nom_station_mod",
        "pays": "pays_station_mod"

    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(station_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Stations_terrestres SET {', '.join(updates)} WHERE station_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/STN', methods=['POST'])
def modifier_STN():
    satellite_id= request.form.get("sat_id_stn_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "bande_frequence": "bf_stn_mod",
        "capacite_transmission": "ctr_stn_mod",
        "precision_localisation": "prloc_stn_mod"

    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(satellite_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Sat_Telecom_Navigation SET {', '.join(updates)} WHERE satellite_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/modification/ODD', methods=['POST'])
def modifier_ODD():
    satellite_id= request.form.get("sat_id_odd_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "resolution_spectrale": "res_spc_odd_mod",
        "frequence_passage": "freq_pass_odd_mod",
        "type_image": "type_img_odd_mod"

    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(satellite_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Observation_De_Donnees SET {', '.join(updates)} WHERE satellite_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/modification/SR', methods=['POST'])
def modifier_SR():
    satellite_id= request.form.get("id_sat_SR_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "domaine_recherche": "dom_SR_mod",
        "type_instrumentation": "type_instr_SR_mod",
        "precision_mesure": "prec_mes_SR_mod"

    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(satellite_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Sat_Recherche SET {', '.join(updates)} WHERE satellite_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/modification/SM', methods=['POST'])
def modifier_SM():
    satellite_id= request.form.get("sat_id_SM_mod")

    # Clés : nom en base | Valeurs : nom du champ dans le formulaire HTML
    champs_formulaire = {
        "niveau_securite": "niv_sec_SM_mod",
        "cryptage": "crypt_SM_mod",
        "type_mission_militaire": "type_miss_SM_mod"

    }

    updates = []
    values = []

    for colonne_sql, champ_html in champs_formulaire.items():
        valeur = request.form.get(champ_html)
        if valeur not in [None, ""]:
            updates.append(f"{colonne_sql} = ?")
            values.append(valeur)

    if not updates:
        return "Aucune donnée à modifier.", 400

    values.append(satellite_id)  # ID à la fin pour le WHERE

    query = f"UPDATE Sat_Militaire SET {', '.join(updates)} WHERE satellite_id = ?"

    conn = get_db_connection()
    conn.execute(query, values)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))












if __name__ == '__main__':
    app.run(host='192.168.114.142', port=5000, debug=True)

