import pymysql
from app import app
from config import mysql
from flask import jsonify ,flash, request ,render_template , url_for,redirect

# MOHON DENGAN SANGAT INI UNTUK HTML JANGAN DIGANGGU BARIS 6-14
@app.route('/')
def semuakursus():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM bimbel")
    kursus = cursor.fetchall()
    return render_template('index.html', all_text = kursus)
@app.route('/tambahkursus',methods=['GET','POST'])
def halamantambahkursus():
    if request.method == 'GET':
        return  render_template('tambahkursus.html')
    if request.method == 'POST':
        tgl_pendaftaran = request.form['tgl_pendaftaran']
        nama = request.form['nama']
        alamat = request.form['alamat']
        telp = request.form['telp']
        jeniskelamin = request.form['jeniskelamin']
        jeniskursus = request.form['jeniskursus']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sqlQuery = "INSERT INTO bimbel(tgl_pendaftaran , nama, alamat, telp, jeniskelamin, jeniskursus) VALUES (%s,%s,%s,%s,%s,%s)"
        bindData = (tgl_pendaftaran, nama, alamat, telp, jeniskelamin, jeniskursus)
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        return redirect('/')
@app.route('/halamaneditkursus/<int:no>',methods=['GET','POST'])
def halamaneditkursus(no):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT no, tgl_pendaftaran, nama, alamat, telp, jeniskelamin, jeniskursus FROM bimbel WHERE no =%s",no)
        empRow = cursor.fetchall()
        return render_template('/editkursus.html',no=empRow)
    if request.method == 'POST':
        tgl_pendaftaran = request.form['tgl_pendaftaran']
        nama = request.form['nama']
        alamat = request.form['alamat']
        telp = request.form['telp']
        jeniskelamin = request.form['jeniskelamin']
        jeniskursus = request.form['jeniskursus']
        if nama and alamat and telp and tgl_pendaftaran and jeniskelamin and jeniskursus and no and request.method == 'POST':			
            sqlQuery = "UPDATE bimbel SET nama=%s, alamat=%s, telp=%s, jeniskelamin=%s, jeniskursus=%s, tgl_pendaftaran=%s WHERE no=%s"
            bindData = (nama, alamat, telp, jeniskelamin, jeniskursus, tgl_pendaftaran, no,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            return redirect('/')
@app.route('/halamanhapuskursus/<int:no>',methods=['GET','POST'])
def halamanhapuskursus(no):
    if request.method == "POST":
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bimbel WHERE no =%s", (no,))
        conn.commit()
        return redirect('/')
# BATAS BARIS HTML TOLONG JANGAN DIGANGGU BARIS 14 -6

# untuk menambahkan data kursus (_create_)
@app.route('/create',methods=['POST'])
def tambah_bimbel():
    try:
        _json = request.json
        _tgl_pendaftaran = _json['tgl_pendaftaran']
        _nama = _json['nama']
        _alamat = _json['alamat']
        _telp = _json['telp']
        _jeniskelamin = _json['jeniskelamin']
        _jeniskursus = _json['jeniskursus']
        if _tgl_pendaftaran and _nama and _alamat and _telp and _jeniskelamin and _jeniskursus and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO bimbel(tgl_pendaftaran , nama, alamat, telp, jeniskelamin, jeniskursus) VALUES (%s,%s,%s,%s,%s,%s)"
            bindData = (_tgl_pendaftaran, _nama, _alamat, _telp, _jeniskelamin, _jeniskursus)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respon = jsonify("data berhasil ditambah")
            respon.status_code = 200
            return respon
        else:
            return jsonify("data tidak bisa ditambah")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# untuk mengambil data (_read_)
@app.route('/datakursus')
def databimbel():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM bimbel")
        kursus = cursor.fetchall()
        responn = jsonify(kursus)
        responn.status_code = 200
        return responn
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# untuk mencari data secara detail
@app.route('/show/<int:id>')
def getdetaildata(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT no, tgl_pendaftaran, nama, alamat, telp, jeniskelamin, jeniskursus FROM bimbel WHERE no =%s",id)
        empRow = cursor.fetchone()
        responnn = jsonify(empRow)
        responnn.status_code = 200
        return responnn
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# untuk mengupdate data  kursus
@app.route('/updatekursus', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _no = _json['no']
        _nama = _json['nama']
        _alamat = _json['alamat']
        _telp = _json['telp']
        _tgl_pendaftaran = _json['tgl_pendaftaran']
        _jeniskelamin = _json['jeniskelamin']
        _jeniskursus = _json['jeniskursus']
        if _nama and _alamat and _telp and _tgl_pendaftaran and _jeniskelamin and _jeniskursus and _no and request.method == 'PUT':			
            sqlQuery = "UPDATE bimbel SET nama=%s, alamat=%s, telp=%s, jeniskelamin=%s, jeniskursus=%s, tgl_pendaftaran=%s WHERE no=%s"
            bindData = (_nama, _alamat, _telp, _jeniskelamin, _jeniskursus, _tgl_pendaftaran, _no,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('data berhasil diupdate')
            respone.status_code = 200
            return respone
        else:
            return jsonify('datanya nggak ada')
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

# untuk delete data kursus
@app.route('/hapuskursus/<int:no>', methods=['DELETE'])
def delete_emp(no):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM bimbel WHERE no =%s", (no,))
		conn.commit()
		respone = jsonify('data berhasil dihapus')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# pengendali kode tolong jangan dihapus 
if __name__ == "__main__":
    app.run(debug=True) 